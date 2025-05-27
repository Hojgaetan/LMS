class CategoryView:
    """View class for category-related user interface."""

    @staticmethod
    def display_add_category_menu():
        print("\n===== Add New Category =====")
        name = input("Name (required): ")
        description = input("Description (optional): ")
        return name, description

    @staticmethod
    def display_update_category_menu():
        print("\n===== Update Category =====")
        category_id = input("Category ID to update: ")
        name = input("New Name (press Enter to skip): ")
        description = input("New Description (press Enter to skip): ")
        return category_id, name, description

    @staticmethod
    def display_delete_category_menu():
        print("\n===== Delete Category =====")
        category_id = input("Category ID to delete: ")
        return category_id

    @staticmethod
    def display_categories(categories):
        print("\n===== Categories List =====")
        if not categories:
            print("No categories found.")
            return
        for category in categories:
            print(f"ID: {category.category_id} | Name: {category.name} | Description: {category.description}")

    @staticmethod
    def display_search_category_menu():
        print("\n===== Search Category =====")
        name = input("Name (partial or full): ")
        return name

    @staticmethod
    def display_message(message):
        print(message)
