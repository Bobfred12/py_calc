def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
    # Handle division by Zero error
        return "Error! Division by zero"
    else:
        return x/y 
def main():
    #Display menu options
    print("Simple CLI Calculate")
    print("SELECT OPERATION:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    # Get uswr choice
    choice = input("Enter choice(1/2/3/4): ")
    #Check if choice is valid
    if choice in['1','2','3','4']:
        try:
            #Ask user to input two numbers
            num1 =float(input("Enter first numbers "))
            num2 =float(input("Enter second number "))
        except ValueError:
            #Handle invalid numeric input
            print("Invalid input! Please enter numneric values.")
            return # Exit the function
            # Perform calculation based on user choice
        if choice =='1':
            print(f'{num1} + {num2} = {add(num1,num2)}')
        elif choice == '2':
            print(f"{num1} -{num2} = {subtract(num1,num2)}")
        elif choice == '3':
            print(f"{num1}* {num2} = {multiply(num1,num2)}")
        elif choice == '4':
            result = divide(num1,num2)
            print(f"{num1}/{num2} = {result}")
    else:
        # Handle invalid operation choice
        print("Invalid choice!")
# Run the main function only if this script is executed directly 
if __name__ == "__main__":
    main()