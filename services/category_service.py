from models.category import Category
from utils.db_utils import DatabaseConnection


class CategoryService:
    """Controller for category-related operations."""

    @staticmethod
    def add_category(name, description=None):
        category = Category(name=name, description=description)
        valid, msg = category.validate()
        if not valid:
            return False, msg
        category.save()
        return True, f"Category '{name}' added successfully."

    @staticmethod
    def update_category(category_id, name=None, description=None):
        category = Category.find_by_id(category_id)
        if not category:
            return False, "Category not found."
        if name:
            category.name = name
        if description:
            category.description = description
        valid, msg = category.validate()
        if not valid:
            return False, msg
        category.save()
        return True, f"Category '{category_id}' updated successfully."

    @staticmethod
    def delete_category(category_id):
        category = Category.find_by_id(category_id)
        if not category:
            return False, "Category not found."
        category.delete()
        return True, f"Category '{category_id}' deleted successfully."

    @staticmethod
    def list_categories():
        return Category.all()

    @staticmethod
    def search_categories_by_name(name):
        return Category.find_by_name(name)

    @staticmethod
    def count_categories():
        """
        Count the total number of categories.

        Returns:
            int: The total number of categories
        """
        return len(Category.all())

    @staticmethod
    def get_category_name(category_id):
        """
        Get the name of a category by its ID.

        Args:
            category_id (int): The ID of the category.

        Returns:
            str: The name of the category, or None if not found.
        """
        category = Category.find_by_id(category_id)
        return category.name if category else None

    @staticmethod
    def get_category_by_name(name):
        """
        Get a category by its exact name.

        Args:
            name (str): The exact name of the category.

        Returns:
            Category: The category object if found, None otherwise.
        """
        categories = Category.find_by_name(name)
        if categories:
            # Return the first exact match
            for category in categories:
                if category.name.lower() == name.lower():
                    return category
        return None

