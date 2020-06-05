"""Functions that can be used to model a glossary."""

def add_term():
    """Add term to the specific category."""
    if task == "a":
        print("\n--- Add a term ---")
        print("Available categories: ")
        category = input("Enter category: ")
        term = input("Enter term: ")
        definition = input("Enter definition: ")
        category[term] = definition 
        print(f"\n{term} added to {category}.")
        

def find_term():
    """Find specific term."""
    if task == "f":
        find = input("Enter search phrase: ")
        if find in miscallenous.keys():
            display = f"\t{find}: {miscallenous[find]}"
        elif find in data_types.keys():
            display = f"\t{find}: {data_types[find]}"
        elif find in methods.keys():
            display = f"\t{find}: {methods[find]}"
        else: 
            display = "\tThere is no such entry."
        print(display)


def list_all():
    """list all terms in a given category."""
    if task == "l":
        category = input("Which category do you want to list? ")
        if category == "data_types":
            display = data_types
        elif category == "methods":
            display = methods
        elif category == "miscallenous":
            display = miscallenous
        else:
            display = "There is no such category."
        print(display)


def get_help():
    """Print available commands."""
    if task == "h":
        print("\n--- Help ---")
        print("Following commands are available: ")


def quit():
    """Quit the program."""
    if task == "q":
        print("Quitting...")
        active = False

