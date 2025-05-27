# Library Management System (LMS)

![forks](https://img.shields.io/github/forks/Hojgaetan/LMS)
[![commits](https://img.shields.io/github/commit-activity/w/Hojgaetan/LMS)](https://github.com/Hojgaetan/LMS/commits/main)
![contributors](https://img.shields.io/github/contributors/Hojgaetan/LMS)

## Overview
The Library Management System (LMS) is a robust, modular application designed to streamline and automate the management of library resources. Built with a scalable architecture and following the Model-View-Controller (MVC) pattern, LMS provides a comprehensive suite of features for book, author, category, member, and borrowing management, as well as advanced reporting and administrative controls.

## Key Features
### Book Management
- Add, update, and remove books
- Search books by title
- View detailed book information
- Manage book inventory and availability

### Author & Category Management
- Register and update authors and categories
- View all books by a specific author or within a category

### Member Management
- Register, update, and manage library members
- View member borrowing history
- Activate/deactivate memberships

### Borrowing Operations
- Record book borrowings and returns
- Extend borrowing periods
- Track overdue books and send reminders

### Reporting & Analytics
- Generate reports on popular books, member activity, inventory status, and overdue books

### Administration
- User authentication and role-based access
- System configuration (borrowing period, late fees, etc.)
- Database backup and restore
- Activity logging for audit trails

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
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd LMS
   ```
2. **Install dependencies**
   - Python 3.x is required
   - (Optional) Install dependencies from requirements.txt if provided:
   ```bash
   pip install -r requirements.txt
   ```
3. **Initialize the database**
   - The database is automatically initialized on first run.

4. **Run the application**
   ```bash
   python main.py
   ```

## Technologies Used
- Python 3
- SQLite (for persistent storage)
- MVC architectural pattern

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

### Book Management
- **Add New Books**: Implemented
- **Update Book Information**: Implemented
- **Remove Books**: Implemented
- **Search Books**: Partially implemented
- **View Book Details**: Implemented
- **Manage Book Inventory**: Partially implemented (quantity/availability tracked, but advanced inventory features may be pending)

### Author Management
- **Add New Authors**: Implemented (basic)
- **Update Author Information**: To be completed
- **View Author Bibliography**: To be completed

### Category Management
- **Add New Categories/Genres**: Implemented (basic)
- **Update Category Information**: To be completed
- **Browse Books by Category**: Partially implemented (search by category available)

### Member Management
- **Register New Members**: To be completed
- **Update Member Information**: To be completed
- **View Member History**: To be completed
- **Manage Member Status**: To be completed

### Borrowing Operations
- **Borrow Books**: To be completed
- **Return Books**: To be completed
- **Extend Borrowing Period**: To be completed
- **Track Overdue Books**: To be completed
- **Send Reminders**: To be completed

### Reporting and Analytics
- **Popular Books Report**: To be completed
- **Member Activity Report**: To be completed
- **Inventory Status Report**: To be completed
- **Overdue Books Report**: To be completed

### Administration
- **User Authentication**: To be completed
- **System Configuration**: To be completed
- **Database Backup/Restore**: To be completed
- **Activity Logging**: To be completed

---

For a detailed description of each use case, see `features.md`.

## Authors & Contributors
- [@Hojgaetan](https://github.com/Hojgaetan) (Lead project)
- [@pmp-p](https://github.com/pmp-p)
- Contributors are welcome! Please see the CONTRIBUTING.md file for guidelines.

## License
This project is provided for educational and professional use. Please refer to the LICENSE file for more information.
