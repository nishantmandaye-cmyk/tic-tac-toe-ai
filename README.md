# Tic-Tac-Toe AI

## Overview
This project implements an AI agent that plays the classic **Tic-Tac-Toe** game against a human player.  
The AI uses the **Minimax algorithm**, a fundamental technique in **game theory and artificial intelligence**, to choose the optimal move at every step.

The AI evaluates all possible future game states and always selects the best move, making it **unbeatable**.

You can only **draw or lose** against the AI.

---

## Features
- Human vs AI gameplay in the terminal
- AI powered by the **Minimax search algorithm**
- Perfect decision-making (unbeatable AI)
- Clear board display for gameplay
- Simple and lightweight Python implementation

---

## How the AI Works

The AI uses the **Minimax algorithm** to simulate every possible move and outcome.

### Scoring System
| Outcome | Score |
|-------|------|
| AI wins | +1 |
| Human wins | -1 |
| Draw | 0 |

### Decision Process
1. Generate all possible moves.
2. Simulate future game states.
3. Evaluate outcomes using Minimax.
4. Select the move with the best score.

This guarantees the AI always chooses the optimal strategy.