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
        if term in self.glossary[category]:
            confirm = input(f"\nTerm '{term}' exists in '{category}', do you want"
                  " to  overwrite it? (y/n) ")
            if confirm == 'y':
                definition = input("Enter definition: ")
                self.glossary[category][term] = definition
                print(f"\n'{term}' modified in '{category}'.")
        else:
            definition = input("Enter definition: ")
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


    def move(self):
        """Move an item from one category to another."""
        term = input("\nEnter term you want to move: ")
        count_nonmatch = 0
        for category in self.glossary:
            if term in self.glossary[category]:
                confirm = input(f"\nDo you want to move '{term}'"
                                f" from '{category}'? (y/n [n]) ")
                if confirm == 'y':
                    destination = input("Where do you want to move it? ")
                    if destination in self.glossary:
                        origin = self.glossary[category][term]
                        self.glossary[destination][term] = origin
                        del self.glossary[category][term]
                        print(f"\n'{term}' successfully moved to '{destination}'.")
                    else:
                        print(f"Category '{destination}' does not exist.")
                elif confirm != 'y' and confirm != 'n' and confirm != '':
                    print("\nError: use either 'y', 'n' or simply press enter")
            else:
                count_nonmatch += 1
                continue
        if count_nonmatch == len(self.glossary):
            print(f"\n'{term}' does not exist.")

                            


    def remove_term(self):
        """Remove term from the glossary."""
        remove = input("\nEnter term you want to remove: ")
        exists_in = []
        for category in self.glossary:
            if remove in self.glossary[category]:
                exists_in.append(category)
        if exists_in:
            print(f"\nFound '{remove}' in these categories:")
            for category in exists_in:
                print(f"\t{category}")
            for category in exists_in:
                confirm = input("\nAre you sure you want to remove"
                                f" '{remove}' from '{category}'? (y/n [n]) ")
                if confirm == 'y':
                    del self.glossary[category][remove]
                    print(f"\n'{remove}' has been removed from '{category}'.")
                elif confirm == 'n' or confirm == '':
                    print("\nRemoval canceled.")
                    break
                else:
                    print("\nError: use either 'y', 'n' or simply press enter")
        else:
            print(f"'{remove}' has not been found.")


    def get_help(self):
        """Display help information about the usage of the glossary."""
        # Display the usage info.
        print("\nUsage: ")
        print("\t'a' (add) - add term or category")
        print("\t'f' (find) - find specific term")
        print("\t'l' (list all) - list all terms from glossary")
        print("\t'm' (move) - move item to another category")
        print("\t'r' (remove) - remove specific term")
        print("\t'h' (help) - print usage info")
        print("\t'q' (quit) - quit glossary")


    def quit(self, flag):
        """Quit the glossary program"""
        flag == False
