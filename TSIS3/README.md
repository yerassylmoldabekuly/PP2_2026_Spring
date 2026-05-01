# TSIS3: Racer Game — Advanced Driving, Leaderboard & Power-Ups

This project extends the Racer game from previous practices and adds a more advanced arcade-style driving experience with obstacles, dynamic road events, power-ups, settings, and persistent leaderboard support.

## Features

### Gameplay & Track
- Lane-based road movement
- Dynamic traffic cars moving downward
- Lane hazards:
  - oil spills
  - slow-down zones
  - potholes
- Dynamic road events:
  - moving barriers
  - speed bumps
  - nitro boost strips

### Obstacles & Difficulty
- Traffic cars cause game over on collision
- Random road hazards appear during the run
- Safe spawn logic prevents traffic, coins, and power-ups from spawning directly on the player
- Difficulty scaling:
  - more traffic
  - more hazards
  - faster road speed
  - increased event frequency as distance grows

### Coins & Power-Ups
- Weighted coins with different values
- Three power-ups:
  - **Nitro**: temporary speed boost
  - **Shield**: protects from one collision
  - **Repair**: saves one crash / clears one dangerous collision
- Only one power-up can be active at a time
- Power-ups disappear if not collected
- Active power-up and timer are shown on screen

### Score & Progress
- Score is based on:
  - collected coins
  - distance traveled
  - power-up bonus
- Distance meter is displayed
- Remaining distance to finish is shown

### Persistence
- Leaderboard is saved to `leaderboard.json`
- Settings are saved to `settings.json`
- Settings are loaded at startup and applied immediately

### Game Screens
- Main Menu
- Settings screen
- Leaderboard screen
- Game Over screen
- Username input screen before starting

---

## Repository Structure

```text
TSIS3/
├── main.py
├── racer.py
├── ui.py
├── persistence.py
├── settings.json
├── leaderboard.json
└── assets/