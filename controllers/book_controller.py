from flask import Blueprint, jsonify, request
from services.book_service import BookService
from services.author_service import AuthorService
from services.category_service import CategoryService
import logging

logging.basicConfig(level=logging.DEBUG)

book_blueprint = Blueprint('books', __name__)

@book_blueprint.route('/add', methods=['POST'])
def add_book():
    data = request.json
    logging.debug(f"Received data: {data}")

    try:
        titre = data.get('title')
        auteur_nom = data.get('author')
        categorie_id = data.get('category')
        isbn = data.get('isbn')
        publication_year = data.get('publication_year')
        publisher = data.get('publisher')
        quantite = data.get('quantity')

        if not titre or not auteur_nom or not categorie_id:
            logging.error("Validation error: Missing required fields")
            return jsonify({'success': False, 'message': 'Missing required fields'}), 400

        auteur = AuthorService.search_authors_by_name(auteur_nom)
        logging.debug(f"Author search result: {auteur}")

        if not auteur:
            success, result = AuthorService.add_author(name=auteur_nom)
            logging.debug(f"Author creation result: success={success}, result={result}")
            if not success:
                logging.error(f"Author creation failed: {result}")
                return jsonify({'success': False, 'message': result}), 400
            auteur_id = result
        else:
            auteur_id = auteur[0].author_id if isinstance(auteur, list) else auteur.author_id

        success, result = BookService.add_book(
            title=titre,
            author_id=auteur_id,
            category_id=categorie_id,
            isbn=isbn,
            publication_year=publication_year,
            publisher=publisher,
            quantity=quantite
        )
        logging.debug(f"Book creation result: success={success}, result={result}")

        if success:
            return jsonify({'success': True, 'message': 'Book added successfully', 'book_id': result})
        else:
            logging.error(f"Book creation failed: {result}")
            return jsonify({'success': False, 'message': result}), 400

    except Exception as e:
        logging.exception("An unexpected error occurred")
        return jsonify({'success': False, 'message': str(e)}), 500

@book_blueprint.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    success, message = BookService.delete_book(book_id)
    if success:
        return jsonify({'success': True, 'message': message})
    else:
        return jsonify({'success': False, 'message': message}), 400

@book_blueprint.route('/update/<int:book_id>', methods=['POST'])
def update_book(book_id):
    book = BookService.get_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    titre = request.form.get('titre')
    auteur_nom = request.form.get('auteur')
    categorie_id = request.form.get('categorie')
    isbn = request.form.get('isbn')
    publication_year = request.form.get('publication_year')
    publisher = request.form.get('publisher')
    quantite = request.form.get('quantity', type=int)

    auteur = AuthorService.search_authors_by_name(auteur_nom)
    if not auteur:
        success, result = AuthorService.add_author(name=auteur_nom)
        if not success:
            return jsonify({'success': False, 'message': result}), 400
        auteur_id = result
    else:
        auteur_id = auteur[0].author_id if isinstance(auteur, list) else auteur.author_id

    success, result = BookService.update_book(
        book_id,
        title=titre,
        author_id=auteur_id,
        category_id=categorie_id,
        isbn=isbn,
        publication_year=publication_year,
        publisher=publisher,
        quantity=quantite,
        available_quantity=quantite
    )

    if success:
        return jsonify({'success': True, 'message': 'Book updated successfully'})
    else:
        return jsonify({'success': False, 'message': result}), 400

@book_blueprint.route('/details/<int:book_id>', methods=['GET'])
def book_details(book_id):
    book = BookService.get_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    author = AuthorService.get_author(book.author_id).name if book.author_id else ''
    category = CategoryService.get_category(book.category_id).name if book.category_id else ''

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
        total_popular_books = BookService.count_popular_books(threshold=threshold)
        return jsonify({'total_popular_books': total_popular_books})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@book_blueprint.route('/total-overdue-books', methods=['GET'])
def total_overdue_books():
    try:
        total_overdue_books = BookService.count_overdue_books()
        return jsonify({'total_overdue_books': total_overdue_books})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@book_blueprint.route('/books', methods=['GET'])
def get_books():
    try:
        books = BookService.get_all_books()
        books_data = []
        for book in books:
            books_data.append({
                'id': book.book_id,
                'title': book.title,
                'author': AuthorService.get_author(book.author_id).name if book.author_id else '',
                'category': CategoryService.get_category(book.category_id).name if book.category_id else '',
                'isbn': book.isbn,
                'publication_year': book.publication_year,
                'publisher': book.publisher,
                'quantity': book.quantity,
                'available_quantity': book.available_quantity
            })
        return jsonify({'books': books_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


