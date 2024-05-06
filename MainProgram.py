from AddRecipeService import AddRecipeService
from ViewRecipeService import ViewRecipeService
from DeleteRecipeService import DeleteRecipeService

class MainProgram:
    def __init__(self):
        # Initialize instances of services needed for recipe management
        self.add_recipe_service = AddRecipeService()  
        self.view_recipe_service = ViewRecipeService(self.add_recipe_service)  
        self.delete_recipe_service = DeleteRecipeService() 

    def main_menu(self):
        # Main menu loop
        while True:
            print("\nWelcome to Recipe Manager!")
            print("Main Menu:")
            print("1. View Recipes")
            print("2. Add Recipe")
            print("3. Delete Recipe")
            print("4. View Recipe")
            print("5. Exit")

            # Prompt user for menu choice
            choice = input("Please enter the number corresponding to your choice: ")

            if choice == '1':
                # View recipes
                self.view_recipe_service.view_recipes()
            elif choice == '2':
                # Add a new recipe
                name = input("Enter recipe name: ")
                ingredients = input("Enter ingredients (comma-separated): ").split(',')
                instructions = input("Enter instructions: ")
                self.add_recipe_service.add_recipe(name, ingredients, instructions)
            elif choice == '3':
                # Delete a recipe
                name = input("Enter recipe name to delete: ")
                self.delete_recipe_service.delete_recipe(name, self.add_recipe_service)  
            elif choice == '4':
                # View details of a specific recipe
                name = input("Enter recipe name to view: ")
                self.view_recipe_service.view_recipe(name)
            elif choice == '5':
                # Exit the program
                print("Exiting Recipe Manager.")
                break
            else:
                # Invalid input handling
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    # Create an instance of MainProgram and start the main menu loop
    program = MainProgram()
    program.main_menu()
