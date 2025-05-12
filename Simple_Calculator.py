
# Ask the user to select an operator
# Then Ask the user to enter two Values/Numbers to perform that operation between those two Numbers.
# Writing conditions for each and every operator. And printing results corresponding to each and every operator.
# If user enter an Invalid operator, Print an Error Message.
# Ask user if they want to continue or not.
# If Yes repeat the same procedure, if No Terminate.
# Loop at the beginning makes the user to use the calculator multiple times if they want.


while True:
    oper = input("Enter an operator (+, -, *, /): ")
    num1 = float(input("Enter 1st Value: "))
    num2 = float(input("Enter 2nd Value: "))

    if oper == "+":
        result = num1 + num2
        print(round(result,3))
    elif oper == "-":
        result = num1 - num2
        print(round(result,3))
    elif oper == "*":
        result = num1 * num2
        print(round(result,3))
    elif oper == "/":
        result = num1 / num2
        print(round(result,3))
    else:
        print(f'{oper} is not a valid operator')

    should_continue = input("Want to use the Calculator again? (Y/N): ").lower()
    if should_continue == 'n':
        break

    # In some cases the result might have the large length of decimal point like "9.4333333333...". 
    # In such cases we use "round()" method. This will limit the decimals and print only integer part if we don't mention any value into the method.
    # If we want to print the decimal part also but upto 3 digits like "0.333" we can mention value "3" like this -> round(result,3). 