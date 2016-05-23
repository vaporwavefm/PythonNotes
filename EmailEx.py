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

def main():
    emailDictionary = {}
    with open("emailDatabase.txt") as f:
        for line in f:
            (key,val) = line.split()
            emailDictionary[key] = val
    print(emailDictionary)
    print("The is the main menu for the Name and E-mail Program.\n"\
          "1. Look up e-mail address\n" \
          "2. Add a new name and e-mail address\n" \
          "3. Change an existing e-mail address\n" \
          "4. Delete an existing e-mail address\n")
#call main
main()
