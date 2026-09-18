
# ADDITION NUMBERS

def ADDITION():
    num1 = float(input("Enter The First Number: "))
    num2 = float(input("Enter The Second Number: "))
    
    print("--------------------------------------")
    print("Addition:", num1 + num2)
    print("--------------------------------------")


# SUBTRACTION NUMBERS

def SUBTRACTION():

    num1 = float(input("Enter The First Number: "))
    num2 = float(input("Enter The Second Number: "))
    
    print("--------------------------------------")
    print("Subtraction:", num1 - num2)
    print("--------------------------------------")


# MULTIPLICATION NUMBERS

def MULTIPLICATION():
    num1 = float(input("Enter The First Number: "))
    num2 = float(input("Enter The Second Number: "))
    
    print("--------------------------------------")
    print("Multiplication:", num1 * num2)
    print("--------------------------------------")


# DIVISION NUMBERS

def DIVISION():
    num1 = float(input("Enter The First Number: "))
    num2 = float(input("Enter The Second Number: "))
    
    print("--------------------------------------")
    if num2 == 0: 
        print("Error: Cannot divide by zero!")
    else:
        print("Division:", num1 / num2)
    print("--------------------------------------")

# CALCULATOR APP MENU

while True:

    print("\n===== CALCULATOR =====")

    print("1. ADDITION (+)")
    print("2. SUBRACTION (-)")
    print("3. MULTIPLICATION (*)")
    print("4. DIVISION (/)")
    print("5. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        ADDITION()

    elif choice == 2:

        SUBTRACTION()

    elif choice == 3:

        MULTIPLICATION()

    elif choice == 4:

        DIVISION()

    elif choice == 5:
        print("Thank you for using CALCULATOR APP!")
        break
    else:

        print("Invalid choice! Please try again.")