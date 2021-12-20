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
proceed = "y"

while proceed == "y":

    proceed = input("Do You want to calculate Y/N: \n")

    if proceed.lower() == 'y':
        x = input("First value: ")
        operation = input("Choose one operation: \n"
                          "Add: + \n"
                          "Subtract: - \n"
                          "Multiply: * \n"
                          "Divide: / \n"
                          "Power by N: ** \n")
        y = input("Second Value: ")

        if operation not in operations.values():
            print("Hm... I don't know how to calculate =(((")
        else:
            for key in operations.keys():
                if operation == operations[key]:
                    func = key

            write_to_file("output_results/result.txt",
                          eval(func + "(" + x + "," + y + ")"))
