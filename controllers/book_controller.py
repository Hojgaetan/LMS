from flask import Blueprint, jsonify, request
from services import BookService, AuthorService, CategoryService
import logging

logging.basicConfig(level=logging.DEBUG)

book_blueprint = Blueprint('books', __name__)

@book_blueprint.route('/add', methods=['POST'])
def add_book():
    try:
        data = request.json or {}
        logging.debug(f"Received data: {data}")

        required_fields = ['title', 'author', 'category', 'isbn', 'publication_year', 'publisher', 'quantity']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({'success': False,'message': f'Champs manquants: {", ".join(missing_fields)}'}), 400

        titre = data.get('title')
        auteur_nom = data.get('author')
        categorie_nom = data.get('category')
        isbn = data.get('isbn')
        publication_year = data.get('publication_year')
        publisher = data.get('publisher')
        quantite = data.get('quantity')

        # Auteur (get_or_create)
        a_ok, auteur_id_or_msg = AuthorService.get_or_create_author(auteur_nom)
        if not a_ok:
            return jsonify({'success': False,'message': f"Erreur auteur: {auteur_id_or_msg}"}), 400
        auteur_id = auteur_id_or_msg

        # Catégorie (get_or_create)
        c_ok, categorie_id_or_msg = CategoryService.get_or_create_category(categorie_nom)
        if not c_ok:
            return jsonify({'success': False,'message': f"Erreur catégorie: {categorie_id_or_msg}"}), 400
        categorie_id = categorie_id_or_msg

        success, result = BookService.add_book(
            title=titre,
            author_id=auteur_id,
            category_id=categorie_id,
            isbn=isbn,
            publication_year=publication_year,
            publisher=publisher,
            quantity=quantite
        )

        if success:
            return jsonify({'success': True,'message': 'Livre ajouté avec succès','book_id': result}), 201
        return jsonify({'success': False,'message': f"Erreur lors de l'ajout du livre: {result}"}), 400

    except Exception as e:
        logging.exception("Une erreur inattendue s'est produite")
        return jsonify({'success': False,'message': f'Erreur serveur: {str(e)}'}), 500

@book_blueprint.route('/delete', methods=['POST'])
def delete_book():
    try:
        data = request.get_json() or {}
        if 'book_id' not in data:
            return jsonify({'success': False,'message': 'ID du livre manquant dans la requête'}), 400
        book_id = data['book_id']
        book = BookService.get_book(book_id)
        if not book:
            return jsonify({'success': False,'message': f'Livre avec ID {book_id} non trouvé'}), 404
        success, message = BookService.delete_book(book_id)
        if success:
            return jsonify({'success': True,'message': message}), 200
        return jsonify({'success': False,'message': message}), 400
    except Exception as e:
        logging.exception("Erreur lors de la suppression du livre")
        return jsonify({'success': False,'message': f'Erreur serveur: {str(e)}'}), 500

@book_blueprint.route('/edit', methods=['POST'])
def update_book():
    try:
        data = request.json or {}
        logging.debug(f"Received data for update: {data}")
        required_fields = ['id','title', 'author', 'category', 'isbn', 'publication_year', 'publisher', 'quantity']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({'success': False,'message': f'Missing fields: {", ".join(missing_fields)}'}), 400

        book_id = data.get('id')
        title = data.get('title')
        author_name = data.get('author')
        category_name = data.get('category')
        isbn = data.get('isbn')
        publication_year = data.get('publication_year')
        publisher = data.get('publisher')
        quantity = data.get('quantity')

        a_ok, author_id_or_msg = AuthorService.get_or_create_author(author_name)
        if not a_ok:
            return jsonify({'success': False,'message': f'Error adding author: {author_id_or_msg}'}), 400
        author_id = author_id_or_msg

        c_ok, category_id_or_msg = CategoryService.get_or_create_category(category_name)
        if not c_ok:
            return jsonify({'success': False,'message': f'Error adding category: {category_id_or_msg}'}), 400
        category_id = category_id_or_msg

        success, result = BookService.update_book(
            book_id=book_id,
            title=title,
            author_id=author_id,
            category_id=category_id,
            isbn=isbn,
            publication_year=publication_year,
            publisher=publisher,
            quantity=quantity
        )
        if success:
            return jsonify({'success': True,'message': 'Book updated successfully','book_id': result}), 200
        return jsonify({'success': False,'message': result}), 400
    except Exception as e:
        logging.exception("An unexpected error occurred during book update")
        return jsonify({'success': False,'message': f'Server error: {str(e)}'}), 500

@book_blueprint.route('/details/<int:book_id>', methods=['GET'])
def book_details(book_id):
    book = BookService.get_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    author = AuthorService.get_author(book.author_id).name if book.author_id else ''
    category = CategoryService.get_category_name(book.category_id) if book.category_id else ''
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
                'category': CategoryService.get_category_name(book.category_id) if book.category_id else '',
                'isbn': book.isbn,
                'publication_year': book.publication_year,
                'publisher': book.publisher,
                'quantity': book.quantity,
                'available_quantity': book.available_quantity
            })
        return jsonify({'books': books_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@book_blueprint.route('/total-books', methods=['GET'])
def total_books():
    try:
        total_books = BookService.count_books()
        return jsonify({'total_books': total_books})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
