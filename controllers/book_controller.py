from flask import Blueprint, jsonify, request
from services.book_service import BookService
from services.author_service import AuthorService
from services.category_service import CategoryService
import logging

logging.basicConfig(level=logging.DEBUG)

book_blueprint = Blueprint('books', __name__)

@book_blueprint.route('/add', methods=['POST'])
def add_book():
    try:
        data = request.json
        logging.debug(f"Received data: {data}")

        # Validation des champs requis
        required_fields = ['title', 'author', 'category', 'isbn', 'publication_year', 'publisher', 'quantity']
        missing_fields = [field for field in required_fields if not data.get(field)]
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Champs manquants: {", ".join(missing_fields)}'
            }), 400

        # Récupération des données
        titre = data.get('title')
        auteur_nom = data.get('author')
        categorie_nom = data.get('category')  # On reçoit le nom de la catégorie
        isbn = data.get('isbn')
        publication_year = data.get('publication_year')
        publisher = data.get('publisher')
        quantite = data.get('quantity')

        # Vérification de l'auteur
        auteur = AuthorService.search_authors_by_name(auteur_nom)
        if not auteur:
            success, result = AuthorService.add_author(name=auteur_nom)
            if not success:
                return jsonify({
                    'success': False,
                    'message': f'Erreur lors de la création de l\'auteur: {result}'
                }), 400
            auteur_id = result
        else:
            auteur_id = auteur[0].author_id if isinstance(auteur, list) else auteur.author_id

        # Vérification de la catégorie
        categorie = CategoryService.get_category_by_name(categorie_nom)
        if not categorie:
            success, result = CategoryService.add_category(name=categorie_nom)
            if not success:
                return jsonify({
                    'success': False,
                    'message': f'Erreur lors de la création de la catégorie: {result}'
                }), 400
            categorie_id = result
        else:
            categorie_id = categorie.category_id

        # Ajout du livre
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
            return jsonify({
                'success': True,
                'message': 'Livre ajouté avec succès',
                'book_id': result
            }), 201
        else:
            return jsonify({
                'success': False,
                'message': f'Erreur lors de l\'ajout du livre: {result}'
            }), 400

    except Exception as e:
        logging.exception("Une erreur inattendue s'est produite")
        return jsonify({
            'success': False,
            'message': f'Erreur serveur: {str(e)}'
        }), 500

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


