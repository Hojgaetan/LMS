# UML Diagrams for Library Management System


## Class Diagram

```plantuml
@startuml

package "Models" {
  abstract class BaseModel {
    # _attributes: dict
    + TABLE_NAME: str
    + PRIMARY_KEY: str
    + __init__(kwargs)
    # _get_attribute(name): Any
    # _set_attribute(name, value): void
    + __getattr__(name): Any
    + __setattr__(name, value): void
    + __dict__: dict
    + {static} find_by_id(id): BaseModel
    + {static} find_all(): List[BaseModel]
    + save(): int
    + delete(): void
  }

  class Book {
    + TABLE_NAME = 'books'
    + PRIMARY_KEY = 'book_id'
    + book_id: int
    + title: str
    + author_id: int
    + category_id: int
    + isbn: str
    + publication_year: int
    + publisher: str
    + quantity: int
    + available_quantity: int
    + {static} find_by_isbn(isbn): Book
    + {static} find_by_title(title): List[Book]
    + {static} find_by_author(author_id): List[Book]
    + {static} find_by_category(category_id): List[Book]
    + get_author(): Author
    + get_category(): Category
    + validate(): (bool, str)
  }

  class Author {
    + TABLE_NAME = 'authors'
    + PRIMARY_KEY = 'author_id'
    + author_id: int
    + name: str
    + biography: str
    + {static} find_by_name(name): List[Author]
    + get_books(): List[Book]
    + validate(): (bool, str)
  }

  class Category {
    + TABLE_NAME = 'categories'
    + PRIMARY_KEY = 'category_id'
    + category_id: int
    + name: str
    + description: str
    + {static} find_by_name(name): List[Category]
    + get_books(): List[Book]
    + validate(): (bool, str)
  }

  class Member {
    + TABLE_NAME = 'members'
    + PRIMARY_KEY = 'member_id'
    + member_id: int
    + name: str
    + email: str
    + phone: str
    + address: str
    + registration_date: str
    + {static} find_by_name(name): List[Member]
    + {static} find_by_email(email): Member
    + get_borrowings(): List[Borrowing]
    + validate(): (bool, str)
  }

  class Borrowing {
    + TABLE_NAME = 'borrowings'
    + PRIMARY_KEY = 'borrowing_id'
    + borrowing_id: int
    + book_id: int
    + member_id: int
    + borrow_date: str
    + due_date: str
    + return_date: str
    + status: str
    + {static} find_by_book(book_id): List[Borrowing]
    + {static} find_by_member(member_id): List[Borrowing]
    + {static} find_overdue(): List[Borrowing]
    + get_book(): Book
    + get_member(): Member
    + return_book(): (bool, str)
    + validate(): (bool, str)
  }
}

package "Controllers" {
  class BookController {
    + {static} add_book(title, author_id, category_id, isbn, publication_year, publisher, quantity): (bool, Any)
    + {static} get_book(book_id): Book
    + {static} get_all_books(): List[Book]
    + {static} search_books_by_title(title): List[Book]
    + {static} search_books_by_author(author_id): List[Book]
    + {static} search_books_by_category(category_id): List[Book]
    + {static} update_book(book_id, **kwargs): (bool, Any)
    + {static} delete_book(book_id): (bool, str)
    + {static} get_all_authors(): List[Author]
    + {static} get_all_categories(): List[Category]
  }

  class DatabaseController {
    + {static} initialize_database(force_reset): bool
    + {static} reset_database(): bool
  }
}

package "Views" {
  class MenuView {
    + {static} display_main_menu(): str
    + {static} display_message(message): void
    + {static} display_error(error): void
    + {static} display_success(message): void
    + {static} get_input(prompt): str
    + {static} get_int_input(prompt, default): int
  }

  class BookView {
    + {static} display_add_book_menu(): void
    + {static} display_authors(authors): void
    + {static} display_categories(categories): void
    + {static} get_book_details(): dict
    + {static} display_book(book): void
    + {static} display_books(books): void
  }
}

package "Utils" {
  class DatabaseConnection {
    - _DB_NAME: str
    + {static} get_db_name(): str
    + {static} set_db_name(db_name): void
    + {static} get_connection(): Connection
    + {static} execute_query(query, params): List
    + {static} execute_insert(query, params): int
    + {static} create_tables(): void
    + {static} insert_sample_data(): void
  }
}

class LibraryManagementSystem {
  - book_controller: BookController
  - menu_view: MenuView
  - book_view: BookView
  + __init__(): void
  + add_new_book(): void
  + run(): void
}

' Inheritance relationships
BaseModel <|-- Book
BaseModel <|-- Author
BaseModel <|-- Category
BaseModel <|-- Member
BaseModel <|-- Borrowing

' Associations
Book "1" -- "0..*" Borrowing: has >
Member "1" -- "0..*" Borrowing: makes >
Book "0..*" -- "1" Author: written by >
Book "0..*" -- "1" Category: belongs to >

' Dependencies
BaseModel ..> DatabaseConnection: uses >
BookController ..> Book: uses >
BookController ..> Author: uses >
BookController ..> Category: uses >
DatabaseController ..> DatabaseConnection: uses >
LibraryManagementSystem ..> DatabaseController: uses >
LibraryManagementSystem ..> BookController: uses >
LibraryManagementSystem ..> MenuView: uses >
LibraryManagementSystem ..> BookView: uses >

@enduml
```

## Package Diagram

```plantuml
@startuml@startuml
actor Bibliothécaire
actor Membre

rectangle "Système de gestion de bibliothèque" {
  Bibliothécaire -- (Ajouter un livre)
  Bibliothécaire -- (Mettre à jour un livre)
  Bibliothécaire -- (Supprimer un livre)
  Bibliothécaire -- (Consulter la liste des livres)
  Bibliothécaire -- (Gérer les auteurs)
  Bibliothécaire -- (Gérer les catégories)
  Bibliothécaire -- (Consulter les emprunts)
  Bibliothécaire -- (Gérer les membres)
  Bibliothécaire -- (Initialiser/réinitialiser la base de données)

  Membre -- (Rechercher un livre)
  Membre -- (Consulter la liste des livres)
  Membre -- (Emprunter un livre)
  Membre -- (Rendre un livre)
  Membre -- (Consulter ses emprunts)
}

(Ajouter un livre) .> (Gérer les auteurs) : <<include>>
(Ajouter un livre) .> (Gérer les catégories) : <<include>>
(Emprunter un livre) .> (Consulter la liste des livres) : <<include>>
@enduml

package "Models" {
  [BaseModel]
  [Book]
  [Author]
  [Category]
  [Member]
  [Borrowing]
}

package "Controllers" {
  [BookController]
  [DatabaseController]
}

package "Views" {
  [MenuView]
  [BookView]
}

package "Utils" {
  [DatabaseConnection]
}

[LibraryManagementSystem]

' Dependencies between packages
Models ..> Utils: uses
Controllers ..> Models: uses
Controllers ..> Utils: uses
LibraryManagementSystem ..> Controllers: uses
LibraryManagementSystem ..> Views: uses

@enduml
```

## Use Case Diagram

```plantuml
@startuml
actor Bibliothécaire
actor Membre

rectangle "Système de gestion de bibliothèque" {
  Bibliothécaire -- (Ajouter un livre)
  Bibliothécaire -- (Mettre à jour un livre)
  Bibliothécaire -- (Supprimer un livre)
  Bibliothécaire -- (Consulter la liste des livres)
  Bibliothécaire -- (Gérer les auteurs)
  Bibliothécaire -- (Gérer les catégories)
  Bibliothécaire -- (Consulter les emprunts)
  Bibliothécaire -- (Gérer les membres)
  Bibliothécaire -- (Initialiser/réinitialiser la base de données)

  Membre -- (Rechercher un livre)
  Membre -- (Consulter la liste des livres)
  Membre -- (Emprunter un livre)
  Membre -- (Rendre un livre)
  Membre -- (Consulter ses emprunts)
}

(Ajouter un livre) .> (Gérer les auteurs) : <<include>>
(Ajouter un livre) .> (Gérer les catégories) : <<include>>
(Emprunter un livre) .> (Consulter la liste des livres) : <<include>>
@enduml
```

## Explanation

### MVC Architecture

The Library Management System follows the Model-View-Controller (MVC) architectural pattern:

1. **Models**: Represent the data and business logic of the application
   - BaseModel: Abstract base class for all models
   - Book, Author, Category, Member, Borrowing: Domain-specific models

2. **Views**: Handle the presentation and user interface
   - MenuView: Displays menus and handles general user input
   - BookView: Handles book-specific display and input

3. **Controllers**: Mediate between models and views
   - BookController: Handles book-related operations
   - DatabaseController: Manages database initialization and reset

4. **Utils**: Provides utility functionality
   - DatabaseConnection: Handles low-level database operations

5. **Main Application**: Coordinates the overall application flow
   - LibraryManagementSystem: Main application class that ties everything together

### Key Relationships

- **Inheritance**: All model classes inherit from BaseModel, which provides common functionality for database operations and attribute management.

- **Associations**:
  - Books are written by Authors (many-to-one)
  - Books belong to Categories (many-to-one)
  - Books can be borrowed by Members through Borrowings (many-to-many)

- **Dependencies**:
  - Models depend on DatabaseConnection for database operations
  - Controllers depend on Models for data access and manipulation
  - The main application depends on Controllers and Views to implement functionality

### Encapsulation

All classes implement proper encapsulation:
- Model classes use private attributes with getters and setters
- Controllers provide a clean API for operations on models
- Views handle user interaction without exposing implementation details

This UML diagram provides a comprehensive overview of the Library Management System's architecture, showing the relationships between classes and the overall structure of the application.