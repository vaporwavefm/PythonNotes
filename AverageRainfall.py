# George Juarez

'''
    Average Rainfall
         Write a program that uses nested loops to collect data and calculate the average rainfall
         over a period of years. The program should first ask for the number of years. The
         outer loop will iterate once for each year. The inner loop will iterate twelve times, once
         for each month. Each iteration of the inner loop will ask the user for the inches of rainfall
         for that month. After all iterations, the program should display the number of
         months, the total inches of rainfall, and the average rainfall per month for the entire period.
'''

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
monthlyRainfallDatabase = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

def main():
    # prompt user to enter the amount of years for timespan
    years = int(input("Enter the number of years you wish to process: "))
    totalRainfall = 0.0
    # nested for loop to process the months in each year
    for i in range(0, years):
        for j in range(0,12):
            # prompt user for rainfall for specific month in specific year
            print("\nFor ", months[j], " of Year ", i + 1, ",", sep = "", end = "" )
            monthlyRainfall = float(input(" enter the amount of rainfall (in inches): "))
            # add each of the elements in monthlyRainfallDatabase according to the current month
            monthlyRainfallDatabase[j] = monthlyRainfallDatabase[j] + monthlyRainfall
            # add to the totalRainfall
            totalRainfall = totalRainfall + monthlyRainfall
    # print out results, including total months, total rainfall, and average rainfall for each month
    print("\nThe total amount of months in your timespan is ", years * 12, " months.", sep = "")
    print("\nThe total amount of inches of rainfall in your timespan is ", totalRainfall, " inches.", sep = "")
    for i in range(0,12):
        print("\nThe average amount of rainfall for ", months[i], " is ", monthlyRainfallDatabase[i] / years, " inches.", sep = "")
main()
