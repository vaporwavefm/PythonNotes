print('To be or not to be')
print('That is the question')

# George Juarez

age = 25
width = 10
length = 5
area = width * length
print(area)

print('The area is: ',area)

# remember, input(string) always returns a string
# the exponent operator is x**n where x is the base and n is the exponent

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print('Your full name is: ',first_name, last_name)

string_value = input('How many hours did you work? ')
hours = int(string_value)
max_hours = abs(40 - hours)
print('You need or exceeded ',max_hours,' hours off your work schedule.')

print('A formatted division (with 3 decimal places) of 2/3 is: ', format(2/3,'.3f'))

# Sales Prediction

projectedSales = int(input("Enter your projected amount of sales: "))
print("Your projected profit would be: $", projectedSales * .23)

# Land Calculation

landAcreDiv = int(input("Enter the toal square feet in a tract of land: "))
print("The number of acres from this input is ", format(landAcreDiv / 43560, '.3f'), " acres.")

# Tip, Tax, and Total

subtotal = float(input("Enter your subtotal for the meal: "))
tip = subtotal * .15
salesTax = subtotal * .07
print("The tip will be $", format(tip, '.2f'), " and the Sales Tax will be $", \
format(salesTax, '.2f'), ". \nThe total will be $", format(subtotal + tip + salesTax, '.2f'), ".")
