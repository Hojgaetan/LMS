from models.author import Author
from utils.db_utils import DatabaseConnection


class AuthorService:
    """Controller for author-related operations."""

    @staticmethod
    def add_author(name, biography=None):
        author = Author(name=name, biography=biography)
        valid, msg = author.validate()
        if not valid:
            return False, msg
        author.save()
        return True, f"Author '{name}' added successfully."

    @staticmethod
    def update_author(author_id, name=None, biography=None):
        author = Author.find_by_id(author_id)
        if not author:
            return False, "Author not found."
        if name:
            author.name = name
        if biography:
            author.biography = biography
        valid, msg = author.validate()
        if not valid:
            return False, msg
        try:
            author.save()
        except Exception as e:
            return False, f"Failed to update author: {str(e)}"
        return True, f"Author '{author_id}' updated successfully."

    @staticmethod
    def delete_author(author_id):
        author = Author.find_by_id(author_id)
        if not author:
            return False, "Author not found."
        try:
            author.delete()
        except Exception as e:
            return False, f"Failed to delete author: {str(e)}"
        return True, f"Author '{author_id}' deleted successfully."

    @staticmethod
    def list_authors():
        return Author.all()

    @staticmethod
    def search_authors_by_name(name):
        return Author.find_by_name(name)

    @staticmethod
    def count_authors():
        """
        Count the total number of authors.

        Returns:
            int: The total number of authors
        """
        return len(Author.all())

    @staticmethod
    def get_author_name(author_id):
        """
        Get the name of an author by their ID.

        Args:
            author_id (int): The ID of the author.

        Returns:
            str: The name of the author, or None if not found.
        """
        author = Author.find_by_id(author_id)
        return author.name if author else None

