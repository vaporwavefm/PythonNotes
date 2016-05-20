# George Juarez

'''
    The local driver’s license office has asked you to create an application that grades the written
    portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here
    are the correct answers:
                1. B 6. A 11. B 16. C
                2. D 7. B 12. C 17. C
                3. A 8. A 13. D 18. B
                4. A 9. C 14. A 19. D
                5. C 10. D 15. D 20. A
    Your program should store these correct answers in a list. The program should read the
    student’s answers for each of the 20 questions from a text file and store the answers in
    another list. (Create your own text file to test the application.) After the student’s answers
    have been read from the file, the program should display a message indicating whether the
    student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
    to pass the exam.) It should then display the total number of correctly answered questions,
    the total number of incorrectly answered questions, and a list showing the question numbers
    of the incorrectly answered questions.
'''

correctAnsDatabase = ['B','D','A','A','C','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A']

def main():
    userFile = open(input("Enter the file you wish to grade: "),'r')
    i = 0
    totalCorrect = 0
    userList = []
    for line in userFile:
        userList.append(line.rstrip('\n'))
        i += 1
    for i in range(0,20):
        if(userList[i] == correctAnsDatabase[i]):
            totalCorrect = totalCorrect + 1
    print("You scored", totalCorrect,"out of 20.")
    if(totalCorrect >= 15):
        print("You passed!")
    else:
        print("You failed.")
    userFile.close()
    
# call main
main()
