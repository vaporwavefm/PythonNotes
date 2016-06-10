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
        print("The name of your pet is", self.__name, ", their animal type is", self.__animal_type, "and their age is", self.__age, ".")

def main():
    inpName = input("Enter the name of the new pet: ")
    inpAnType = input("Enter the type of animal this pet is: ")
    inpAge = int(input("Enter the age of this pet: "))
    newPet = Pet(inpName,inpAnType,inpAge)
    newPet.printAll()

# call main

main()
