# George Juarez

'''
    8. Name and Email Addresses
    Write a program that keeps names and email addresses in a dictionary as key-value pairs.
    The program should display a menu that lets the user look up a person’s email address, add
    a new name and email address, change an existing email address, and delete an existing
    name and email address. The program should pickle the dictionary and save it to a file
    when the user exits the program. Each time the program starts, it should retrieve the dictionary
    from the file and unpickle it.
'''

import pickle

'''
emailDictionary = {'Jorge Juarez':'jjuarez@albany.edu','Theo Vasilakos':'overlordtheo@gmail.com'}
pickle.dump(emailDictionary,open('emailDatabase.txt','wb'))
'''

userFile = 'emailDatabase.txt'

def main():
    go_again = 'y'   
    print("This is the main menu for the Name and E-mail Program.")
    while go_again.lower() == 'y':
        menuOption = 0
        while (menuOption < 1) or (menuOption > 4):
            menuOption = int(input("1. Look up e-mail address\n" \
                  "2. Add a new name and e-mail address\n" \
                  "3. Change an existing e-mail address\n" \
                  "4. Delete an existing e-mail address\n" \
                  "5. Display all e-mails\n"))
            if((menuOption < 1) or (menuOption > 5)):
                print("Not a valid input. Try again.")
            elif(menuOption == 1):
                lookupEmail()
            elif(menuOption == 2):
                addEmail()
            elif(menuOption == 3):
                inpName = input("Please enter the full name of the person's email: ")
                inpEmail = input("Now, please enter the new e-mail of that person: ")
                changeEmail(inpName, inpEmail)
            elif(menuOption == 4):
                inpName = input("Enter the full name of the person's email to be deleted: ")
                deleteEmail(inpName)
            elif(menuOption == 5):
                printAll()
            
        go_again = input("Would you like to perform another action? [y/n]: ")
    print("Thanks for using my wee lil' program!")
    
def lookupEmail():
    foundFlag = False
    with open(userFile,'rb') as handle:
        currEl = pickle.load(handle)
        print(currEl)
    '''
    if(foundFlag == False):
        print("User not found.")
    '''    
def addEmail():
    sampleD = {}
    name = input("Enter the new person's name: ")
    email = input("Enter the new person's e-mail: ")
    sampleD[name] = email
    with open(userFile,'ab') as handle:
        pickle.dump(sampleD,handle)

def changeEmail(inpName, inpEmail):
    newPair = {inpName : inpEmail}
    userFile = pickle.load(open('emailDatabase.txt','rb'))
    for key in userFile:
        if(str(key) == inpName):
            del userFile[key]
            pickle.dump(newPair,open('emailDatabase.txt','ab'))
            break
'''           
def deleteEmail(inpName):
    userFile = pickle.load(open('emailDatabase.txt','rb'))
    for key in userFile:
        if(str(key) == inpName):
            del userFile[key]
            break
'''

def printAll():
    endOfFile = False
    inpFile = open(userFile,'rb')
    while not endOfFile:
        try:
            nextEl = pickle.load(inpFile)
            print(nextEl)
        except EOFError:
            endOfFile = True
    inpFile.close()

       
#call main
main()
