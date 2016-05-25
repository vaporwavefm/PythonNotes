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


def main():
    go_again = 'y'   
    print("This is the main menu for the Name and E-mail Program.")
    while go_again.lower() =='y':
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
                inpName = input("Please enter the full name of the person's e-mail: ")
                lookupEmail(inpName)
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
        go_again = input("Would you like to perform another action? [y]: ")
    print("Thanks for using my wee lil' program!")
    
def lookupEmail(inpName):
    emailDictionary = pickle.load(open('emailDatabase.txt','rb'))
    for key in emailDictionary:
        if(str(inpName) == str(key)):
            print("The is the email of your requested person:", emailDictionary[key])
    
def addEmail():
    sampleD = {}
    name = input("Enter the new person's name: ")
    email = input("Enter the new person's e-mail: ")
    sampleD[name] = email
    pickle.dump(sampleD, open('emailDatabase.txt','wb'))
    print("Success!")

def changeEmail(inpName, inpEmail):
    newPair = {inpName : inpEmail}
    userFile = pickle.load(open('emailDatabase.txt','rb'))
    for key in userFile:
        if(str(key) == inpName):
            del userFile[key]
            pickle.dump(newPair,open('emailDatabase.txt','wb'))
            break
            
def deleteEmail(inpName):
    userFile = pickle.load(open('emailDatabase.txt','rb'))
    for key in userFile:
        if(str(key) == inpName):
            del userFile[key]
            break

def printAll():
    userFile = pickle.load(open('emailDatabase.txt','rb'))
    for key in userFile:
        print(key, userFile[key])
        
#call main
main()
