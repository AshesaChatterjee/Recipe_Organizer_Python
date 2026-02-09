import json
import os

FILE_NAME = "recipes.json"

class RecipeManager:
    def __init__(self):
        self.recipes = self.load_recipes()

    def load_recipes(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        return {}

    def save_recipes(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.recipes, file, indent=4)

    def add_recipe(self):
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma separated): ")
        steps = input("Enter preparation steps: ")

        self.recipes[name] = {
            "ingredients": ingredients.split(","),
            "steps": steps
        }

        self.save_recipes()
        print("✅ Recipe added successfully!\n")

    def view_recipes(self):
        if not self.recipes:
            print("No recipes found.\n")
            return

        for name, details in self.recipes.items():
            print(f"\n🍲 {name}")
            print("Ingredients:", ", ".join(details["ingredients"]))
            print("Steps:", details["steps"])

    def search_recipe(self):
        name = input("Enter recipe name to search: ")
        recipe = self.recipes.get(name)

        if recipe:
            print(f"\n🍲 {name}")
            print("Ingredients:", ", ".join(recipe["ingredients"]))
            print("Steps:", recipe["steps"])
        else:
            print("❌ Recipe not found.\n")

    def update_recipe(self):
        name = input("Enter recipe name to update: ")

        if name in self.recipes:
            ingredients = input("Enter new ingredients: ")
            steps = input("Enter new steps: ")

            self.recipes[name] = {
                "ingredients": ingredients.split(","),
                "steps": steps
            }

            self.save_recipes()
            print("✅ Recipe updated successfully!\n")
        else:
            print("❌ Recipe not found.\n")

    def delete_recipe(self):
        name = input("Enter recipe name to delete: ")

        if name in self.recipes:
            del self.recipes[name]
            self.save_recipes()
            print("🗑️ Recipe deleted successfully!\n")
        else:
            print("❌ Recipe not found.\n")


def main():
    manager = RecipeManager()

    while True:
        print("""
==== Recipe Organizer ====
1. Add Recipe
2. View Recipes
3. Search Recipe
4. Update Recipe
5. Delete Recipe
6. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            manager.add_recipe()
        elif choice == "2":
            manager.view_recipes()
        elif choice == "3":
            manager.search_recipe()
        elif choice == "4":
            manager.update_recipe()
        elif choice == "5":
            manager.delete_recipe()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()