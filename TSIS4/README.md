# TSIS4: Snake Game — Database Integration & Advanced Gameplay

This project extends the Snake game from previous practices and adds PostgreSQL leaderboard support, poison food, power-ups, level obstacles, settings persistence, and multiple game screens.

## Features

### Database Integration
- Username entry on the main menu
- Save result to PostgreSQL after game over
- Persistent leaderboard stored in database
- Top 10 leaderboard screen inside the game
- Personal best score shown during gameplay

### Gameplay
- Wall and border collision detection
- Random food placement
- Food with different point weights
- Food that disappears after a timer
- Poison food that shortens the snake
- Power-ups:
  - Speed boost
  - Slow motion
  - Shield
- Random obstacle blocks starting from Level 3
- Level progression
- Speed increase with level

### Settings
- Snake color
- Grid overlay on / off
- Sound on / off
- Settings saved in `settings.json`

### Screens
- Main Menu
- Leaderboard
- Settings
- Game Over

---

## Repository Structure

```text
TSIS4/
├── main.py
├── game.py
├── db.py
├── settings.json
├── config.py
└── assets/