class AuthorView:
    """View class for author-related user interface."""

    @staticmethod
    def display_add_author_menu():
        print("\n===== Add New Author =====")
        name = input("Name (required): ")
        biography = input("Biography (optional): ")
        return name, biography

    @staticmethod
    def display_update_author_menu():
        print("\n===== Update Author =====")
        author_id = input("Author ID to update: ")
        name = input("New Name (press Enter to skip): ")
        biography = input("New Biography (press Enter to skip): ")
        return author_id, name, biography

    @staticmethod
    def display_delete_author_menu():
        print("\n===== Delete Author =====")
        author_id = input("Author ID to delete: ")
        return author_id

    @staticmethod
    def display_authors(authors):
        print("\n===== Authors List =====")
        if not authors:
            print("No authors found.")
            return
        for author in authors:
            print(f"ID: {author.author_id} | Name: {author.name} | Biography: {author.biography}")

    @staticmethod
    def display_search_author_menu():
        print("\n===== Search Author =====")
        name = input("Name (partial or full): ")
        return name

    @staticmethod
    def display_message(message):
        print(message)
