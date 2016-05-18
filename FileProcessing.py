# George Juarez

    # 7.1
    # file_variable = open(filename, mode)
    # mode is a string specifying the mode ('r','w', or 'a')
    # where 'a' (append) is open a file to be written to, all data written will
    # be appended to its end, as opposed to 'w', where all data on the
    # existing file will be erased before writing to it

    # Python assumes the files is in same location as the program
    # but you can specify the path as well as a filename in argument
    # Ex: test_file = open(r'C:\Users\Blake\temp\test.txt','w')
    # remember to prefix the string with the letter 'r'

    # file_variable.write(string) writes data to a file
    # file_variable.close() closes file

    # to read file contents, set a variable to file_variable.read()
    # to read one line from a file, set a variable to file_variable.readline()

    # to read a string and strip \n from it, set variable to var.rstrip('\n')
    # this returns a copy of the var string without the trailing \n

    # to append data to an existing file, just open file using 'a' and use the .write(string)function

    # to rw numeric data, use the str(number) function to convert it to a string

    # 7.2
    # To detect the EOF, use this algorithm: open file...use readline to read
    # first line from file...while value returned from readline is not an empty string:
    # process item that was just read from file...use readline to read next line from file
    # (end while)...close file

    # Python's for loops automatically reads line in a file without testing for
    # any special condition that signals end of file...doesn't require a priming
    # read option, and stops when EOF reached..loop will iterate for each line in file

    # 7.3
    # "import os" needed if you want to remove and rename functions
    # also to remove .txt files...ex: os.remove('your_file.txt')
    # to rename .txt files...ex: os.rename('old_file.txt','new_file.txt')

    # 7.4
    # Exception Handler: written with a try/except statement
    # try suite is 1+ statements that can potentially raise an exception
    # except clause has a block of statements called the handler
    # if statement in try suite raises an exception specified by the ExceptionName
    # in except clase, handler executes, then program resumes execution with statement
    # following the try/except statement...if not specified, program will halt with a
    # trackback error message...if statements in try suite execute w/o raising an
    # exeption, then any except clasues and handlers are skipped, resume program
    # an example of an exception could be a ValueError (user input different type than specified)
    # IOError exception: error in trying to read file
    # "except ValueError as err: " is a way of displaying an exception default error message
    # try/except/else...where else suite execute after statements in try suite, only if no
    # exceptions were raise
    # try/except/finally...where finally always executed after any exception
    # handlers have executed (perform cleanup operation, such as closing files, resources...)
    
def main():
    readNums()
    fileHeadDisplay()
    lineNumbers()
    
# File Diplay: read and print all numbers from numbers.txt

def readNums():
    currNumFile = open('numbers.txt','r')
    for line in currNumFile:
        print(line)
    currNumFile.close()   

# ask user for name of .txt file, print out the first 5 lines of the text
# if less than 5 lines, print out all of the lines

def fileHeadDisplay():
    userFile = open(input("Enter the name of the file you would like to view (first 5 lines): "),'r')
    fiveFlag = 5
    for line in userFile:
        print(line)
        fiveFlag = fiveFlag - 1
        if(fiveFlag <= 0):
            break
    userFile.close()      

# ask user for name of .txt file, print out contents with line numbers

def lineNumbers():
    userFile = open(input("Enter the name of the file you would like to view: "),'r')
    i = 0
    for line in userFile:
        print("Line",i, ": ", line)
        i = i + 1
    userFile.close()
    
# call main function

main()
