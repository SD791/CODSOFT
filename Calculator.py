# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

def main():
    print("Select operation :")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take user input for operation
        select = input("Select operations form (1/2/3/4): ")

        # Validate the choice and proceed
        if select in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue    

             # Perform the selected operation based on the user's choice
            if select == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif select == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif select == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif select == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        
            # check if user wants another calculation
            # break the while loop if answer is no
            ans = input("Let's do next calculation? (yes/no): ")
            if ans == "no":
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()

