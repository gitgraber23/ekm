import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def percentage(part, whole):
    return (part / whole) * 100

def average(numbers):
    return sum(numbers) / len(numbers)

def area_of_circle(radius):
    return math.pi * radius ** 2

def circumference_of_circle(radius):
    return 2 * math.pi * radius

def power(base, exp):
    return base ** exp

def square_root(num):
    return math.sqrt(num)

def factorial(num):
    return math.factorial(num)

def logarithm(value, base):
    return math.log(value, base)

def main():
    while True:
        print("\n===== Advanced Python Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Average")
        print("7. Area of Circle")
        print("8. Circumference of Circle")
        print("9. Power")
        print("10. Square Root")
        print("11. Factorial")
        print("12. Logarithm")
        print("13. Exit")
        
        choice = input("Choose an option (1-13): ")
        
        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", add(a, b))
        
        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", subtract(a, b))
        
        elif choice == "3":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", multiply(a, b))
        
        elif choice == "4":
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            print("Result:", divide(a, b))
        
        elif choice == "5":
            part = float(input("Enter part value: "))
            whole = float(input("Enter whole value: "))
            print("Percentage:", percentage(part, whole), "%")
        
        elif choice == "6":
            nums = input("Enter numbers separated by space: ").split()
            nums = [float(x) for x in nums]
            print("Average:", average(nums))
        
        elif choice == "7":
            r = float(input("Enter radius: "))
            print("Area of Circle:", area_of_circle(r))
        
        elif choice == "8":
            r = float(input("Enter radius: "))
            print("Circumference of Circle:", circumference_of_circle(r))
        
        elif choice == "9":
            base = float(input("Enter base: "))
            exp = float(input("Enter exponent: "))
            print("Result:", power(base, exp))
        
        elif choice == "10":
            num = float(input("Enter number: "))
            print("Square Root:", square_root(num))
        
        elif choice == "11":
            num = int(input("Enter number: "))
            print("Factorial:", factorial(num))
        
        elif choice == "12":
            val = float(input("Enter value: "))
            base = float(input("Enter base: "))
            print("Logarithm:", logarithm(val, base))
        
        elif choice == "13":
            print("Exiting Calculator... Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select again.")

if __name__ == "__main__":
    main()
