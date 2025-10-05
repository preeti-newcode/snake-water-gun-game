# Snake-Water-Gun-game

🎮 A fun and interactive Python-based command-line game inspired by the classic Snake, Water, Gun logic — similar to Rock, Paper, Scissors.
This repository includes two versions of the game:

🧍‍♂️ Single Player — play against the computer.

👥 Two Player (Luck Edition) — challenge a friend and let luck decide your fate!

*** 🧩 Game Logic

⚙️Option -> Beats	: Loses To

🐍 Snake -> Water	: Gun

💧 Water -> Gun	: Snake

🔫 Gun -> Snake : Water


⚙️ Game Versions
# 🎯 1️⃣ Single Player Mode

In this version, you compete against the computer, which makes random choices each round.

💡 Features

🧠 Single-player mode – You play against a computer opponent.

🎲 Randomized computer choices using randint() and shuffle().

📊 Score tracking – Keeps count of Wins, Losses, and Ties.

✨ Interactive CLI experience – Simple text-based interface with clear outputs.

🛑 Exit anytime – Type STOP to quit and view your final results.

🔁 Replay-ready – Keeps looping until you decide to stop.


💻 How It Works

The computer randomly assigns positions to "Snake", "Water", and "Gun".

You choose one option.

The game reveals both choices and displays the winner.

Results are updated automatically.

# 🍀 2️⃣ Two Player Mode – Luck Edition

This version adds a completely new twist — players don’t choose Snake, Water, or Gun directly! 😲

Instead, both players pick a number (0–2), and the program randomly shuffles the options before assigning them.
That means every round is based on luck, not strategy — a totally unpredictable and fun way to play!

💡 Features

🎲 Luck-based gameplay – Players pick numbers, not actual options.

👥 Two-player mode – Compete with a friend.

📊 Score tracking – Win/Loss/Tie count for both players.

🔁 Replay option – Continue playing multiple rounds.

🎯 Final result summary at the end.

⚡ 100% Python, no external libraries needed.

💻 How It Works

The list ['Snake', 'Water', 'Gun'] is shuffled each time.

Each player selects a number (0–2).

The shuffled list determines what that number corresponds to.

Results are revealed after both selections.

🌟 Why It’s Unique

Unlike traditional versions, this edition adds surprise and suspense — your number might turn into Snake now, but Water next round! 😄

It’s a rare, luck-based twist on a timeless game — something you won’t find in most Python mini-projects.

🧠 Future Scope

🔄 Add a mode selector – Classic or Luck edition.

📊 Add match history and round summary logs.

🎨 Create GUI using Tkinter or Pygame.

🌐 Experiment with online two-player mode.

🤖 Include difficulty levels or AI learning behavior.
