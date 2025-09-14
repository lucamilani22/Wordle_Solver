# Wordle_Solver 
A Python implementation of a **Wordle solver**. The project simulates the Wordle game and focuses on building a smart guesser that can efficiently identify the hidden 5-letter word.  

## Features  
- Implements the Wordle game logic (`wordle.py`).  
- Runs multiple games and tracks performance stats (`game.py`).  
- Customizable guessing strategy in `guesser.py` (main solution).  
- Uses provided training and development wordlists.  

## Project Structure  

The repository consists of the following key files:  

- **`game.py`**  
  Coordinates multiple games of Wordle and handles scoring. This script can be used to run multiple rounds of the game automatically for testing and evaluation.  

- **`wordle.py`**  
  Implements the core Wordle game mechanics: selecting a target word, processing guesses, and providing feedback on each attempt.  

- **`guesser.py`**  
  Contains the guessing algorithm — the heart of the solver. This is where the strategy for selecting guesses is implemented, using feedback from previous attempts.  

- **`mymethods.py`**  
  Includes helper methods used by `guesser.py` to refine the guessing process and improve accuracy.  

- **`wordlist.yaml` / `dev_wordlist.yaml` / `sample_words.yaml`**  
  Word lists that define the set of valid 5-letter words for guesses and solutions. These files are used by the game to generate challenges and evaluate guesses.  

## Usage  

Run multiple games with:  

`python game.py --r 10`

## Credits 
Assignment developed as part of coursework in the Natural Language Processing course at Bocconi University, academic year 2024-2025.

## Questions & Queries
If you have any questions, thoughts, or comments on this project, please contact me: luca.milani2@studbocconi.it
