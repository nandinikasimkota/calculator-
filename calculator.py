def calculator():
    print("Welcome to Simple Calculator")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation.")
                continue

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the calculator.")
            break

calculator()