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
def main():
    go_again = 'y'
    '''
    with open("emailDatabase.txt") as f:
        for line in f:
            (key,val) = line.split()
            emailDictionary[key] = val
    
    emailDictionary = pickle.load(open('emailDatabase.txt','rb'))
    '''
    print("This is the main menu for the Name and E-mail Program.")
    while go_again == 'y' or go_again == 'Y':
        menuOption = 0
        while (menuOption < 1) or (menuOption > 4):
            menuOption = int(input("1. Look up e-mail address\n" \
                  "2. Add a new name and e-mail address\n" \
                  "3. Change an existing e-mail address\n" \
                  "4. Delete an existing e-mail address\n"))
            if((menuOption < 1) or (menuOption > 4)):
                print("Not a valid input. Try again.")
        go_again = input("Would you like to perform another action? [y]: ")
        
#call main
main()
