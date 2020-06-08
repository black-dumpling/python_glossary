"""Classes to model glossary."""

class Glossary:
    """Class that models glossary."""

    def __init__(self, glossary):
        """Initialize attributes."""
        self.glossary = glossary

    def show_categories(self):
        """Displays all categories of a glossary."""
        print("\nAvailable categories: ")
        for category in self.glossary:
            print(category)


    def add_term(self):
        """Add term to the specific category."""
        print("\n--- Add a term ---")
        print("Available categories: ")
        for category in self.glossary:
            print(f"\t{category}")
        category = input("\nEnter category: ")
        term = input("Enter term: ")
        definition = input("Enter definition: ")
        if term in self.glossary[category]:
            confirm = input(f"\nTerm '{term}' exists in '{category}', do you want"
                  " to  overwrite it? (y/n) ")
            if confirm == 'y':
                self.glossary[category][term] = definition
                print(f"\n'{term}' modified in '{category}'.")
            else:
                pass
        else:
            self.glossary[category][term] = definition
            print(f"\n'{term}' added to '{category}'.")



    def add_category(self):
        """Add another category."""
        category = input("\nEnter a new category: ")
        if category in self.glossary:
            print(f"'{category}' already exists and cannot be overwritten!")
        elif category not in self.glossary:
            self.glossary[category] = {}


    def find_term(self):
        """Find specific term."""
        print("\n--- Find a term ---")
        find = input("Enter search phrase: ")
        for category in self.glossary:
            if find in self.glossary[category]:
                display = f"\t{find}: {self.glossary[category][find]}"
                print(display)
                break


    def list_all(self):
        """List all terms from the glossary."""
        for category in self.glossary:
            print(f"\n{category}")
            for term in self.glossary[category]:
                print(f"\t{term}: {self.glossary[category][term]}")

    def remove_term(self):
        """Remove term from the glossary."""
        remove = input("\nEnter term you want to remove: ")
        confirm = input("Are you sure you want to"
                        f" remove '{remove}'? (y/n [n]) ")
        if confirm == 'y':
            for category in self.glossary:
                if remove in self.glossary[category]:
                    del self.glossary[category][remove]
                    print(f"\n'{remove}' has been removed from '{category}'.")
                    break
        elif confirm == 'n' or confirm == '':
            print("\nRemoval canceled.")
        else:
            print("\nError: use either 'y', 'n' or simply press enter")


    def get_help(self):
        """Display help information about the usage of the glossary."""
        # Display the usage info.
        print("\nUsage: ")
        print("\t'a' (add) - add term or category")
        print("\t'f' (find) - find specific term")
        print("\t'l' (list all) - list all terms from glossary")
        print("\t'r' (remove) - remove specific term")
        print("\t'h' (help) - print usage info")
        print("\t'q' (quit) - quit glossary")


    def quit(self, flag):
        """Quit the glossary program"""
        flag == False
