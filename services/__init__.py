"""Aggregation des services pour des imports stables.

Usage recommandé dans les controllers :
    from services import BookService, AuthorService

Cela limite le risque d'import circulaire et centralise l'API publique.
"""

from .book_service import BookService
from .author_service import AuthorService
from .category_service import CategoryService
from .member_service import MemberService
from .borrowing_service import BorrowingService
from .dashboard_service import DashboardService
from .admin_service import AdminService
from .database_service import DatabaseService

__all__ = [
    "BookService",
    "AuthorService",
    "CategoryService",
    "MemberService",
    "BorrowingService",
    "DashboardService",
    "AdminService",
    "DatabaseService",
]

