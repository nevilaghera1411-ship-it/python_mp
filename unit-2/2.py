# 2.Write a program to execute user defined exception in python.

class AgeNotValidError(Exception):
    pass

print("User Defined Exception Program")

try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise AgeNotValidError("Age must be 18 or above!")
    
    print("You are eligible.")

except AgeNotValidError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Error: Please enter a valid number.")

finally:
    print("Program Ended.")
