# George Juarez

def main():
    romanNumeralConverter()
    massWeight()
    softwareSales()
    timeCalculator()
    bugCollector()
    caloriesBurned()
    topDownStarFormation()
    
# ask user for valid input (1-10) and then convert to roman numerals

def romanNumeralConverter():
    inp = int(input("Enter your number (1-10): "))
    if(inp < 1 or inp > 10):
        print("\nNot a valid number. Restart and try again.")
    else:
        if(inp == 1):
            print("\nI")
        elif(inp == 2):
            print("\nII")
        elif(inp == 3):
            print("\nIII")
        elif(inp == 4):
            print("\nIV")
        elif(inp == 5):
            print("\nV")
        elif(inp == 6):
            print("\nVI")
        elif(inp == 7):
            print("\nVII")
        elif(inp == 8):
            print("\nVIII")
        elif(inp == 9):
            print("\nIX")
        else:
            print("\nX")

# Mass and Weight: generate weight from user's input (in mass)
# if more than 1000 newtons, too heavy, if less than 10, too light

def massWeight():
    num = float(input("Enter the object's mass to check and see if it's too heavy or too light: "))
    num = num * 9.8
    if(num > 1000):
        print("\nThis object is too heavy!")
    elif(num < 10):
        print("\nThis object is too light!")
    else:
        print("\nWe're all good here!")

# Software Sales: as user for number of packages purchased and provide proper discount
# 10-19 would be 20%, 20-49 would be 30%, 50-99 would be 40%, 99+ would be 50%...and display total afterwards
# each package sells for $99

def softwareSales():
    quant = int(input("Enter the number of packages you are purchasing: "))
    discount = 0.0
    if(quant > 10 and quant < 19):
        discount = 0.2
    elif(quant > 20 and quant < 49):
        discount = 0.3
    elif(quant > 50 and quant < 99):
        discount = 0.4
    elif(quant >= 99):
        discount = 0.5
    print("\nYour discount today will be ", discount * 100, "%.")
    print("\nYou total today will be $", format((99 * quant) * discount, ".2f"), ".")

# Time Calculator: prompt user for number of seconds...if greater than 60,
# display number of minutes, if greater than 3600, display number of hours
# if greater than 86400, display number of days

def timeCalculator():
    seconds = float(input("Enter the number of seconds to be converted: "))
    if(seconds >= 60):
        seconds = seconds / 60
        print("\nThere are at least ", format(seconds, ".1f"), " minutes from this input.")
    elif(seconds >= 3600):
        seconds = seconds / 3600
        print("\nThere are at least ", format(seconds,".1f"), " hours from this input.")
    elif(seconds >= 86400):
        print("\nThere are at least ", format(seconds, ".1f"), " days from this input.")

#-----------end if chapter, begin loop chapter--------------------

'''
    Example while statement:

    # calculate a series of commissions
    
    keep_going = 'y'
    while keep_going == 'y':
    
        # get a salesperson's sales and comission rates
        
        sales = float(input("Enter the amount of sales: "))
        comm_rate = float(input(Enter the commission rate: "))

        #calculate and display commission

        commission = sale * comm_rate
        print("The commission is $", format(commission, ".2f"), sep = '')
        keep_going = input("Do you want to calculate another " + \
                            " commission? (Enter y for yes): ")

    # end while loop
'''

# Bug Collector: prompt user for number of bugs caught for each day for 7 days
# calculate total

def bugCollector():
    total = 0
    for i in range(1,8):
        print("\nFor day ", i, ", ", sep = "")
        temp = int(input("Enter the number of bugs caught: "))
        total = total + temp
    print("The total number of bugs caught for all 7 days is: ", total, " bug(s).", sep = "")

# Calories Burned: display how much calories burned after 10,15,20,25,30 min
# particular treadmill burns 3.9 a minute

def caloriesBurned():
    for i in [10,15,20,25,30]:
        print("\nThe number of calories burned after ", i, " minutes is ", i * 3.9, " calories.")

# TopDown Star Formation: use nested loops to draw 7 stars on the top,
# followed by 6 stars on the next line, then 5 stars...

def topDownStarFormation():
    for i in range(8,1,-1):
        for j in range(1,i):
            print("*", end = " ")
        print("\n")
        
# call main function

main()
