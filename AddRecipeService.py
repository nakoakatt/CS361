class AddRecipeService:
    def __init__(self):
        # Initialize an empty list to store recipes
        self.recipes = []

    def add_recipe(self, name, ingredients, instructions):
        # Create a dictionary representing the recipe
        recipe = {
            'name': name,  
            'ingredients': ingredients,  
            'instructions': instructions
        }
        # Append the recipe dictionary to the list of recipes
        self.recipes.append(recipe)
        print("Recipe added successfully!")
