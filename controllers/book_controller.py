from flask import Blueprint, jsonify, request
from models.book import Book
from models.author import Author
from models.category import Category

book_blueprint = Blueprint('books', __name__)

@book_blueprint.route('/add', methods=['POST'])
def add_book():
    titre = request.form.get('titre')
    auteur_nom = request.form.get('auteur')
    categorie_id = request.form.get('categorie')
    isbn = request.form.get('isbn')
    publication_year = request.form.get('publication_year')
    publisher = request.form.get('publisher')
    quantite = request.form.get('quantity', type=int)

    auteur = Author.find_by_name(auteur_nom)
    if auteur:
        auteur_id = auteur[0].author_id if isinstance(auteur, list) else auteur.author_id
    else:
        new_auteur = Author(name=auteur_nom)
        new_auteur.save()
        auteur_id = new_auteur.author_id

    livre = Book(
        title=titre,
        author_id=auteur_id,
        category_id=categorie_id,
        isbn=isbn,
        publication_year=publication_year,
        publisher=publisher,
        quantity=quantite,
        available_quantity=quantite
    )
    livre.save()
    return jsonify({'success': True, 'message': 'Book added successfully'})

@book_blueprint.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    Book.delete(book_id)
    return jsonify({'success': True, 'message': 'Book deleted successfully'})

@book_blueprint.route('/update/<int:book_id>', methods=['POST'])
def update_book(book_id):
    book = Book.find_by_id(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    titre = request.form.get('titre')
    auteur_nom = request.form.get('auteur')
    categorie_id = request.form.get('categorie')
    isbn = request.form.get('isbn')
    publication_year = request.form.get('publication_year')
    publisher = request.form.get('publisher')
    quantite = request.form.get('quantity', type=int)

    auteur = Author.find_by_name(auteur_nom)
    if auteur:
        auteur_id = auteur[0].author_id if isinstance(auteur, list) else auteur.author_id
    else:
        new_auteur = Author(name=auteur_nom)
        new_auteur.save()
        auteur_id = new_auteur.author_id

    book.title = titre
    book.author_id = auteur_id
    book.category_id = categorie_id
    book.isbn = isbn
    book.publication_year = publication_year
    book.publisher = publisher
    book.quantity = quantite
    book.available_quantity = quantite
    book.save()

    return jsonify({'success': True, 'message': 'Book updated successfully'})

@book_blueprint.route('/details/<int:book_id>', methods=['GET'])
def book_details(book_id):
    book = Book.find_by_id(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    author = Author.find_by_id(book.author_id).name if book.author_id else ''
    category = Category.find_by_id(book.category_id).name if book.category_id else ''

    return jsonify({
        'title': book.title,
        'author': author,
        'category': category,
        'isbn': book.isbn,
        'publication_year': book.publication_year,
        'publisher': book.publisher,
        'quantity': book.quantity,
        'available_quantity': book.available_quantity
    })

@book_blueprint.route('/total-popular-books', methods=['GET'])
def total_popular_books():
    try:
        threshold = request.args.get('threshold', default=10, type=int)
        total_popular_books = Book.count_popular_books(threshold=threshold)
        return jsonify({'total_popular_books': total_popular_books})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@book_blueprint.route('/total-overdue-books', methods=['GET'])
def total_overdue_books():
    try:
        total_overdue_books = Book.count_overdue_books()
        return jsonify({'total_overdue_books': total_overdue_books})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
