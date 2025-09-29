from flask import Blueprint, jsonify, request, render_template
from services.book_service import BookService
from services.author_service import AuthorService
from services.category_service import CategoryService
import logging

logging.basicConfig(level=logging.DEBUG)

book_blueprint = Blueprint('books', __name__)

# Nouvelle route pour afficher la page livres avec les catégories
@book_blueprint.route('/', methods=['GET'])
def books_page():
    try:
        books = BookService.get_all_books()
        books_data = []
        for book in books:
            author_name = AuthorService.get_author_name(book.author_id) if book.author_id else ''
            category_name = CategoryService.get_category_name(book.category_id) if book.category_id else ''
            books_data.append({
                'id': book.book_id,
                'title': book.title,
                'author': author_name or '',
                'category': category_name or '',
                'isbn': book.isbn,
                'publication_year': book.publication_year,
                'publisher': book.publisher,
                'quantity': book.quantity,
                'available_quantity': book.available_quantity
            })
        categories = CategoryService.list_categories()
        total_books = BookService.count_books()
        # Seuil par défaut pour livres populaires (peut être changé si besoin via query param plus tard)
        total_popular_books = BookService.count_popular_books(threshold=10)
        return render_template('books.html', books=books_data, categories=categories, total_books=total_books, total_popular_books=total_popular_books)
    except Exception as e:
        logging.exception("Erreur lors de l'affichage de la page livres")
        # Fallback JSON si problème de rendu
        return jsonify({'error': str(e)}), 500

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

@book_blueprint.route('/delete', methods=['POST'])
def delete_book():
    try:
        data = request.get_json()
        if not data or 'book_id' not in data:
            return jsonify({
                'success': False,
                'message': 'ID du livre manquant dans la requête'
            }), 400

        book_id = data['book_id']
        
        # Vérifier si le livre existe
        book = BookService.get_book(book_id)
        if not book:
            return jsonify({
                'success': False,
                'message': f'Livre avec ID {book_id} non trouvé'
            }), 404

        # Tenter la suppression
        success, message = BookService.delete_book(book_id)
        
        if success:
            return jsonify({
                'success': True,
                'message': message
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': message
            }), 400

    except Exception as e:
        logging.exception("Erreur lors de la suppression du livre")
        return jsonify({
            'success': False,
            'message': f'Erreur serveur: {str(e)}'
        }), 500

@book_blueprint.route('/edit', methods=['POST'])
def update_book():
    try:
        data = request.json
        logging.debug(f"Received data for update: {data}")

        # Validate required fields
        required_fields = ['title', 'author', 'category', 'isbn', 'publication_year', 'publisher', 'quantity']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Missing fields: {", ".join(missing_fields)}'
            }), 400

        # Extract data
        book_id = data.get('id')
        title = data.get('title')
        author_name = data.get('author')
        category_name = data.get('category')
        isbn = data.get('isbn')
        publication_year = data.get('publication_year')
        publisher = data.get('publisher')
        quantity = data.get('quantity')

        # Validate author
        author = AuthorService.search_authors_by_name(author_name)
        if not author:
            success, author_id = AuthorService.add_author(name=author_name)
            if not success:
                return jsonify({
                    'success': False,
                    'message': f'Error adding author: {author_id}'
                }), 400
        else:
            author_id = author[0].author_id if isinstance(author, list) else author.author_id

        # Validate category
        category = CategoryService.get_category_by_name(category_name)
        if not category:
            success, category_id = CategoryService.add_category(name=category_name)
            if not success:
                return jsonify({
                    'success': False,
                    'message': f'Error adding category: {category_id}'
                }), 400
        else:
            category_id = category.category_id

        # Update book
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
            return jsonify({
                'success': True,
                'message': 'Book updated successfully',
                'book_id': result
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': result
            }), 400

    except Exception as e:
        logging.exception("An unexpected error occurred during book update")
        return jsonify({
            'success': False,
            'message': f'Server error: {str(e)}'
        }), 500

@book_blueprint.route('/details/<int:book_id>', methods=['GET'])
def book_details(book_id):
    book = BookService.get_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    author = AuthorService.get_author_name(book.author_id) if book.author_id else ''
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
        category_name = request.args.get('category')
        if category_name:
            category = CategoryService.get_category_by_name(category_name)
            if category:
                books = BookService.search_books(category_id=category.category_id)
            else:
                books = []
        else:
            books = BookService.get_all_books()
        books_data = []
        for book in books:
            author_name = AuthorService.get_author_name(book.author_id) if book.author_id else ''
            category_name = CategoryService.get_category_name(book.category_id) if book.category_id else ''
            books_data.append({
                'id': book.book_id,
                'title': book.title,
                'author': author_name or '',
                'category': category_name or '',
                'isbn': book.isbn,
                'publication_year': book.publication_year,
                'publisher': book.publisher,
                'quantity': book.quantity,
                'available_quantity': book.available_quantity
            })
        return jsonify({'books': books_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@book_blueprint.route('/api', methods=['GET'])
def api_books():
    """Endpoint API utilisé par le filtre dynamique (front) pour récupérer les livres éventuellement filtrés par catégorie."""
    try:
        category_name = request.args.get('category')
        if category_name:
            category = CategoryService.get_category_by_name(category_name)
            if category:
                books = BookService.search_books(category_id=category.category_id)
            else:
                books = []
        else:
            books = BookService.get_all_books()
        books_data = []
        for book in books:
            author_name = AuthorService.get_author_name(book.author_id) if book.author_id else ''
            category_label = CategoryService.get_category_name(book.category_id) if book.category_id else ''
            books_data.append({
                'id': book.book_id,
                'title': book.title,
                'author': author_name or '',
                'category': category_label or '',
                'isbn': book.isbn,
                'publication_year': book.publication_year,
                'publisher': book.publisher,
                'quantity': book.quantity,
                'available_quantity': book.available_quantity
            })
        return jsonify({'books': books_data})
    except Exception as e:
        logging.exception('Erreur API /books/api')
        return jsonify({'error': str(e)}), 500

@book_blueprint.route('/total-books', methods=['GET'])
def total_books():
    try:
        total_books = BookService.count_books()
        return jsonify({'total_books': total_books})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
