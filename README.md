# Library Management System (LMS)

![forks](https://img.shields.io/github/forks/Hojgaetan/LMS)
[![commits](https://img.shields.io/github/commit-activity/w/Hojgaetan/LMS)](https://github.com/Hojgaetan/LMS/commits/main)
![contributors](https://img.shields.io/github/contributors/Hojgaetan/LMS)
![MIT License Badge](https://img.shields.io/badge/license-MIT-green)

## Overview
The Library Management System (LMS) is a robust, modular application designed to streamline and automate the management of library resources. Built with a scalable architecture and following the Model-View-Controller (MVC) pattern, LMS provides a comprehensive suite of features for book, author, category, member, and borrowing management, as well as advanced reporting and administrative controls.

## Key Features

### 📚 Book Management
- ➕ **Add, update, and remove books**: Manage your library's collection effortlessly.
- 🔍 **Search books by title**: Quickly locate books using a powerful search feature.
- 📝 **View detailed book information**: Access comprehensive details about each book.
- 📦 **Manage book inventory and availability**: Keep track of stock and borrowing status.

### ✍️ Author & Category Management
- 🖊️ **Register and update authors and categories**: Organize books by authors and genres.
- 📖 **View all books by a specific author or within a category**: Simplify browsing and discovery.

### 👥 Member Management
- 🆕 **Register, update, and manage library members**: Maintain member profiles and activity.
- 📜 **View member borrowing history**: Track borrowing records for each member.
- 🔒 **Activate/deactivate memberships**: Manage membership statuses with ease.

### 🔄 Borrowing Operations
- 📘 **Record book borrowings and returns**: Streamline lending and returning processes.
- ⏳ **Extend borrowing periods**: Allow members to extend their borrowing duration.
- ⚠️ **Track overdue books and send reminders**: Ensure timely returns with automated notifications.

### 📊 Reporting & Analytics
- 📈 **Generate reports on popular books**: Identify trends and popular titles.
- 👤 **Member activity reports**: Analyze borrowing patterns and member engagement.
- 📦 **Inventory status reports**: Monitor stock levels and availability.
- ⏰ **Overdue books reports**: Stay informed about overdue items.

### 🔐 Administration
- 🔑 **User authentication and role-based access**: Secure the system with permissions and roles.
- ⚙️ **System configuration**: Customize borrowing periods, late fees, and other settings.
- 💾 **Database backup and restore**: Safeguard data with backup and recovery options.
- 🕵️ **Activity logging for audit trails**: Track system usage and changes for accountability.

---

### Why Choose LMS?
The Library Management System (LMS) is designed to be scalable, modular, and user-friendly. Whether you're managing a small library or a large institution, LMS provides the tools you need to streamline operations and enhance user experience.

---

## Project Structure
```
LMS/
│   main.py                  # Main application entry point
│   book_management.py       # Book management utilities
│   features.md              # Use case documentation
│   library.db               # SQLite database
│   test_book_management.py  # Unit tests
│   uml_diagram.md           # UML diagrams
│
├── controllers/
│   ├── book_controller.py
│   ├── database_controller.py
│   └── ...
├── models/
│   ├── book.py
│   ├── author.py
│   ├── category.py
│   ├── member.py
│   ├── borrowing.py
│   └── ...
├── views/
│   ├── book_view.py
│   ├── menu_view.py
│   └── ...
├── utils/
│   └── db_utils.py
└── README.md                # Project documentation
```

## Installation & Setup

Follow these steps to set up the Library Management System (LMS) on your local machine:

### 1. Clone the Repository
Clone the project repository from GitHub and navigate to the project directory:
```bash
git clone <repository-url>
cd LMS
```

### 2. Install Dependencies
Ensure Python 3.x is installed on your system. Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```
> **Note**: The `requirements.txt` file contains all necessary libraries for the application.

### 3. Initialize the Database
The SQLite database will be automatically initialized on the first run of the application. No manual setup is required.

### 4. Run the Application
Start the application by running the following command:
```bash
python main.py
```

> **Tip**: For development purposes, you can use a virtual environment to isolate dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

---

### Additional Notes:
- Ensure you have Git installed for cloning the repository.
- If you encounter issues with dependencies, verify your Python version and ensure compatibility with the libraries listed in `requirements.txt`.
- For database backups or migrations, refer to the `utils/db_utils.py` file for additional scripts.


## Technologies Used

- 🐍 **Python 3**: Core programming language for building the application.
- 🗄️ **SQLite**: Lightweight database for persistent storage of library data.
- 🏗️ **MVC Architectural Pattern**: Ensures separation of concerns and modular design.
- 🌐 **Flask**: (Optional) For future web-based interface development.
- 🧪 **Pytest**: Framework for writing and running unit tests.
- 🛠️ **Git**: Version control system for collaboration and code management.
- 📄 **Markdown**: Used for project documentation.

## Usage
- Interact with the system via the command-line interface.
- Navigate the main menu to access book, author, category, member, and borrowing management features.
- Generate reports and perform administrative tasks as needed.

## Extensibility
The LMS is designed for extensibility. New features, modules, or integrations (e.g., web interface, REST API) can be added with minimal changes to the core architecture.

## Documentation
- **features.md**: Detailed use cases and functional requirements
- **uml_diagram.md**: System architecture and class diagrams
- **test_book_management.py**: Example unit tests

## Feature Implementation Status

| **Feature**                 | **Status**              | **Notes**                                                                 |
|-----------------------------|-------------------------|---------------------------------------------------------------------------|
| **Book Management**         |                         |                                                                           |
| Add New Books               | ✅ Implemented          | Fonctionnalité entièrement opérationnelle dans `books.html`.             |
| Update Book Information     | ✅ Implemented          | Fonctionnalité opérationnelle avec un modal dans `books.html`.           |
| Remove Books                | ✅ Implemented          | Fonctionnalité opérationnelle avec un modal dans `books.html`.           |
| Search Books                | ⚠️ Partially implemented | Recherche basique disponible, mais les fonctionnalités avancées sont en attente. |
| View Book Details           | ✅ Implemented          | Modal pour afficher les détails du livre dans `books.html`.              |
| Manage Book Inventory       | ⚠️ Partially implemented | Gestion de la disponibilité et du stock partiellement implémentée.       |
| **Author Management**       |                         |                                                                           |
| Add New Authors             | ✅ Implemented (basic)  | Fonctionnalité basique disponible.                                       |
| Update Author Information   | ❌ To be completed      | Aucun formulaire ou modal trouvé pour cette fonctionnalité.              |
| View Author Bibliography    | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| **Category Management**     |                         |                                                                           |
| Add New Categories/Genres   | ✅ Implemented (basic)  | Fonctionnalité basique disponible.                                       |
| Update Category Information | ❌ To be completed      | Aucun formulaire ou modal trouvé pour cette fonctionnalité.              |
| Browse Books by Category    | ⚠️ Partially implemented | Recherche par catégorie disponible, mais pas entièrement fonctionnelle.  |
| **Member Management**       |                         |                                                                           |
| Register New Members         | ❌ To be completed      | Aucun formulaire ou modal trouvé pour cette fonctionnalité.              |
| Update Member Information    | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| View Member History          | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Manage Member Status         | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| **Borrowing Operations**    |                         |                                                                           |
| Borrow Books                | ❌ To be completed      | Aucun formulaire ou modal trouvé pour cette fonctionnalité.              |
| Return Books                | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Extend Borrowing Period     | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Track Overdue Books         | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Send Reminders              | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| **Reporting and Analytics** |                         |                                                                           |
| Popular Books Report        | ❌ To be completed      | Aucun tableau ou rapport trouvé pour cette fonctionnalité.               |
| Member Activity Report      | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Inventory Status Report     | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Overdue Books Report        | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| **Administration**          |                         |                                                                           |
| User Authentication         | ❌ To be completed      | Aucun système d'authentification trouvé dans le projet.                  |
| System Configuration        | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Database Backup/Restore     | ❌ To be completed      | Aucun script ou fonctionnalité trouvée pour cette tâche.                 |
| Activity Logging            | ❌ To be completed      | Fonctionnalité non implémentée.                                          |

---

### Legend:
- ✅ **Implemented**: Fully functional
- ⚠️ **Partially implemented**: Some features are functional, but improvements are pending
- ❌ **To be completed**: Not yet implemented

---

### Notes :
- Les fonctionnalités liées aux livres semblent être les plus avancées dans le projet.
- Les fonctionnalités liées aux membres, emprunts, et rapports nécessitent une implémentation complète.
- L'administration (authentification, configuration, sauvegarde) est absente et doit être ajoutée.

Si vous souhaitez des détails supplémentaires ou des suggestions pour prioriser les tâches, faites-le-moi savoir !## Feature Implementation Status

| **Feature**                 | **Status**              | **Notes**                                                                 |
|-----------------------------|-------------------------|---------------------------------------------------------------------------|
| **Book Management**         |                         |                                                                           |
| Add New Books               | ✅ Implemented          | Fonctionnalité entièrement opérationnelle dans `books.html`.             |
| Update Book Information     | ✅ Implemented          | Fonctionnalité opérationnelle avec un modal dans `books.html`.           |
| Remove Books                | ✅ Implemented          | Fonctionnalité opérationnelle avec un modal dans `books.html`.           |
| Search Books                | ⚠️ Partially implemented | Recherche basique disponible, mais les fonctionnalités avancées sont en attente. |
| View Book Details           | ✅ Implemented          | Modal pour afficher les détails du livre dans `books.html`.              |
| Manage Book Inventory       | ⚠️ Partially implemented | Gestion de la disponibilité et du stock partiellement implémentée.       |
| **Author Management**       |                         |                                                                           |
| Add New Authors             | ✅ Implemented (basic)  | Fonctionnalité basique disponible.                                       |
| Update Author Information   | ❌ To be completed      | Aucun formulaire ou modal trouvé pour cette fonctionnalité.              |
| View Author Bibliography    | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| **Category Management**     |                         |                                                                           |
| Add New Categories/Genres   | ✅ Implemented (basic)  | Fonctionnalité basique disponible.                                       |
| Update Category Information | ❌ To be completed      | Aucun formulaire ou modal trouvé pour cette fonctionnalité.              |
| Browse Books by Category    | ⚠️ Partially implemented | Recherche par catégorie disponible, mais pas entièrement fonctionnelle.  |
| **Member Management**       |                         |                                                                           |
| Register New Members         | ❌ To be completed      | Aucun formulaire ou modal trouvé pour cette fonctionnalité.              |
| Update Member Information    | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| View Member History          | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Manage Member Status         | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| **Borrowing Operations**    |                         |                                                                           |
| Borrow Books                | ❌ To be completed      | Aucun formulaire ou modal trouvé pour cette fonctionnalité.              |
| Return Books                | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Extend Borrowing Period     | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Track Overdue Books         | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Send Reminders              | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| **Reporting and Analytics** |                         |                                                                           |
| Popular Books Report        | ❌ To be completed      | Aucun tableau ou rapport trouvé pour cette fonctionnalité.               |
| Member Activity Report      | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Inventory Status Report     | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Overdue Books Report        | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| **Administration**          |                         |                                                                           |
| User Authentication         | ❌ To be completed      | Aucun système d'authentification trouvé dans le projet.                  |
| System Configuration        | ❌ To be completed      | Fonctionnalité non implémentée.                                          |
| Database Backup/Restore     | ❌ To be completed      | Aucun script ou fonctionnalité trouvée pour cette tâche.                 |
| Activity Logging            | ❌ To be completed      | Fonctionnalité non implémentée.                                          |

---

### Legend:
- ✅ **Implemented**: Fully functional
- ⚠️ **Partially implemented**: Some features are functional, but improvements are pending
- ❌ **To be completed**: Not yet implemented

---

---

### Legend:
- ✅ **Implemented**: Fully functional
- ⚠️ **Partially implemented**: Some features are functional, but improvements are pending
- ❌ **To be completed**: Not yet implemented

---

For a detailed description of each use case, see `features.md`.

## Authors & Contributors
- [@Hojgaetan](https://github.com/Hojgaetan) (Lead project)
- [@pmp-p](https://github.com/pmp-p)
- Contributors are welcome! Please see the `CONTRIBUTING.md` file for guidelines.

## License
This project is licensed under the **MIT License**, an open-source license that allows free use, modification, and distribution of the software. 

For more details, please refer to the `LICENSE` file included in the repository.