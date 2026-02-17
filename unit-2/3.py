# 3. Write a program to generate arithmetic exception and log the exception in system.

import logging

logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b
    print("Result =", result)

except Exception as e:
    print("Error occurred!")
    logging.error("Exception occurred: " + str(e))

print("Program Ended.")
