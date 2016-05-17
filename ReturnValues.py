# George Juarez

import random
import math

def main():
    #----------------- begin misc notes about Return Values-------------
    print("The dice landed on", random.randint(1,6))
    print("\nThe tens dice landed on", random.randrange(0,100,10))
    print("\nA random floating point number is", random.uniform(0.0,1.0))
    
    # random.seed(int) sets the integer starting value used in generating random number
    # you can call this function before calling any other random module function
    # always give the same random number sequence if used

    # square root stuff
    squaredNum = float(input("Enter a number: "))
    print("\nThe square root of", squaredNum, "is", math.sqrt(squaredNum), ".")

    # math.hypotenuse(int,int) returns the length of a right triangle's hypotenuse
    # other functions like sin(int), cos(int), exp(x), ceil(x)....
    # math module also defines pi and e

    #---------------------end misc notes------------------------------
    print("\n")
    
    print(feetToInches(3))

    print("\n \n \n ")

    mathQuiz()

    # below calls are part of the calc_average and determine_grade problem

    rawScores = [0,0,0,0,0]
    for i in range(0,5):
        rawScores[i] = int(input("Enter a score: "))
    calc_average(rawScores[0],rawScores[1],rawScores[2],rawScores[3],rawScores[4])
    for i in range(0,5):
        determine_grade(rawScores[i],i)

    testNum = int(input("Enter a number to determine if it's prime or not: "))
    if(isPrime(testNum) == True):
        print("\nThis number is prime.")
    elif(isPrime(testNum) == False):
        print("\nTHis number is not prime.")
    
# Feet To Inches: self-explanatory

def feetToInches(feet):
    return feet * 12

# Math Quiz: generate two random numbers to be added by the user
# if user answers correctly, yay ; if not, display correct answer

def mathQuiz():
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print(" ",num1, "\n+",num2, "=\n")
    guess = int(input("Your answer: "))
    if(guess == (num1 + num2)):
        print("\nCorrect! Good for you!")
    else:
        print("\nI'm sorry, that is not correct. The correct answer is", num1 + num2)

# Test Average and Grade: ask user for 5 test scores, then calculate test
# average and determine the grade for each test (90-100 = A, 80-89 = B,
# 70-79 = C, 60-69 = D, Below 60 = F) (Note: this includes calc_average and determine_grade

def calc_average(un,deux,trois,quatre,cinq):
    total = un + deux + trois + quatre + cinq
    print("\nThe average test score is", total / 5)

def determine_grade(score,place):
    if(score >= 90 and score <= 100):
        print("\nYou get an A for test",place, ".")
    elif(score >= 80 and score <= 89):
        print("\nYou get a B for test",place,".")
    elif(score >= 70 and score <= 79):
        print("\nYou get a C for test",place,".")
    elif(score >= 60 and score <= 69):
        print("\nYou get a D for test",place,".")
    elif(score <= 60):
        print("\nYou get a F for test",place,".")

# isPrime(), self explanatory
# algorithm is pretty universal, i guess

def isPrime(testNum):
    if(testNum <= 1):
        return False
    elif(testNum <= 3):
        return True
    elif( (testNum % 2) == 0 or (testNum % 3) == 0):
        return False
    i = 5
    w = 2
    while i * i <= testNum:
        if( (testNum % i) == 0 or (testNum % (i + 2)) == 0):
            return False
        i = i + w
        w = 6 - w
    return True
          
# call main()

main()
