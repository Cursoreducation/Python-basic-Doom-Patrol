from calc_func import *
from globals import *


"""
    Calculator program
    choose one operation from menu:
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      5. Power by N
    Input two values
    result will be written to file
    
    calc_main.py - main module for interaction with user
    calc_func.py - module with all calculation and working with files methods
    globals.py - global variables and imports
"""

clear_file("output_results/result.txt")
stop = False

while not stop:

    operation = int(input("Choose one operation: \n"
                          "1. Add \n"
                          "2. Subtract \n"
                          "3. Multiply \n"
                          "4. Divide \n"
                          "5. Power by N\n"
                          "6. Stop \n"))

    if operation == 6:
        stop = True
    else:
        x = input("First value: ")
        y = input("Second Value: ")

        if operation in operations.keys():
            write_to_file("output_results/result.txt",
                          eval(operations[operation][0] + "(" + x + "," + y + ")"))
