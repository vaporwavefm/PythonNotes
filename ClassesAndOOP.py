# George Juarez

# Chapter 11: Classes and Object-Oriented Programming

# 11.1
# Objects are software entities that contains both data and procedures: has attributes
# Encapsulatin: combining of data and code into a single object
# Data Hiding: object's ability to hide its data attributes from code that is outside the object
# Public vs. Private methods

# 11.2
# class: code that specifies data attributes and methods of a particular type of object
# Each object that is created from a class is an instance of the class
# class defintion: set of statements that define a class's methods and data attributes
# Most Python classes have a special method called __init__ (initializer method)


# Pet Class: has initializer, with gets, sets, and printall

class Pet:

    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self,name):
        self.__name = name
    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type

    def get_name(self):
        return self.__name
    def get_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
 
    def printAll(self):
        print("The name of your pet is", self.get_name(), ", their animal type is", \
              self.get_type(), "and their age is", self.get_age(), ".")


# Car Class: gets and sets, also a brake and accelerate methods

class Car:

    def __init__(self,year_model,make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def get_year_model(self):
        return self.__year_model
    def get_make(self):
        return self.__make
    def get_speed(self):
        return self.__speed

    def set_year_model(self,year_model):
        self.__year_model = year_model
    def set_make(self,make):
        self.__make = make

    # accelerate method increases speed by 5 every time it is called
    def accelerate(self):
        self.__speed += 5

    # brake method decreases speed by 5 every time it is called, or otherwise hits 0
    def brake(self):
        if(self.__speed <= 5):
            self.__speed = 0
        else:
            self.__speed -= 5

    def printAll(self):
        print("The year model of this car is", self.get_year_model(), ", the make is", \
              self.get_make(), "and the current speed is", self.get_speed(), "mph.")

# Question class: used for trivia game for 2 players

class Question:

    def __init__(self, question, ans1, ans2, ans3, ans4, corr):
        self.__question = question
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans4 = ans4
        self.__corr = corr
        
    def get_question(self):
        return self.__question
    def get_ans1(self):
        return self.__ans1
    def get_ans2(self):
        return self.__ans2
    def get_ans3(self):
        return self.__ans3
    def get_ans4(self):
        return self.__ans4
    def get_corr(self):
        return self.__corr

    def set_question(self,question):
        self.__question = question
    def set_ans1(self,ans1):
        self.__ans1 = ans1
    def set_ans2(self,ans2):
        self.__ans1 = ans2
    def set_ans3(self,ans3):
        self.__ans1 = ans3
    def set_ans4(self,ans4):
        self.__ans1 = ans4
    def set_corr(self,corr):
        self.__corr = corr


questionDict = { "Which number is odd?" : Question("Which number is odd?","2","4","31","2008",'C'), \
                 "What color comes after red in the rainbow?" : Question("What color comes after red in the rainbow?", \
                                                                         "blue","green","yellow","orange",'D'), \
                 "Which number is prime?" : Question("Which number is prime?","20","19","22","2000010",'B'), \
                 "Who was the first President of the US?" : Question("Who was the first President of the US?", "George Washington", \
                                                                    "Alexander Hamilton","Ghandi","Smitty Werbenjagermanjensen",'A'), \
                 "Who won Season 8 of Rupaul's Drag Race?": Question("Who won Season 8 of Rupaul's Drag Race?", "Kim Chi", "Naomi Smalls", \
                                                                     "Bob the Drag Queen", "Chi Chi Kat Devayne", 'C'), \
                 "Choose the correct response.": Question("Choose the correct response.", "Pick me! I'm correct!", "I'm the wrong answer.", \
                                                          "I also am the wrong answer.", "Don't even pick me, I'm wrong too (sighs)", 'A') \
                 }
triviaAdPass = "cookiecutter"
    
def main():
    # these statements deal with the Pet Class created above
    '''
    inpName = input("Enter the name of the new pet: ")
    inpAnType = input("Enter the type of animal this pet is: ")
    inpAge = int(input("Enter the age of this pet: "))
    newPet = Pet(inpName,inpAnType,inpAge)
    newPet.printAll()
    '''

    # the following statements are for the Car Class created above as well
    '''
    inpYrMdl = input("Enter the year model for this car: ")
    inpMake = input("Enter the make for this car: ")
    newCar = Car(inpYrMdl,inpMake)
    newCar.printAll()
    print("Now adjusting speed...")
    for i in range(0,5):
        newCar.accelerate()
        print(newCar.get_speed())
    print("Slowing down now...")
    for i in range(0,3):
        newCar.brake()
        print(newCar.get_speed())
    '''

    # Trivia Game:

    go_again = 'y'
    userChoice = 0
    print("Hello there. This is the menu for the Trivia Game Program. \nPlease select an option. ")
    while go_again.lower() == 'y':
        userChoice = int(input("[1] Play the game. \n" \
              "[2] ADMIN MODE: Add a question. \n" \
              "[3] ADMIN MODE: Delete a question. \n" \
              "[4] ADMIN MODE: Print all questions. \n" \
              "Enter your input: "))
        if(userChoice == 1):
            theActualGame()
        elif(userChoice == 2):
            userPass = input("Enter the password: ")
            if(valPass(userPass) == True):
                addQuestion()
            else:
                print("Access denied.")
        elif(userChoice == 3):
            userPass = input("Enter the password: ")
            if(valPass(userPass) == True):
                delQuestion()
            else:
                print("Access denied.")
        elif(userChoice == 4):
            userPass = input("Enter the password: ")
            if(valPass(userPass) == True):
                printAllQuestions()
            else:
                print("Access denied.")
        go_again = input("Would you like to perform another action? [y/n]: ")
    print("Thank you, come again!")

def theActualGame():
    maxLimit = 5
    userCorr = 0
    for key in questionDict:
        print(key, "\nA.", questionDict[key].get_ans1(), "\nB.", questionDict[key].get_ans2(), "\nC.", questionDict[key].get_ans3(), \
              "\nD.", questionDict[key].get_ans4())
        userAns = input("Enter your choice: ")
        if(userAns.upper() == questionDict[key].get_corr()):
            print("Correct! One point for you!")
            userCorr += 1
        else:
            print("I'm sorry, that is not correct. The correct answer is", questionDict[key].get_corr())
        maxLimit -= 1
        if(maxLimit <= 0):
            break
    print("You have received", userCorr, "points, so that means you get a", 20 * userCorr, "% for this game. Congrats!")
    
def valPass(userPass):
    return triviaAdPass == userPass
    
def addQuestion():
    userQuest = input("Enter the question you wish to add: ")
    userAns1 = input("Now, enter the first choice: ")
    userAns2 = input("Now, enter the second choice: ")
    userAns3 = input("Now, enter the third choice: ")
    userAns4 = input("Now, enter the fourth choice: ")
    corrAns = input("Enter the correct choice [Input: A/B/C/D] : ")
    userObject = Question(userQuest,userAns1,userAns2,userAns3,userAns4,corrAns.upper())
    questionDict[userObject.get_question()] = userObject

def delQuestion():
    userQuest = input("Enter the question you wish to delete: ")
    foundFlag = False
    for key in questionDict:
        if(userQuest == questionDict[key].get_question()):
            del(questionDict[key])
            foundFlag = True
            break
    if(foundFlag == False):
        print("Not found.")
    
def printAllQuestions():
    for key in questionDict:
        print(key, "\nA.", questionDict[key].get_ans1(), "\nB.", questionDict[key].get_ans2(), \
              "\nC.", questionDict[key].get_ans3(), "\nD.", questionDict[key].get_ans4(), \
              "\nThe correct answer for this question is Choice", questionDict[key].get_corr(), ".")

    
# call main

main()
