import random

WORDS = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
]


class WordGame:

    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess
        self.failed_attempts = 0
        self.total_attempts = len(self.word_to_guess)*2
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
        print(f"remaining attempts : {self.total_attempts - self.failed_attempts}")
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
                print("The input is not valid! ")
                continue
            
            if user_input in self.word_progress:
                print("You have already guessed this letter! ")
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

                



word_to_guess = random.choice(WORDS)
wordgame = WordGame(word_to_guess)
wordgame.play()
