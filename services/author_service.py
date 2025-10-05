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
    def get_or_create_author(name, biography=None):
        """Return existing author id or create a new one.
        Returns: (success: bool, result: int | str) -> id ou message d'erreur
        """
        # Recherche exacte (case insensitive)
        existing = Author.find_by_name(name)
        if existing:
            # On privilégie une correspondance exacte
            for a in existing:
                if a.name.lower() == name.lower():
                    return True, a.author_id
            # Sinon on prend le premier
            return True, existing[0].author_id
        # Créer si absent
        created_ok, msg = AuthorService.add_author(name=name, biography=biography)
        if not created_ok:
            return False, msg
        # Rechercher à nouveau pour récupérer l'ID
        created_list = Author.find_by_name(name)
        if created_list:
            return True, created_list[0].author_id
        return False, "Author creation failed (ID not retrievable)."

    @staticmethod
    def get_author(author_id: int):
        """Retourne l'objet Author ou None."""
        return Author.find_by_id(author_id)

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

    # Alias rétrocompatible pour éviter les erreurs si du code externe utilise encore ce nom.
    @staticmethod
    def get_all_authors():
        """
        Deprecated: utiliser list_authors().
        Conserve la compatibilité avec l'ancien code.
        """
        return AuthorService.list_authors()

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
