from flask import Flask, render_template, request, redirect, url_for, jsonify
from models.book import Book
from models.author import Author
from models.category import Category
from models.member import Member

app = Flask(__name__)

# Importer les blueprints
@app.route('/', methods=['GET'])
def index():
    try:
        # Récupérer les statistiques
        total_books = Book.count()
        total_category = Category.count()
        total_authors = Author.count()
        total_members = Member.count()
        total_popular_books = Book.count_popular_books(threshold=10)
        total_active_members = Member.count_active_members()
        total_overdue_books = Book.count_overdue_books()
        #popular_books = Book.get_popular_books(limit=5)
        #active_members = Member.get_active_members(limit=5)
        #overdue_books = Book.get_overdue_books()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    else:
        return render_template('index.html', 
                           total_books=total_books, 
                           total_category=total_category,
                           total_authors=total_authors, 
                           total_members=total_members,
                           total_popular_books=total_popular_books,
                           total_active_members= total_active_members,
                           total_overdue_books=total_overdue_books,
                           #popular_books=popular_books, 
                           #active_members=active_members, 
                           #overdue_books=overdue_books
                           )

if __name__ == '__main__':
    app.run(debug=True)
