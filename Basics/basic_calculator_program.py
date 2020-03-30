def Add(num1, num2):
    return (num1 + num2)

def Subtract(num1, num2):
    return (num1 - num2)

def Multiply(num1, num2):
    return (num1 * num2)

def Divide(num1, num2):
    return (num1 // num2)

print("Please select operation - \n" \
    "1. Add\n" \
    "2. Subtract\n" \
    "3. Multiply\n" \
    "4. Divide\n" \
)

selected_operation = int(input("Select operations from 1, 2, " \
                            "3, 4 : "))

first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))

if (selected_operation == 1):
    print(first_number, "+", second_number, "=", 
        Add(first_number, second_number))
elif (selected_operation == 2):
    print(first_number, "-", second_number, "=", 
        Subtract(first_number, second_number))
elif (selected_operation == 3):
    print(first_number, "*", second_number, "=", 
        Multiply(first_number, second_number))
elif (selected_operation == 4):
    print(first_number, "/", second_number, "=", 
        Divide(first_number, second_number))
else:
    print("Invalid Input")