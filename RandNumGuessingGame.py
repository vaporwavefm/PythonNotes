# George Juarez

'''
    Random Number Guessing Game
     Write a program that generates a random number in the range of 1 through 100 and asks the
     user to guess what the number is. If the user’s guess is higher than the random number, the program
     should display “Too high, try again.” If the user’s guess is lower than the random number,
     the program should display “Too low, try again.” If the user guesses the number, the application
     should congratulate the user and then generate a new random number so the game can start over.
         Optional Enhancement: Enhance the game so it keeps count of the number of guesses that the
         user makes. When the user correctly guesses the random number, the program should display
         the number of guesses.
'''

import random

def main():
    continue_game = 'y'
    globlNumGuess = 0
    print("Hello, this is a little number guessing game.")
    print("I have thought of a number between 1 and 100.")
    print("If you can guess my number correctly, you win.")
    print("I will tell you if you are too high or too low.")
    print("At the end, I will tell you the number of guesses you made from each game.")
    while continue_game == 'y':
        totalGuesses = 0
        seedNum = random.randint(1,100)
        guess = int(input("Enter your guess as to what my mystery number might be: "))
        while guess != seedNum :
            if(guess > seedNum):
                print("Your guess is too high!")
                guess = int(input("Enter a new guess: "))
                totalGuesses = totalGuesses + 1
                globlNumGuess = globlNumGuess + 1
            elif(guess < seedNum):
                print("Your guess is too low!")
                guess = int(input("Enter a new guess: "))
                totalGuesses = totalGuesses + 1
                globlNumGuess = globlNumGuess + 1
        print("You did it! Congradulations! Your total number of guesses was", totalGuesses, "guess(es).")
        continue_game = input("Would you like to play again? [y]")
    print("Thanks for playing this little game.")
    print("Your total number of guesses from all the games you played was", globlNumGuess, "guess(es).")
    
main()
    
