
# ADDITION NUMBERS

class calculation: 
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2

    def ADDITION(self):
        print("-"*30)
        print("Addition:", self.number1 + self.number2)
        print("-"*30)
    def SUBTRACTION(self):
        print("-"*30)
        print("Subtraction:", self.number1 - self.number2)
        print("-"*30)
    def MULTIPLICATION(self):
        print("-"*30)
        print("Multiplication:", self.number1 * self.number2)
        print("-"*30)
    def DIVISION(self):
        print("-"*30)
        if self.number2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Division:", self.number1 / self.number2)
        print("-"*30)    

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

        number1 = float(input("Enter The First Number: "))
        number2 = float(input("Enter The Second Number: "))
        obj1 = calculation(number1,number2)
        obj1.ADDITION()

    elif choice == 2:

        number1 = float(input("Enter The First Number: "))
        number2 = float(input("Enter The Second Number: "))
        obj1 = calculation(number1,number2)
        obj1.SUBTRACTION()

    elif choice == 3:

        number1 = float(input("Enter The First Number: "))
        number2 = float(input("Enter The Second Number: "))
        obj1 = calculation(number1,number2)
        obj1.MULTIPLICATION()

    elif choice == 4:

        number1 = float(input("Enter The First Number: "))
        number2 = float(input("Enter The Second Number: "))
        obj1 = calculation(number1,number2)
        obj1.DIVISION()

    elif choice == 5:
        print("Thank you for using CALCULATOR APP!")
        break
    else:

        print("Invalid choice! Please try again.")