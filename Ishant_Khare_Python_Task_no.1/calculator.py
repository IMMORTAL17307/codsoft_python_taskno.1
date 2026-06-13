def run_calculator():
    print("--- Calculator Program ---")
    
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    print("Choose operation:")
    print("  +  for Addition")
    print("  -  for Subtraction")
    print("  *  for Multiplication")
    print("  /  for Division")
    operation = input("Enter your choice (+, -, *, /): ").strip()
    

    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return


    if operation == '+':
        result = num1 + num2
        print("Result:", num1, "+", num2, "=", result)
    elif operation == '-':
        result = num1 - num2
        print("Result:", num1, "-", num2, "=", result)
    elif operation == '*':
        result = num1 * num2
        print("Result:", num1, "*", num2, "=", result)
    elif operation == '/':
      
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Result:", num1, "/", num2, "=", result)
    else:
        print("Error: Invalid operation choice.")

if __name__ == "__main__":
    while True:
        run_calculator()
        print()

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != "yes" and again != "y":
            print("Goodbye!")
            break
        print()
