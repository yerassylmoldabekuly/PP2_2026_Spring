import pygame
import random
import json
from db import get_personal_best

WIDTH = 640
HEIGHT = 640
BLOCK = 20

BG_COLOR = (20, 20, 20)
FOOD_COLOR = (220, 50, 50)
POISON_COLOR = (120, 0, 0)
SPEED_BOOST_COLOR = (80, 180, 255)
SLOW_MOTION_COLOR = (180, 180, 255)
SHIELD_COLOR = (255, 220, 80)
OBSTACLE_COLOR = (90, 90, 90)
GRID_COLOR = (40, 40, 40)


def load_settings():
    try:
        with open("settings.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "snake_color": [0, 220, 0],
            "grid": True,
            "sound": True
        }


class Snake:
    def __init__(self, x, y):
        self.body = [(x, y), (x - BLOCK, y), (x - 2 * BLOCK, y)]
        self.direction = "RIGHT"
        self.grow_pending = 0

    def set_direction(self, new_direction):
        opposite = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }
        if opposite[self.direction] != new_direction:
            self.direction = new_direction

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            head_y -= BLOCK
        elif self.direction == "DOWN":
            head_y += BLOCK
        elif self.direction == "LEFT":
            head_x -= BLOCK
        elif self.direction == "RIGHT":
            head_x += BLOCK

        self.body.insert(0, (head_x, head_y))

        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self, amount=1):
        self.grow_pending += amount

    def shrink(self, amount=2):
        for _ in range(amount):
            if len(self.body) > 1:
                self.body.pop()

    def head(self):
        return self.body[0]

    def collided_with_self(self):
        return self.body[0] in self.body[1:]


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.weight = 1
        self.color = FOOD_COLOR
        self.spawn_time = 0
        self.life_time = 6000

    def respawn(self, snake_body, obstacles):
        food_type = random.choice([
            {"weight": 1, "color": (220, 50, 50), "life_time": 7000},
            {"weight": 2, "color": (255, 165, 0), "life_time": 5000},
            {"weight": 3, "color": (255, 215, 0), "life_time": 3500},
        ])

        self.weight = food_type["weight"]
        self.color = food_type["color"]
        self.life_time = food_type["life_time"]

        self.position = random_free_cell(snake_body, obstacles)
        self.spawn_time = pygame.time.get_ticks()

    def expired(self):
        return pygame.time.get_ticks() - self.spawn_time > self.life_time


class PoisonFood:
    def __init__(self):
        self.position = None

    def respawn(self, snake_body, obstacles, food_pos):
        while True:
            pos = random_free_cell(snake_body, obstacles)
            if pos != food_pos:
                self.position = pos
                return


class PowerUp:
    def __init__(self):
        self.kind = None
        self.position = None
        self.spawn_time = 0
        self.field_duration = 8000

    def spawn(self, snake_body, obstacles, food_pos, poison_pos):
        self.kind = random.choice(["speed", "slow", "shield"])
        while True:
            pos = random_free_cell(snake_body, obstacles)
            if pos != food_pos and pos != poison_pos:
                self.position = pos
                self.spawn_time = pygame.time.get_ticks()
                return

    def expired_on_field(self):
        return self.position is not None and pygame.time.get_ticks() - self.spawn_time > self.field_duration


def random_free_cell(snake_body, obstacles):
    while True:
        x = random.randrange(1, WIDTH // BLOCK - 1) * BLOCK
        y = random.randrange(1, HEIGHT // BLOCK - 1) * BLOCK
        pos = (x, y)
        if pos not in snake_body and pos not in obstacles:
            return pos


def build_border_walls():
    walls = set()
    for x in range(0, WIDTH, BLOCK):
        walls.add((x, 0))
        walls.add((x, HEIGHT - BLOCK))
    for y in range(0, HEIGHT, BLOCK):
        walls.add((0, y))
        walls.add((WIDTH - BLOCK, y))
    return walls


def generate_level_obstacles(level, snake_body):
    if level < 3:
        return set()

    obstacles = set()
    count = min(4 + level, 14)

    safe_zone = set()
    head_x, head_y = snake_body[0]
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            safe_zone.add((head_x + dx * BLOCK, head_y + dy * BLOCK))

    while len(obstacles) < count:
        x = random.randrange(2, WIDTH // BLOCK - 2) * BLOCK
        y = random.randrange(2, HEIGHT // BLOCK - 2) * BLOCK
        pos = (x, y)

        if pos not in snake_body and pos not in safe_zone:
            obstacles.add(pos)

    return obstacles


class SnakeGame:
    def __init__(self, username):
        self.username = username
        self.settings = load_settings()
        self.snake_color = tuple(self.settings["snake_color"])
        self.grid_on = self.settings["grid"]

        self.font = pygame.font.SysFont("Arial", 24)
        self.big_font = pygame.font.SysFont("Arial", 38, bold=True)

        self.border_walls = build_border_walls()
        self.personal_best = get_personal_best(username)

        self.reset()

    def reset(self):
        self.snake = Snake(200, 200)
        self.food = Food()
        self.poison = PoisonFood()
        self.powerup = PowerUp()

        self.score = 0
        self.level = 1
        self.base_speed = 8
        self.current_speed = self.base_speed

        self.active_powerup = None
        self.powerup_end_time = 0
        self.shield_available = False

        self.level_obstacles = generate_level_obstacles(self.level, self.snake.body)
        all_obstacles = self.border_walls | self.level_obstacles

        self.food.respawn(self.snake.body, all_obstacles)
        self.poison.respawn(self.snake.body, all_obstacles, self.food.position)

        self.game_over = False

        self.move_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.move_event, 1000 // self.current_speed)

    def update_speed(self):
        speed = self.base_speed + (self.level - 1) * 2

        if self.active_powerup == "speed":
            speed += 4
        elif self.active_powerup == "slow":
            speed = max(4, speed - 3)

        self.current_speed = speed
        pygame.time.set_timer(self.move_event, max(50, 1000 // self.current_speed))

    def activate_powerup(self, kind):
        self.active_powerup = kind

        if kind == "shield":
            self.shield_available = True
            self.powerup_end_time = 0
        else:
            self.powerup_end_time = pygame.time.get_ticks() + 5000

        self.update_speed()

    def check_powerup_timeout(self):
        if self.active_powerup in ("speed", "slow"):
            if pygame.time.get_ticks() >= self.powerup_end_time:
                self.active_powerup = None
                self.update_speed()

    def level_up_if_needed(self):
        new_level = 1 + self.score // 6
        if new_level != self.level:
            self.level = new_level
            self.level_obstacles = generate_level_obstacles(self.level, self.snake.body)
            self.update_speed()

            all_obstacles = self.border_walls | self.level_obstacles
            self.food.respawn(self.snake.body, all_obstacles)
            self.poison.respawn(self.snake.body, all_obstacles, self.food.position)
            self.powerup.position = None

    def handle_collision(self):
        head = self.snake.head()
        obstacles = self.border_walls | self.level_obstacles

        if head in obstacles or self.snake.collided_with_self():
            if self.shield_available:
                self.shield_available = False
                self.active_powerup = None
                return
            self.game_over = True

    def update(self):
        self.check_powerup_timeout()

        if self.food.expired():
            all_obstacles = self.border_walls | self.level_obstacles
            self.food.respawn(self.snake.body, all_obstacles)

        if self.powerup.position is not None and self.powerup.expired_on_field():
            self.powerup.position = None

        if self.powerup.position is None and random.random() < 0.003:
            all_obstacles = self.border_walls | self.level_obstacles
            self.powerup.spawn(self.snake.body, all_obstacles, self.food.position, self.poison.position)

    def handle_move(self):
        if self.game_over:
            return

        self.snake.move()
        self.handle_collision()

        if self.game_over:
            return

        head = self.snake.head()
        all_obstacles = self.border_walls | self.level_obstacles

        if head == self.food.position:
            self.score += self.food.weight
            self.snake.grow(self.food.weight)
            self.food.respawn(self.snake.body, all_obstacles)
            self.poison.respawn(self.snake.body, all_obstacles, self.food.position)
            self.level_up_if_needed()

        elif head == self.poison.position:
            self.snake.shrink(2)
            if len(self.snake.body) <= 1:
                self.game_over = True
                return
            self.poison.respawn(self.snake.body, all_obstacles, self.food.position)

        elif self.powerup.position is not None and head == self.powerup.position:
            self.activate_powerup(self.powerup.kind)
            self.powerup.position = None

    def draw_grid(self, screen):
        if not self.grid_on:
            return
        for x in range(0, WIDTH, BLOCK):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, BLOCK):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

    def draw(self, screen):
        screen.fill(BG_COLOR)
        self.draw_grid(screen)

        # Walls
        for x, y in self.border_walls:
            pygame.draw.rect(screen, OBSTACLE_COLOR, (x, y, BLOCK, BLOCK))
        for x, y in self.level_obstacles:
            pygame.draw.rect(screen, (120, 120, 120), (x, y, BLOCK, BLOCK))

        # Food
        fx, fy = self.food.position
        pygame.draw.rect(screen, self.food.color, (fx, fy, BLOCK, BLOCK), border_radius=5)

        # Poison
        if self.poison.position:
            px, py = self.poison.position
            pygame.draw.rect(screen, POISON_COLOR, (px, py, BLOCK, BLOCK), border_radius=5)

        # Power-up
        if self.powerup.position:
            px, py = self.powerup.position
            color = {
                "speed": SPEED_BOOST_COLOR,
                "slow": SLOW_MOTION_COLOR,
                "shield": SHIELD_COLOR
            }[self.powerup.kind]
            pygame.draw.rect(screen, color, (px, py, BLOCK, BLOCK), border_radius=5)

        # Snake
        for i, (x, y) in enumerate(self.snake.body):
            color = self.snake_color if i > 0 else tuple(min(255, c + 20) for c in self.snake_color)
            pygame.draw.rect(screen, color, (x, y, BLOCK, BLOCK), border_radius=4)

        # HUD
        screen.blit(self.font.render(f"User: {self.username}", True, (255, 255, 255)), (10, 8))
        screen.blit(self.font.render(f"Score: {self.score}", True, (255, 255, 255)), (10, 36))
        screen.blit(self.font.render(f"Level: {self.level}", True, (255, 255, 0)), (150, 8))
        screen.blit(self.font.render(f"Best: {self.personal_best}", True, (180, 255, 180)), (150, 36))

        power_text = "None"
        if self.active_powerup == "speed":
            power_text = f"Speed {max(0, (self.powerup_end_time - pygame.time.get_ticks()) // 1000 + 1)}s"
        elif self.active_powerup == "slow":
            power_text = f"Slow {max(0, (self.powerup_end_time - pygame.time.get_ticks()) // 1000 + 1)}s"
        elif self.active_powerup == "shield":
            power_text = "Shield"

        screen.blit(self.font.render(f"Power: {power_text}", True, (255, 255, 255)), (350, 8))
        screen.blit(self.font.render(f"Len: {len(self.snake.body)}", True, (255, 255, 255)), (350, 36))