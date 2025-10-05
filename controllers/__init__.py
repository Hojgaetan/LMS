"""Package controllers
Expose les blueprints Flask pour enregistrement centralisé.
"""
from .book_controller import book_blueprint
from .member_controller import member_blueprint
from .author_controller import author_blueprint
from .category_controller import category_blueprint
from .dashboard_controller import dashboard_blueprint

__all__ = [
    "book_blueprint",
    "member_blueprint",
    "author_blueprint",
    "category_blueprint",
    "dashboard_blueprint",
]
