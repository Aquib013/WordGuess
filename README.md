# Guessing Letters of a Word - Python OOP Project

## Overview
This project is a simple implementation of a word-guessing game using Object-Oriented Programming (OOP) principles in Python. The game selects a word at random from a predefined list, and the player must guess the letters of the word within a limited number of attempts. The project demonstrates the use of classes, methods, and encapsulation.

## Features
- Randomly selects a word from a predefined list.
- Allows the player to guess letters of the word.
- Keeps track of the guessed letters and remaining attempts.
- Displays the current state of the word with correct guesses and underscores for remaining letters.
- Notifies the player of win/lose status.

## Installation
1. Ensure you have Python installed on your system (Python 3.x is recommended).
2. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/yourusername/guessing-letters-game.git
   ```
3. Navigate to the project directory:
   ```sh
   cd guessing-letters-game
   ```

## Usage
1. Run the game script:
   ```sh
   python main.py
   ```
2. Follow the on-screen instructions to play the game.

## Project Structure
```
guessing-letters-game/
│
├── main.py            # Entry point of the game
├── README.md          # Project documentation
└── requirements.txt   # List of dependencies (if any)
```

## Code Explanation

### Word List
The game uses a predefined list of words for guessing. Here is the list:
```python
WORDS = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
]
```

### `WordGame` Class
The `WordGame` class encapsulates the game logic and state.

#### Attributes
- `word_to_guess`: The word to be guessed.
- `failed_attempts`: Counter for the number of failed attempts.
- `total_attempts`: Total attempts allowed, which is twice the length of the word.
- `word_progress`: List showing the current state of guessed letters and underscores.

#### Methods
- `__init__(self, word_to_guess)`: Initializes the game with the given word.
- `find_indexes(self, letter)`: Finds all indexes of a given letter in the word.
- `invalid_input(self, input)`: Validates the user's input.
- `print_game_status(self)`: Prints the current game status, including remaining attempts and the word progress.
- `update_progress(self, letter, indexes)`: Updates the word progress with correctly guessed letters.
- `get_user_input(self)`: Prompts the user to enter a letter.
- `play(self)`: Main game loop where the user guesses letters until they win or lose.

### Example
Here is the complete implementation:
```python
import random

WORDS = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
]

class WordGame:
    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess
        self.failed_attempts = 0
        self.total_attempts = len(self.word_to_guess) * 2
        self.word_progress = list('_' * len(self.word_to_guess))

    def find_indexes(self, letter):
        indexes = []
        for i, char in enumerate(self.word_to_guess):
            if char == letter:
                indexes.append(i)
        return indexes
    
    def invalid_input(self, input):
        return input.isdigit() or input.isalpha() and len(input) > 1
    
    def print_game_status(self):
        print(f"Remaining attempts: {self.total_attempts - self.failed_attempts}")
        print("\n")
        print(' '.join(self.word_progress))
    
    def update_progress(self, letter, indexes):
        for index in indexes:
            self.word_progress[index] = letter

    def get_user_input(self):
        user_input = input("Please enter a letter: ")
        return user_input
    
    def play(self):
        while self.failed_attempts < self.total_attempts:
            self.print_game_status()
            print("\n")
            user_input = self.get_user_input()
            if self.invalid_input(user_input):
                print("The input is not valid!")
                continue
            
            if user_input in self.word_progress:
                print("You have already guessed this letter!")
                continue

            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                if self.word_progress.count("_") == 0:
                    print("YAY!!! You Guessed the Word!")
                    print(f"The Word is {self.word_to_guess}")
                    quit()
            else:
                self.failed_attempts += 1
        print("You Lost :(")

if __name__ == "__main__":
    word_to_guess = random.choice(WORDS)
    wordgame = WordGame(word_to_guess)
    wordgame.play()
```

## Contribution
Contributions are welcome! Please create an issue or submit a pull request.

## License
This project is licensed under the MIT License.

---

Enjoy playing and learning with the Guessing Letters of a Word game!
