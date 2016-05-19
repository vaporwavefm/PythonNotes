# George Juarez

# List and Tuples

# 8.2
# you can use the list() function to convert certain types of objects to lists
# ex: numsZeroThroughFour = list(range(5)) or evenNumsOneThroughTen = list(range(1,10,2))
# list * n (repetition operator) makes mult. copes of list and joins them
# can iterate a List with for loop (ex: for n in myList:)
# len(myList) returns the length of a sequence
# Lists are mutable, so elements can be changed
# you can use the + operator to concatenate two lists

# 8.3
# slice: span of items taken from a sequence...list_name[start : end]
# you can also say list_name[start : ] so Python uses lengthof list as the end
# list_name[ : ] just returns the entire list
# can also use neg. numbers to reference positions relative to end of list

# 8.4
# Use 'in' operator to determine whether an item is contained in a list
# (item in myList)...returns a boolean
# (item not in myList)...returns true if item is not in list

# 8.5
# Some useful built-in methods for Lists: myList.append(item) appends item to end of list
# myList.index(item) returns index of first element whose value is equal to item
# ValueError exception raised if item not found in List
# myList.inset(index,item) inserts items at specified index...List is then expanded
# to accommodate new item...all items after shifted to the right...if index specfified
# is beyond end of List, item added to end of List...if index specified is neg., item
# will be added to beginning of List
# myList.sort() sorts items so they appear in ascending order
# myList.remove(item) removes first occurrence of item from List
# ValueError exception raised if item is not found in the List
# myList.reverse() reverses order of items in List
# del myList[index] deletes item at specified index
# min(myList) and max(myList) returns min and max items of sequence

# 8.6
# assigning a List to another List will just make both variables reference the same List
# gotta use for loop to copy a List onto another one

# 8.7
# you can pass an entire List to a function and return it as a List
# Python has file function called writelines(myList) that writes myList to
# a the file (ex: myFile.writelines(myList) )

# 8.9
# Tuples: immutable sequence, cannot be changed
# tuples support subscript indexing, methods such as index, len, min, max
# slicing expressions, in operator, + and * operators
# a tuple with one element, create it as so: myTuple = (1,)
# Tuples are faster to process, so maybe better with lots of data (and also safe!)
# you can convert a tuple to a list by using list() and vice-versa: tuple()

import random

def main():
    '''
    totalSales()
    lotteryNumGen()
    numAnalysisProg()
    '''
    
# Total Sales: ask user to enter store's sales for each day of the week
# use loop to calculate total sales for the week and display result

def totalSales():
    salesArr = [0.00] * 7
    total = 0.00
    for i in range(0,len(salesArr)):
        print("Enter your sales for day",i+1,end ="")
        salesArr[i] = float(input(": "))
    for i in range(0,len(salesArr)):
        total += salesArr[i]
    print("Your total sales amount to $",format(total,'.2f'),".")

# Lottery Number Generator: generate 7 numbers (0-9) and place them in a List
# print out contents of that list

def lotteryNumGen():
    lottDatabase = [0] * 7
    for i in range(0,len(lottDatabase)):
        lottDatabase[i] = random.randint(0,9)
    print("The lottery number of the day is: ", end = "")
    for i in range(0,len(lottDatabase)):
        print(lottDatabase[i], end = "")

# Number Analysis Program: ask user for 20 inputs, and fill List with it
# display min, max, total and average of the created List

def numAnalysisProg():
    numList = [0] * 20
    total = 0
    for i in range(0,len(numList)):
        print("Enter your numbers...this will be input",i+1, end="")
        numList[i] = int(input(": "))
        total += numList[i]
    print("The lowest number in this List is:",min(numList))
    print("The highest number in this List is:",max(numList)) 
    print("The total of these numbers is:",total)
    print("The average of these numbers is:", format(total / 20, '.2f'))
    
# call main

main()

