# George Juarez

'''
    10. Golf Scores
         The Springfork Amateur Golf Club has a tournament every weekend. The club president
         has asked you to write two programs:
              1. A program that will read each player’s name and golf score as keyboard input, and then
                 save these as records in a file named golf.txt. (Each record will have a field for the
                 player’s name and a field for the player’s score.)
              2. A program that reads the records from the golf.txt file and displays them.
'''

def main():
    move_on = 'y'
    golfScoreFile = open('golfRecords.txt','a')
    while move_on == 'y' or move_on == 'Y':
        pName = input("Enter the player's name: ")
        pScore = int(input("Enter the player's score: "))
        golfScoreFile.write(pName + "\n")
        golfScoreFile.write(str(pScore) + "\n")
        move_on = input("Would you like to continue? [y]: ")
    displayRecords = input("Would you like to display all the records from golfRecords.txt? [y]: ")
    golfScoreFile.close()
    if(displayRecords == 'y' or displayRecords == 'Y'):
        displayRecs()

def displayRecs():
    golfScoreFile = open('golfRecords.txt','r')
    lineCount = 1
    for line in golfScoreFile:
        golfRecLine = lineCount % 2
        if(golfRecLine == 0):
            print("The score of this person is: ",line)
        if(golfRecLine == 1):
            print("The name of this person is: ",line)
        lineCount = lineCount + 1
    golfScoreFile.close()
    
# call main

main()
