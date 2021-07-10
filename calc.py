# Function to add two numbers
def addition(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtraction(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiplication(num1, num2):
    return num1 * num2

# Function to divide two numbers
def division(num1, num2):
    return num1 / num2

select=input("Please select an operation- \n"
            "1. Add \n"
            "2. Subtract \n"
            "3. Multiply \n"
            "4. Divide \n")
number1=input("Enter the first number: \n")
number2=input("Enter the second number: \n")

if select == 1:
    print(number_1, "+", number_2, "=",
        add(number_1, number_2))
  
elif select == 2:
    print(number_1, "-", number_2, "=",
        subtract(number_1, number_2))
  
elif select == 3:
    print(number_1, "*", number_2, "=",
        multiply(number_1, number_2))
  
elif select == 4:
    print(number_1, "/", number_2, "=",
        divide(number_1, number_2))
else:
    print("Invalid input")