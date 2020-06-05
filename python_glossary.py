# My Python glossary
# Previously in python_work/chapter6

import glossary_functions as gf
import glossary as g
# Data

miscallenous, data_types, methods = '', '', ''
glossary = g.Glossary(miscallenous, data_types, methods)
# Miscallenous

miscallenous = {
    "tuple": "immutable list",
    "dictionary": "data structure that allows for mapping key-value pairs",
    "PEP": "Python Enhancement Proposal",
    "conditional test": "test that returns either 'True' or 'False'",
    "list comprehension": "concise way of creatint a list",
    "set": "data structure in which each item must be unique",
    "float": "any number with a decimal point",
    "f-string": "formatted string, variable name replaced with value",
    "constant": "variable whose value stays the same during life of prog",
    "range()": "returns value within given range - [x,y)",
}

# Data types

data_types = {
    "string": "any set of characters enclosed with''",
    "numbers": "numerical data in a form of integers or floats",
}

# Methods

methods = {
    "title()": "converts string value into a title case",
    "lower()": "converts string value into a lower case",
    "upper()": "converts string value into an upper case",
    "range()": "returns numbers from a given range",
    "append()": "appends an item to a list",
    "remove()": "removes an item from a list by value",
    "items()": "returns key-value pairs from a dictionary",
    "keys()": "returns keys from a dictionary",
    "values()": "returns values from a dictionary",
}



print("\nWelcome to the Python Glossary created by Arkadiusz Podkowa.")
print("Refer to this document whenever you need help with a particular python element.\n")

active = True
while active:
    # Input possibilities:
    instr = "\nEnter either 'a' (add),"
    instr += " 'f' (find),"
    instr += " 'l' (list all),"
    instr += " 'r' (remove,"
    instr += " 'h' (help),"
    instr += " or 'q' (quit): "
    task = input(instr)
    if task == 'a':
        gf.add_term()
    elif task == 'f':
        gf.find_term()
    elif task == 'l':
        gf.list_all()
    elif task == 'r':
        gf.remove_term()
    elif task == 'h':
        gf.get_help()
    elif task == 'q':
        gf.quit()
