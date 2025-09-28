# Guide de Développement - LMS

Ce guide vous aidera à configurer votre environnement de développement pour contribuer au projet LMS.

## 🚀 Configuration Rapide

### Prérequis
- Python 3.10 ou supérieur
- Git
- Un éditeur de code (VS Code, PyCharm, etc.)

### Installation

1. **Cloner le projet**
```bash
git clone https://github.com/Hojgaetan/LMS.git
cd LMS
```

2. **Créer et activer l'environnement virtuel**

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Initialiser la base de données**
```bash
python -c "from services.database_service import DatabaseService; DatabaseService.initialize_database()"
```

5. **Lancer l'application**

**Mode Web:**
```bash
python app.py
```
Puis ouvrir http://127.0.0.1:5000/

**Mode CLI:**
```bash
python main.py
```

## 🧪 Tests

### Lancer les tests
```bash
pytest
```

### Lancer les tests avec couverture
```bash
pytest --cov=. --cov-report=html
```

### Lancer des tests spécifiques
```bash
pytest test_member_service.py
pytest -k "test_add_member"
```

## 🔧 Structure des Branches

### Convention de nommage
- `feature/nom-de-la-fonctionnalité` - Nouvelles fonctionnalités
- `fix/description-du-bug` - Corrections de bugs
- `docs/sujet-documentation` - Modifications de documentation
- `refactor/nom-du-refactoring` - Refactoring de code
- `test/nom-des-tests` - Ajout de tests

### Workflow Git
```bash
# Créer une nouvelle branche
git checkout -b feature/ma-nouvelle-fonctionnalite

# Faire vos changements et les commiter
git add .
git commit -m "feat: ajouter fonctionnalité X"

# Pousser la branche
git push origin feature/ma-nouvelle-fonctionnalite

# Créer une Pull Request sur GitHub
```

## 📝 Conventions de Code

### Python (PEP 8)
- Indentation: 4 espaces
- Longueur de ligne: 88 caractères (Black formatter)
- Noms de variables: `snake_case`
- Noms de classes: `PascalCase`
- Noms de constantes: `UPPER_CASE`

### Messages de Commit
Utilisez le format [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

feat: ajouter fonctionnalité de recherche de membres
fix: corriger le bug de validation d'email
docs: mettre à jour le README
style: formater le code selon PEP 8
refactor: restructurer le service de membres
test: ajouter tests pour MemberService
```

Types courants:
- `feat`: nouvelle fonctionnalité
- `fix`: correction de bug
- `docs`: documentation
- `style`: formatage
- `refactor`: refactoring
- `test`: tests
- `chore`: maintenance

## 🗂️ Architecture du Projet

```
LMS/
├── controllers/          # Routes Flask et logique de contrôleur
├── models/              # Modèles de données et logique métier
├── services/            # Logique métier et accès aux données
├── views/               # Vues pour l'interface CLI
├── templates/           # Templates HTML pour Flask
├── static/              # Fichiers statiques (CSS, JS, images)
├── utils/               # Utilitaires et helpers
└── tests/               # Tests unitaires et d'intégration
```

### Pattern MVC
- **Models**: Définissent la structure des données et les règles métier
- **Views**: Gèrent l'affichage et l'interaction utilisateur
- **Controllers**: Coordonnent les models et views, gèrent les routes

## 🛠️ Outils de Développement

### Formatage de Code
```bash
# Installer Black (optionnel)
pip install black

# Formater le code
black .
```

### Linting
```bash
# Installer flake8 (optionnel)
pip install flake8

# Vérifier le style
flake8 .
```

### Extensions VS Code Recommandées
- Python
- Python Docstring Generator
- GitLens
- Auto Rename Tag
- Bracket Pair Colorizer

## 🐛 Débogage

### Logs de débogage
L'application utilise des `print()` pour le débogage (à remplacer par un système de logging).

### Base de données
Pour réinitialiser la base de données:
```bash
python -c "from services.database_service import DatabaseService; DatabaseService.reset_database()"
```

### Problèmes courants

**Port déjà utilisé (Flask):**
```bash
# Changer le port
export FLASK_RUN_PORT=5001  # Linux/macOS
set FLASK_RUN_PORT=5001     # Windows
python app.py
```

**Modules non trouvés:**
Vérifiez que l'environnement virtuel est activé:
```bash
which python  # Linux/macOS
where python  # Windows
```

**Erreurs de base de données:**
Supprimez `library.db` et réinitialisez:
```bash
rm library.db  # Linux/macOS
del library.db # Windows
python -c "from services.database_service import DatabaseService; DatabaseService.initialize_database()"
```

## 📚 Ressources Utiles

### Documentation
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/)
- [Python PEP 8 Style Guide](https://pep8.org/)

### Tutoriels
- [Git Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows)
- [Python Testing with pytest](https://docs.pytest.org/en/stable/)
- [Flask Tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/)

## 🤝 Contribution

1. Consultez [GOOD_FIRST_ISSUES.md](GOOD_FIRST_ISSUES.md) pour des tâches adaptées aux débutants
2. Lisez [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines détaillées
3. Utilisez les templates d'issues et de PR dans `.github/`
4. N'hésitez pas à poser des questions dans les discussions

## 🎉 Merci de Contribuer !

Votre contribution, qu'elle soit petite ou grande, est précieuse pour la communauté LMS. Ensemble, nous construisons un meilleur système de gestion de bibliothèque !

---

**Besoin d'aide ?** Ouvrez une issue ou démarrez une discussion sur GitHub.