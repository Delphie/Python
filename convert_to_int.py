try:
    user_input1 = input("Enter the first number: ")
    user_input2 = input("Enter the second number: ")
    num1 = float(user_input1)
    num2 = float(user_input2)
    print("The sum is:", num1 + num2)
except ValueError:
    print("At least one input was not a number.")
