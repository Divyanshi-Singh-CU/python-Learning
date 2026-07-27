#Experiment_02

# Simple Calculator Application

print("SIMPLE CALCULATOR")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5.Modulus (%)")
print("6.power (**)")
print("7.floor division (//)")

choice = input("Enter your choice (1-7): ")

if choice == "1":
    result = num1 + num2
    print("Result of addition  =", result)

elif choice == "2":
    result = num1 - num2
    print("Result of subtraction  =", result)

elif choice == "3":
    result = num1 * num2
    print("Result of multiplication =", result)

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("Result of division =", result)
    else:
        print(" Division by zero is not allowed.")
elif choice=="5":
    if num2 != 0:
            result = num1 % num2
            print("Result of Modulus =", result)
elif choice=="6":
    result=num1**num2
    print("Result of Power=",result)

elif choice=="7":
    if num2 != 0:
            result = num1 // num2
            print("Result of floor division =", result) 
    else:
        print(" Division by zero is not allowed.")



else:
    print("Invalid choice! Please enter a number between 1 and 7.")
 
