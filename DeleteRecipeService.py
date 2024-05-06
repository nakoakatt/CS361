class DeleteRecipeService:
    def __init__(self):
        pass  

    def delete_recipe(self, name, add_recipe_service):
        # Loop through each recipe in the list of recipes stored in AddRecipeService
        for idx, recipe in enumerate(add_recipe_service.recipes):
            # Check if the name of the current recipe matches the name to be deleted
            if recipe['name'] == name:
                # If found, delete the recipe from the list
                del add_recipe_service.recipes[idx]
                print(f"Recipe '{name}' deleted successfully.")
                return  # Exit the method after deletion
        print(f"Recipe '{name}' not found.")
