# 1) Write a program to display basic exception handling in python.

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Please provide numerical inputs."
    else:
        return f"Success! The result is {result}"
    finally:
        print("Execution of the division block is complete.")

print(divide_numbers(10, 2))
print("-" * 10)
print(divide_numbers(10, 0))
print("-" * 10)
print(divide_numbers(10, "a"))