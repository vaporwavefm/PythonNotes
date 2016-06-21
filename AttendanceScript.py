# George Juarez

'''
    Attendance Script:
    
    We use a python script to take attendance. Your goal is to write a script that will
    take down a user's name and the time they entered their information and output the
    data into a CSV file. The datetime and time modules will be useful to you. Feel
    free to output the time in any time format you'd like. Feel free to input the user's name
    in any format you'd like.

    ex:
         2015-02-06 01:56:11, Nasir Memon
'''

# TODO: solve this problem lol

userFile = 'attend_script.csv'
headings = ['Name', 'Date']
from datetime import datetime
import csv

def main():
    userDict = {}
    print("Hello, welcome to this lil' sign-in sheet.")
    userName = input("Please enter your name to sign in: ")
    userDate = datetime.now().strftime('%Y-%m-%d %I:%M:%S')
    userDict[userName] = userDate
    with open(userFile, 'w', newline = '') as myCSVFile:
        csvWriter = csv.DictWriter(myCSVFile, fieldnames = headings, dialect = 'excel', quoting = csv.QUOTE_NONNUMERIC)
        csvWriter.writeheader()
        for data in userDict:
            csvWriter.writerow(data)
        
    '''
    current_time = datetime.datetime.now().time()
    print(current_time)
    '''
    
# call main

main()
