# 🎯 Wordle CLI

A **terminal-based Wordle clone** built in Python. Guess the hidden 5-letter word in 6 tries — with color-coded feedback and a keyboard tracker.

## Repository

📁 [https://github.com/ShaswatRatna/wordle-cli](https://github.com/ShaswatRatna/wordle-cli)

## Features

- 🟩 Color-coded feedback — Green, Yellow, Gray tiles in the terminal
- ⌨️ On-screen keyboard showing used letters
- 📊 Tracks your win/loss stats across sessions
- 🔁 Play again without restarting
- 🎲 Random word picked from 800+ curated words
- 💡 Smart duplicate-letter handling (just like the real Wordle)

## How to Play

| Tile | Meaning |
|------|---------|
| 🟩 Green | Right letter, right position |
| 🟨 Yellow | Right letter, wrong position |
| ⬜ Gray | Letter not in the word |

Guess the word in **6 tries** or fewer!

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/ShaswatRatna/wordle-cli.git
cd wordle-cli
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Play!
```bash
python wordle.py
```

## Example

```
  🎯 WORDLE CLI

  Attempt 1/6
  Your guess: crane

   C   R   A   N   E
  🟨  ⬜  🟩  ⬜  ⬜

  Attempt 2/6
  Your guess: magic

   M   A   G   I   C
  ⬜  🟩  ⬜  ⬜  🟩

  ...

  ✨ Impressive! You got it in 4!
```

## What You'll Learn

- String manipulation and list operations
- Terminal colors using `colorama`
- Game loop design and state management
- Reading/writing files for persistent stats
- Handling edge cases (duplicate letters)

## Tech Stack

- Python 3.10+
- `colorama` — cross-platform terminal colors

## License

MIT — free to use, modify, and share.
