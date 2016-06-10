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


# Pet Class: commented out to make way for Car Class

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
        print("The name of your pet is", self.get_name(), ", their animal type is", self.get_type(), "and their age is", self.get_age(), ".")


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

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if(self.__speed <= 5):
            self.__speed = 0
        else:
            self.__speed -= 5

    def printAll(self):
        print("The year model of this car is", self.get_year_model(), ", the make is", self.get_make(), "and the current speed is", self.get_speed(), "mph.")

# Question class: used for trivia game for 2 players


QuestionDic = {'Question 1': "Who was the winner of Rupaul's Drag Race Season 1?", 'Question 2': "Who was the winner of Rupaul's Drag Race Season 2?", \
                'Question 3': "Who was the winner of Rupaul's Drag Race Season 3?", 'Question 4': "What was the winner of Rupaul's Drag Race Season 4?", \
                'Question 5': "What was the winner of Rupaul's Drag Race All-Stars Season 1?"}

class Question:

    def __init__(self, question, ans1, ans2, ans3, ans4):
        self.__question = question
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans4 = ans4

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

    playOneCount = 0
    print("Hello there, we will now begin the Trivia Game. Player 1, please step up.")
    

    
# call main

main()
