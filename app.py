from flask import Flask, render_template, request, redirect, url_for
from models.book import Book
from models.author import Author
from models.category import Category

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Récupérer tous les livres
    books = Book.search()
    # Récupérer les auteurs et catégories associés
    authors = {a.author_id: a.name for a in Author.all()}
    categories = {c.category_id: c.name for c in Category.all()}
    categories_list = list(categories.items())
    return render_template('index.html', books=books, authors=authors, categories=categories, categories_list=categories_list)

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

if __name__ == '__main__':
    app.run(debug=True)
