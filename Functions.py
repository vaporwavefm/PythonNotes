# George Juarez

def main():
    kiloConverter()
    autoCosts()
    stadiumSeating()

# converts kilometers to miles

def kiloConverter():
    inp = float(input("Please enter your kilometer input: "))
    inp = inp * 0.6214
    print("Your distance in miles is: ", format(inp, ".4f"), " miles.")

# ask user for monthly automobile costs, like insurance and loan payment
# generate total monthly and yearly costs from inputs

def autoCosts():
    loans = float(input("Enter your monthly loan payment: "))
    insurance = float(input("Enter your monthly insurance payment: "))
    gas = float(input("Enter your monthly gas payment: "))
    oil = float(input("Enter your monthly oil payment: "))
    tires = float(input("Enter your monthly tires payment: "))
    maintenance = float(input("Enter your additional maintenance payment: "))
    total = loans + insurance + gas + oil + tires + maintenance
    print("Your total monthly costs amount to: $", format(total, ".2f"), ".")
    print("Your total yearly costs amount to: $", format(total * 12, ".2f"), ".")

# Stadium Seating: ask user for amount of seats sold from Class A, B, and C
# generate total from individual costs of each class

def stadiumSeating():
    classA = int(input("Enter the amount of tickets sold for Class A: "))
    classB = int(input("Enter the amount of tickets sold for Class B: "))
    classC = int(input("Enter the amount of tickets sold for Class C: "))
    print("You generated $",(classA * 15) + (classB * 12) + (classC * 9), ".00 from these 3 classes.")

# call main function

main()
