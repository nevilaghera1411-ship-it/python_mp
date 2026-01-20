# 2. Write a program to input 2 numbers and one arithmetic operator. Perform operations as per arithmetic operator which is given as inpu

num1 = float(input("enter num1: "))
num2 = float(input("enter num2: "))

op = input("enter arith op (+, -, *, /): ")

match op:
    case "+":
        print("Result:", num1 + num2)

    case "-":
        print("Result:", num1 - num2)

    case "*":
        print("Result:", num1 * num2)

    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")

    case _:
        print("Invalid operator")
