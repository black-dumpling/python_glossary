# My Python glossary
# Previously in python_work/chapter6

import glossary as g

import json

# Read glossary.
filename = 'glossary.json'
try:
    with open(filename) as f:
        data = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        json.dump({}, f)
    with open(filename) as f:
        data = json.load(f)
        

# Instantialize glossary.
glossary = g.Glossary(data)


print("\n----- Python Glossary -----")
print("\nWelcome to the Python Glossary created by Arkadiusz Podkowa.")
print("Refer to this document, whenever you need help with a particular python element.\n")

while True:
    # Input possibilities:
    instr = "\nEnter either 'a' (add),"
    instr += " 'f' (find),"
    instr += " 'l' (list all),"
    instr += " 'r' (remove,"
    instr += " 'h' (help),"
    instr += " or 'q' (quit): "
    task = input(instr)
    if task == 'a':
        kind = input("Do you want to add category or term? (c/t or anything"
                     " else to abort) ")
        if kind == 'c':
            glossary.add_category()
        elif kind == 't':
            glossary.add_term()
        else:
            pass
    elif task == 'f':
        glossary.find_term()
    elif task == 'l':
        glossary.list_all()
    elif task == 'r':
        glossary.remove_term()
    elif task == 'h':
        glossary.get_help()
    elif task == 'q':
        break
    else:
        glossary.get_help()


# Write glossary.
with open(filename, 'w') as f:
    json.dump(glossary.glossary, f)
