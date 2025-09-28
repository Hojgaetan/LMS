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
│  app.py                   # Flask app entrypoint (web UI)
│  main.py                  # CLI entrypoint
│  book_management.py       # Book management utilities
│  features.md              # Use case documentation
│  library.db               # SQLite database (generated)
│  uml_diagram.md           # UML diagrams
│  requirements.txt         # Python dependencies
│
├─ controllers/
│  ├─ book_controller.py
│  ├─ member_controller.py
│  ├─ dashboard_controller.py
│  ├─ database_controller.py
│  └─ ...
├─ services/
│  ├─ book_service.py
│  ├─ member_service.py
│  ├─ category_service.py
│  ├─ author_service.py
│  ├─ borrowing_service.py
│  ├─ dashboard_service.py
│  └─ database_service.py
├─ models/
│  ├─ book.py
│  ├─ author.py
│  ├─ category.py
│  ├─ member.py
│  ├─ borrowing.py
│  └─ base_model.py
├─ templates/               # HTML templates for Flask views
│  ├─ index.html
│  ├─ books.html
│  ├─ members.html
│  ├─ loans.html
│  └─ ...
├─ static/
│  ├─ css/
│  └─ js/
├─ views/
│  ├─ menu_view.py
│  ├─ book_view.py
│  └─ ...
└─ utils/
   └─ db_utils.py
```

## Installation & Setup (Windows / cmd.exe)

Suivez ces étapes pour installer et lancer LMS en local.

1) Cloner le dépôt
```
git clone https://github.com/Hojgaetan/LMS.git
cd LMS
```

2) Créer un environnement virtuel et l’activer
```
python -m venv venv
venv\Scripts\activate
```

3) Installer les dépendances
```
pip install -r requirements.txt
```

4) Initialiser la base de données (première utilisation)
- Cette étape crée les tables et insère des données d’exemple si la base n’existe pas encore.
```
python -c "from services.database_service import DatabaseService; DatabaseService.initialize_database()"
```
- Pour réinitialiser complètement la base (attention: suppression des données), exécutez:
```
python -c "from services.database_service import DatabaseService; DatabaseService.reset_database()"
```

5) Lancer l’application
- Mode Web (Flask):
```
python app.py
```
Puis ouvrez http://127.0.0.1:5000/ dans votre navigateur.

- Mode CLI (terminal):
```
python main.py
```

---

### Conseils
- Assurez-vous d’utiliser Python 3.10+.
- Si vous mettez à jour des dépendances, relancez l’installation: `pip install -r requirements.txt`.
- Le fichier `library.db` est créé à la racine du projet.

### Dépannage
- Port déjà utilisé pour Flask: changez de port en lançant `python app.py` après avoir défini la variable d’environnement `set FLASK_RUN_PORT=5050` et adaptez l’URL, ou modifiez l’appel `app.run()`.
- Problèmes de base de données: utilisez la commande de réinitialisation ci-dessus.
- En cas d’erreur de modules manquants, vérifiez l’activation de l’environnement virtuel.

## Technologies Used
- 🐍 **Python 3**: Core programming language for building the application.
- 🗄️ **SQLite**: Lightweight database for persistent storage of library data.
- 🏗️ **MVC Architectural Pattern**: Ensures separation of concerns and modular design.
- 🌐 **Flask**: Web interface (blueprints, templates, static assets).
- 🧪 **Pytest**: (optionnel) Framework pour exécuter des tests unitaires si présents.
- 🛠️ **Git**: Version control system for collaboration and code management.
- 📄 **Markdown**: Used for project documentation.

## Usage
- Via l’interface Web: naviguez entre le tableau de bord, les livres, les membres et les prêts.
- Via le CLI: utilisez le menu principal pour gérer livres, auteurs, catégories, membres et emprunts.

## Documentation
- **uml_diagram.md**: System architecture and class diagrams

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

For a detailed description of each use case, see `README.md`.

## Authors & Contributors
- [@Hojgaetan](https://github.com/Hojgaetan) (Lead project)
- [@pmp-p](https://github.com/pmp-p)
- Contributors are welcome! Please see the `CONTRIBUTING.md` file for guidelines.

### 🚀 Nouveau Contributeur ?
Consultez notre guide [**GOOD_FIRST_ISSUES.md**](GOOD_FIRST_ISSUES.md) qui propose des issues parfaites pour débuter et vous familiariser avec le projet !

### 📖 Guides de Contribution
- 📋 [**GOOD_FIRST_ISSUES.md**](GOOD_FIRST_ISSUES.md) - Issues pour nouveaux contributeurs
- 🤝 [**CONTRIBUTING.md**](CONTRIBUTING.md) - Guide de contribution complet  
- 🛠️ [**DEVELOPMENT.md**](DEVELOPMENT.md) - Configuration de l'environnement de développement

## License
This project is licensed under the **MIT License**, an open-source license that allows free use, modification, and distribution of the software. 

For more details, please refer to the `LICENSE` file included in the repository.