import pygame
import json
from game import SnakeGame, WIDTH, HEIGHT
from db import save_game_result, get_top_scores


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS4 Snake")
clock = pygame.time.Clock()

TITLE_FONT = pygame.font.SysFont("Arial", 42, bold=True)
FONT = pygame.font.SysFont("Arial", 28)
SMALL_FONT = pygame.font.SysFont("Arial", 22)


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


def save_settings(settings):
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)


class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, (220, 220, 220), self.rect, border_radius=10)
        pygame.draw.rect(screen, (50, 50, 50), self.rect, 2, border_radius=10)
        surf = FONT.render(self.text, True, (20, 20, 20))
        rect = surf.get_rect(center=self.rect.center)
        screen.blit(surf, rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


def draw_center(text, y, color=(255, 255, 255), font=FONT):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH // 2, y))
    screen.blit(surf, rect)


def username_input_screen():
    username = ""

    while True:
        screen.fill((20, 20, 30))
        draw_center("Enter Username", 150, font=TITLE_FONT)
        pygame.draw.rect(screen, (255, 255, 255), (120, 260, 400, 55), border_radius=8)
        pygame.draw.rect(screen, (40, 40, 40), (120, 260, 400, 55), 2, border_radius=8)

        text = FONT.render(username + "|", True, (0, 0, 0))
        screen.blit(text, (140, 275))
        draw_center("Enter = start, Esc = cancel", 380, color=(200, 200, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if username.strip():
                        return username.strip()
                elif event.key == pygame.K_ESCAPE:
                    return None
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if event.unicode.isprintable() and len(username) < 14:
                        username += event.unicode

        pygame.display.flip()
        clock.tick(60)


def leaderboard_screen():
    back_btn = Button(220, 570, 200, 50, "Back")

    while True:
        rows = get_top_scores()

        screen.fill((18, 18, 28))
        draw_center("Leaderboard", 70, font=TITLE_FONT)

        y = 140
        if rows:
            for i, row in enumerate(rows, start=1):
                username, score, level_reached, played_at = row
                line = f"{i}. {username} | Score {score} | Lvl {level_reached} | {played_at.strftime('%Y-%m-%d')}"
                surf = SMALL_FONT.render(line, True, (235, 235, 235))
                screen.blit(surf, (25, y))
                y += 38
        else:
            draw_center("No results yet", 250, color=(200, 200, 200))

        back_btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN and back_btn.is_clicked(event.pos):
                return "menu"

        pygame.display.flip()
        clock.tick(60)


def settings_screen(settings):
    back_btn = Button(200, 520, 240, 50, "Save & Back")
    snake_colors = [
        [0, 220, 0],
        [255, 80, 80],
        [80, 180, 255],
        [240, 220, 80]
    ]

    while True:
        screen.fill((22, 22, 30))
        draw_center("Settings", 80, font=TITLE_FONT)

        draw_center(f"Grid: {'ON' if settings['grid'] else 'OFF'}", 180)
        draw_center(f"Sound: {'ON' if settings['sound'] else 'OFF'}", 250)
        draw_center(f"Snake color: {settings['snake_color']}", 320)

        draw_center("Click lines to change", 400, color=(180, 180, 180), font=SMALL_FONT)

        pygame.draw.rect(screen, tuple(settings["snake_color"]), (280, 345, 80, 30))
        pygame.draw.rect(screen, (255, 255, 255), (280, 345, 80, 30), 2)

        back_btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if 180 - 20 <= y <= 180 + 20:
                    settings["grid"] = not settings["grid"]

                elif 250 - 20 <= y <= 250 + 20:
                    settings["sound"] = not settings["sound"]

                elif 320 - 20 <= y <= 320 + 40:
                    idx = snake_colors.index(settings["snake_color"]) if settings["snake_color"] in snake_colors else 0
                    settings["snake_color"] = snake_colors[(idx + 1) % len(snake_colors)]

                elif back_btn.is_clicked(event.pos):
                    save_settings(settings)
                    return "menu"

        pygame.display.flip()
        clock.tick(60)


def game_over_screen(score, level, personal_best):
    retry_btn = Button(220, 450, 200, 50, "Retry")
    menu_btn = Button(220, 520, 200, 50, "Main Menu")

    while True:
        screen.fill((30, 10, 10))
        draw_center("Game Over", 120, color=(255, 90, 90), font=TITLE_FONT)
        draw_center(f"Score: {score}", 240)
        draw_center(f"Level: {level}", 290)
        draw_center(f"Personal Best: {personal_best}", 340)

        retry_btn.draw(screen)
        menu_btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_btn.is_clicked(event.pos):
                    return "retry"
                if menu_btn.is_clicked(event.pos):
                    return "menu"

        pygame.display.flip()
        clock.tick(60)


def main_menu():
    play_btn = Button(220, 220, 200, 50, "Play")
    lb_btn = Button(220, 300, 200, 50, "Leaderboard")
    settings_btn = Button(220, 380, 200, 50, "Settings")
    quit_btn = Button(220, 460, 200, 50, "Quit")

    while True:
        screen.fill((18, 18, 28))
        draw_center("TSIS4 Snake", 120, font=TITLE_FONT)

        play_btn.draw(screen)
        lb_btn.draw(screen)
        settings_btn.draw(screen)
        quit_btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.is_clicked(event.pos):
                    return "play"
                if lb_btn.is_clicked(event.pos):
                    return "leaderboard"
                if settings_btn.is_clicked(event.pos):
                    return "settings"
                if quit_btn.is_clicked(event.pos):
                    return "quit"

        pygame.display.flip()
        clock.tick(60)


def play_game(username):
    game = SnakeGame(username)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.set_direction("UP")
                elif event.key == pygame.K_DOWN:
                    game.snake.set_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    game.snake.set_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    game.snake.set_direction("RIGHT")
                elif event.key == pygame.K_q:
                    return "quit", None

            if event.type == game.move_event:
                game.handle_move()

        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

        if game.game_over:
            save_game_result(username, game.score, game.level)
            best = max(game.personal_best, game.score)
            return "game_over", (game.score, game.level, best)


def main():
    settings = load_settings()
    state = "menu"
    last_username = None

    while True:
        if state == "menu":
            state = main_menu()

        elif state == "leaderboard":
            state = leaderboard_screen()

        elif state == "settings":
            state = settings_screen(settings)

        elif state == "play":
            username = username_input_screen()
            if username is None:
                state = "menu"
                continue

            last_username = username
            next_state, result = play_game(username)

            if next_state == "quit":
                break

            score, level, best = result
            state = game_over_screen(score, level, best)

        elif state == "retry":
            if last_username is None:
                state = "menu"
                continue

            next_state, result = play_game(last_username)

            if next_state == "quit":
                break

            score, level, best = result
            state = game_over_screen(score, level, best)

        elif state == "quit":
            break

    pygame.quit()


if __name__ == "__main__":
    main()