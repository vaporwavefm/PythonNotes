# George Juarez

# Chapter 9: More About Strings

# 9.1
# You can iterate a string with a for loop, using variable as each char
# in the testString...you can also index the characters (string is char array)
# IndexError exception occurs when you try to use an index that is out of range
# for a particular string
# can also use len(myString) function to find length of string
# concatentate strings with '+' operator
# Strings are immutable, so they cannot be changed once they're created

# 9.2 & 9.3
# you can slice strings (because it's a char list) using string[start : end]
# some methods: myString.isalnum() returns true if it only has alphanumeric letter or digits
# or is at least 1 character in length
# myString.isalpha() returns true if its only alphabetic letters, or len() >= 1
# myString.isdigit() for digits
# myString.islower() if all are lowercase letters
# myString.isspace() if string contains all whitespace characters

# myString.upper() if all are uppercase letters
# myString.lower() returns copy with all uppercase letters turned to lowercase
# myString.lstrip() returns copy with all leading whitespace characters removed
# myString.rstrip() for all trailing whitespace characters...could include spaces, newlines, tabs
# myString.lstrip(char) deletes all instances of that leading char removed
# myString.rstrip(char) for trailing char instances
# myString.strip() for both leading and trailing whitespace
# myString.strip(char) for all instances of char, leading and trailing
# myString.upper() turns lowercase characters to upper

# myString.endswith(substring) returns true if string ends with substring
# myString.find(substring) returns lowest index in string where substring is found, or -1 if not found
# myString.replace(old,new) returns copy of string with all instance of old string replace with new string
# myString.startswith(substrings) returns true if string begins with substring
# can also use '*' operator to make multiple copes of a string

def main():
    '''
    sumDigString()  
    datePrinter()
    '''
    alphaTelNumTranslator()
# Sum of Digits in String: ask user for numbers, and find sum of digts -> print
def sumDigString():
    userVal = int(input("Enter your number to find out the sum of its digits: "))
    total = 0
    while userVal != 0:
        total += userVal % 10
        userVal //= 10
    print("Your total is:",total,".")

# Date Printer: ask user for date (mm/dd/yyyy) and display date with month name (ex: 03/28/1995 would be March 28, 1995)
def datePrinter():
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    dateString = input("Enter your date to be converted (mm/dd/yyyy): ")
    monthString = int(dateString[0:2])
    for i in range(0,len(months)):
        if(monthString == i + 1):
            monthString = months[i]
            break
    print("Your date is: ", monthString, " ",dateString[3:5],", ",dateString[6:], sep = "")

def alphaTelNumTranslator():
    userVal = input("Enter your alphanumeric telephone number to be converted to a numeric telephone number (XXX-XXX-XXXX): ")
    partList = [ userVal[0:3],userVal[4:7],userVal[8:13] ]
    
# call main
main()
