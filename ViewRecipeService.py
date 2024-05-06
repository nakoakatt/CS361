class ViewRecipeService:
    def __init__(self, add_recipe_service):
        self.add_recipe_service = add_recipe_service

    def view_recipes(self):
        if not self.add_recipe_service.recipes:
            # If there are no recipes in the list, print a message and return
            print("No recipes available.")
            return
        # If there are recipes, print a header indicating the start of the list
        print("Recipes:")
        # Loop through each recipe in the list of recipes
        for idx, recipe in enumerate(self.add_recipe_service.recipes, start=1):
            # Print the index number and details of each recipe
            print(f"{idx}. Name: {recipe['name']}")
            print("   Ingredients:", ', '.join(recipe['ingredients']))
            print("   Instructions:", recipe['instructions'])
