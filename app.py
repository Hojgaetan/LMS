from flask import Flask, render_template, request, redirect, url_for, jsonify
from models.book import Book
from models.author import Author
from models.category import Category

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Récupérer filtres de recherche
    titre = request.args.get('title')
    auteur_id = request.args.get('author', type=int)
    categorie_id = request.args.get('category', type=int)
    

    # Récupérer tous les livres selon filtres
    books = Book.search(title=titre, author_id=auteur_id, category_id=categorie_id)
    # Récupérer les auteurs et catégories associés
    authors = {a.author_id: a.name for a in Author.all()}
    categories = {c.category_id: c.name for c in Category.all()}
    categories_list = list(categories.items())
    return render_template('index.html', books=books, authors=authors, categories=categories,
                           categories_list=categories_list,
                           title_filter=titre, author_filter=auteur_id,
                           category_filter=categorie_id)

@app.route('/ajouter-livre', methods=['POST'])
def ajouter_livre():
    titre = request.form.get('titre')
    auteur_nom = request.form.get('auteur')
    categorie_id = request.form.get('categorie')
    isbn = request.form.get('isbn')
    publication_year = request.form.get('publication_year')
    publisher = request.form.get('publisher')
    quantite = request.form.get('quantity', type=int)

    # Chercher ou créer l'auteur
    auteur = Author.find_by_name(auteur_nom)
    if auteur:
        auteur_id = auteur[0].author_id if isinstance(auteur, list) else auteur.author_id
    else:
        new_auteur = Author(name=auteur_nom)
        new_auteur.save()
        auteur_id = new_auteur.author_id

    # Créer le livre avec tous les champs
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
    return redirect(url_for('index'))

@app.route('/supprimer-livre/<int:book_id>', methods=['POST'])
def supprimer_livre(book_id):
    Book.delete(book_id)
    return redirect(url_for('index'))

@app.route('/modifier-livre/<int:book_id>', methods=['GET', 'POST'])
def modifier_livre(book_id):
    book = Book.find_by_id(book_id)
    if not book:
        return redirect(url_for('index'))
    if request.method == 'POST':
        titre = request.form.get('titre')
        auteur_nom = request.form.get('auteur')
        categorie_id = request.form.get('categorie')
        isbn = request.form.get('isbn')
        publication_year = request.form.get('publication_year')
        publisher = request.form.get('publisher')
        quantite = request.form.get('quantity', type=int)
        # Chercher ou créer l'auteur
        auteur = Author.find_by_name(auteur_nom)
        if auteur:
            auteur_id = auteur[0].author_id if isinstance(auteur, list) else auteur.author_id
        else:
            new_auteur = Author(name=auteur_nom)
            new_auteur.save()
            auteur_id = new_auteur.author_id
        # Mise à jour du livre
        book.title = titre
        book.author_id = auteur_id
        book.category_id = categorie_id
        book.isbn = isbn
        book.publication_year = publication_year
        book.publisher = publisher
        book.quantity = quantite
        book.available_quantity = quantite
        book.save()
        return redirect(url_for('index'))
    # GET : renvoyer les infos du livre en JSON pour le formulaire pop-up
    return jsonify({
        'titre': book.title,
        'auteur': Author.find_by_id(book.author_id).name if book.author_id else '',
        'categorie': book.category_id,
        'isbn': book.isbn,
        'publication_year': book.publication_year,
        'publisher': book.publisher,
        'quantity': book.quantity
    })

@app.route('/details-livre/<int:book_id>', methods=['GET'])
def details_livre(book_id):
    book = Book.find_by_id(book_id)
    if not book:
        return jsonify({'error': 'Livre non trouvé'}), 404
    author = Author.find_by_id(book.author_id).name if book.author_id else ''
    category = Category.find_by_id(book.category_id).name if book.category_id else ''
    return jsonify({
        'titre': book.title,
        'auteur': author,
        'categorie': category,
        'isbn': book.isbn,
        'publication_year': book.publication_year,
        'publisher': book.publisher,
        'quantity': book.quantity,
        'available_quantity': book.available_quantity
    })

if __name__ == '__main__':
    app.run(debug=True)
