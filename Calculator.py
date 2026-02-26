"""Python Based Calculator"""
def calculator(operation):
 number = int(input("On how many numbers You Have to Perform Operations"))

 if number == 2:
  num1 = int(input("Enter 1st Number "))
  num2 = int(input("Enter 2nd Number "))
  result = eval(f"{num1} {operation} {num2}")
  print(f"Result is {result}")
 elif number == 3:
    num1 = int(input("Enter 1st Number "))
    num2 = int(input("Enter 2nd Number "))
    num3 = int(input("Enter 3rd Number "))
    result = eval(f"{num1} {operation} {num2} {operation} {num3}")
    print(f"Result is {result}")

    def main():
        print("Welcome to Python Based Calculator")
        print("Available Operations: +, -, *, /")
        operation = input("Enter the Operation you want to perform ")
        calculator(operation)