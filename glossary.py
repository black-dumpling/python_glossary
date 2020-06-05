"""Classes to model glossary."""

class Glossary:
    """Class that models glossary."""

    def __init__(self, *categories):
        """Initialize attributes."""
        self.categories = list(categories)

    def show_categories(self):
        """Displays all categories of a glossary."""
        print(self.categories)


    def add_term(self):
        """Add term to the specific category."""
        print("\n--- Add a term ---")
        print("Available categories: ")
        for category in self.categories:
            print(f"\t{category}")
        category = input("Enter category: ")
        term = input("Enter term: ")
        definition = input("Enter definition: ")
        category[term] = definition 
        print(f"\n{term} added to {category}.")


    def add_category(self, category):
        """Add another category."""
        category = input("enter a new category: ")
        self.categories.append(category)


    def find_term(self):
        """Find specific term."""
        print("\n--- Find a term ---")
        find = input("Enter search phrase: ")
        for category in self.categories:
            if find in category:
                display = f"\t{find}: {category[find]}"
                print(display)
                break


    def list_all(self):
        """List all terms from the glossary."""
        for term, definition in glossary.items():
            print(f"{term}: {definition}")

    def remove_term(self):
        """Remove term from the glossary."""
        remove = input("Enter term you want to remove: ")
        confirm = input("Are you sure you want to"
                        f" remove {remove}? (y/n [n])")
        if confirm == 'y':
            # Remove term.
        elif confirm == 'n' or confirm == '':
            print("Removal canceled.")
        else:
            print("Error: use either 'y', 'n' or simply press enter")


    def get_help(self):
        """Display help information about the usage of the glossary."""
        # Display the usage info.


    def quit(self):
        """Quit the glossary program"""
        active == False
