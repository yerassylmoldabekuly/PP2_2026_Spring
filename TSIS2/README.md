# TSIS2: Paint Application — Extended Drawing Tools

This project extends the Paint application from previous practices and adds more complete drawing functionality using only Pygame built-in tools.

## Features

### Drawing Tools
- Pencil tool for freehand drawing
- Straight line tool with live preview
- Rectangle
- Circle
- Square
- Right triangle
- Equilateral triangle
- Rhombus
- Eraser
- Flood fill
- Text tool

### Brush Sizes
Three stroke thickness levels:
- Small: 2 px
- Medium: 5 px
- Large: 10 px

Brush size applies to:
- Pencil
- Line
- Rectangle
- Circle
- Square
- Right triangle
- Equilateral triangle
- Rhombus
- Eraser

### Fill Tool
- Click inside a closed region to fill it
- Implemented using:
  - `pygame.Surface.get_at()`
  - `pygame.Surface.set_at()`

### Save Canvas
- Press `Ctrl+S` to save the canvas as a `.png` file
- File name includes a timestamp so files do not overwrite each other

### Text Tool
- Click on the canvas to place a text cursor
- Type characters in real time
- Press `Enter` to confirm
- Press `Escape` to cancel

---

## Repository Structure

```text
TSIS2/
├── paint.py
├── tools.py
└── assets/