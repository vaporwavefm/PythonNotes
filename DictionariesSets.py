# George Juarez

# Chapter 10: Dictionaries and Sets

# 10.1
# Dictionary: an object that stores a collection of data (each elements has a key and a value)
# Ex: phonebook = {'Chris':'555-1111','Katie':'555-2222','Joanne':'555-3333'}
# values in a dictionary can be objects, but keys must be immutable objects (cannot be lists)
# retrieve a value from a dictionary: dictionary_name[key]...KeyError exception raised if key not found
# KeyError exception raised if you try to retreive a value from dictionary using a non-existent key
# able to use 'in' and 'not in' operators
# Dictionaries are mutable, so able to add new key-value pairs using dictionary_name[key] = value
# you cannot have duplicate keys...when you assign a value to an existing key, new value replaces existing value
# del dictionary_name[key] deletes a key-value pair
# len(dictionary_name) for number of elements in dictionary
# you can create an empty dictionary like so: dictionary_name = {} and then add elements later on
# dictionary_name.clear() clears contents of dictionary
# dictionary_name.get() gets value associated with specified key...or instead returns default value
# dictionary_name.items() returns all keys in dictionary and values as a sequence of tuples
# dictionary_name.keys() returns all keys in dictionary as a sequence of tuples
# dictionary_name.pop() returns value associated key and removed that key value from dictionary
# else, method retuns default value
# dictionary_name.popitem() return randomly selected key-value pair as a tuple and removes it from dictionary
# dictionary_name.values() returns all values in dictionary as a sequence of tuples

# 10.2
# A Set contains a collection of unique values and works like a mathematical set
# all elements in a set must be unique...sets are unordered...elements stored can be of different data types
# Ex: myset = set(['a'.'b','c']) is the same as saying myset = set('abc')
# myset = set('aaabc') will only have one 'a' appear (NO DUPLICATES)
# set() only takes in one argument, so strings must be cast into []
# len(myset) returns the number of elements in the set
# you can use myset.add() to add elements
# you can add a group of elements by using the myset.update(obj) function
# myset.remove(obj) or myset.discard(obj) removes items from the list
# remove raises a KeyError exception, but discard doesn't raise an exception
# can iterate using for loop, use 'in' and 'not in' operators
# set1.union(set2) performs a union operation on set1 and set2
# set1 | set2 performs an intersection operation on set1 and set2
# set1.difference(set2) finds elements in set1 that are not in set2
# set1 * set2 finds symmetric difference of two sets (elements found in either set1 or set2 but not both)
# set2.issubset(set1) returns True if set2 is a subset of set1
# can also use set2 <= set1 for subset, or set1 >= set2 for superset

# 10.3 : Serializing Objects
# The process of converting the object to a stream of bytes that can be saved to a file for later retreival...pickling
# Python standard library provides a module called "pickle" for serializing (pickling) objects
# You can: open a file for binary writing, call pickle module's "dump()" method to pickle object and
# write it to the specified file...after you have pickled all the objects that you want to save to the file
# close the file
# to open a file:  outputfile = open('mydata.dat','wb')
# and then use pickle.dump(object,file)...can pickle lists, tuples, dictionaries, sets, ints, floats, etc.
# and then end with outputfile.close()
# object = pickle.load(file)...object variable will reference object that was retrieved from the file and unpickled
# if you try to read past the EOF, load function will raise and EOFError exception
# 

import pickle

codes = {'A':'C','a':'c','B':'D','b':'d','C':'E','c':'e','D':'F','d':'f',
         'E':'G','e':'g','F':'H','f':'h',"\n":"\n", " ": " "}

def main():
    '''
    courseInfo()
    fileEncryptAlphaToSym()
    '''
    
# Course info: create 3 dictionaries with preset data, prompt user for course number
# and display the course room, instructor, and meeting time
def courseInfo():
    courseRoom = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
    courseInstructor = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    courseTime = {'CS101':'8:00pm','CS102':'9:00am','CS103':'10:00am','NT110':'11:00am','CM241':'1:00pm'}
    print("The courses available in this program are CS101, CS102, CS103, NT110, and CM241")
    userValue = input("Enter your course number to find out its info: ")
    for key in courseRoom:
        if(key == userValue):
            print("The course room for", key, "is", courseRoom[key])
            break
    for key in courseInstructor:
        if(key == userValue):
            print("The course instructor for",key,"is",courseInstructor[key])
            break
    for key in courseTime:
        if(key == userValue):
            print("The course meeting time for",key,"is",courseTime[key])
            break

# File Encrytion and Decryption: create two functions that will take the encryptFileEx.txt
# file and encrypt it via a dictionary you will create (NOTE: this will only work for letter A-Fa-f)
# create another function to take the result and decrypt it once again
def fileEncryptAlphaToSym():
    userFile = open('encryptFileEx.txt','r')
    userDest = open('encryptFileDest.txt','w')
    lineArr = []
    finalStr = ""
    for line in userFile:
        lineArr.append(str(line))
    for i in range(0, len(lineArr)):
        indivLineArr = []
        for j in range(0, len(lineArr[i])):
            indivLineArr += str(lineArr[i][j])
        for i in range(0, len(indivLineArr)):
            for key in codes:
                if(key == indivLineArr[i]):
                    finalStr += str(codes[key])
    userDest.write(finalStr)
    print("\nFile successfully written to encryptFileDest.txt!")
    userFile.close()
    userDest.close()
    
# call main
main()

