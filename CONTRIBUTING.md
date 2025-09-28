# Contributing to Library Management System (LMS)

Merci de considérer contribuer au Library Management System (LMS) ! Les contributions sont les bienvenues et grandement appréciées. Ce document présente les guidelines pour contribuer au projet.

---

## 🚀 Démarrage Rapide

### Nouveau Contributeur ?
1. 📖 **Lisez d'abord:** [GOOD_FIRST_ISSUES.md](GOOD_FIRST_ISSUES.md) - Liste d'issues parfaites pour débuter
2. 🛠️ **Configuration:** [DEVELOPMENT.md](DEVELOPMENT.md) - Guide complet pour configurer votre environnement
3. 💬 **Questions ?** Ouvrez une discussion ou commentez une issue

### Contributeur Expérimenté ?
- Consultez les issues ouvertes marquées `help wanted`
- Proposez de nouvelles fonctionnalités via les templates d'issues
- Aidez à reviewer les PRs d'autres contributeurs

---

## Comment Contribuer

### 1. Choisir une Tâche
- 🟢 **Débutant :** Consultez [GOOD_FIRST_ISSUES.md](GOOD_FIRST_ISSUES.md)
- 🟡 **Intermédiaire :** Issues marquées `enhancement` ou `bug`
- 🔴 **Avancé :** Issues marquées `complex` ou architecture

### 2. Fork et Clone
```bash
git clone <your-forked-repository-url>
cd LMS
```

### 3. Configuration de l'Environnement
Suivez le guide détaillé dans [DEVELOPMENT.md](DEVELOPMENT.md)

### 4. Créer une Branche
```bash
git checkout -b feature/nom-descriptif
# ou
git checkout -b fix/description-bug
```

### 5. Développer
- Implémentez vos changements
- Suivez les conventions de code (voir DEVELOPMENT.md)
- Écrivez ou mettez à jour les tests
- Testez localement

### 6. Commit et Push
```bash
git add .
git commit -m "feat: description de votre changement"
git push origin feature/nom-descriptif
```

### 7. Créer une Pull Request
- Utilisez le template de PR fourni
- Décrivez clairement vos changements
- Liez l'issue correspondante

---

## 📋 Guidelines de Contribution

### Standards de Code
- Suivez le style Python PEP 8
- Utilisez des noms de variables et fonctions significatifs
- Commentez le code complexe
- Respectez la structure MVC du projet

### Tests
- Ajoutez des tests pour toute nouvelle fonctionnalité
- Assurez-vous que tous les tests existants passent :
```bash
pytest
```
- Visez une couverture de code d'au moins 80%

### Documentation
- Mettez à jour le `README.md` si vos changements affectent les fonctionnalités
- Ajoutez des commentaires dans votre code pour plus de clarté
- Mettez à jour la documentation technique si nécessaire

### Messages de Commit
Utilisez le format [Conventional Commits](https://www.conventionalcommits.org/) :
```
type(scope): description

Exemples :
feat: ajouter fonctionnalité de recherche de membres
fix: corriger le bug de validation d'email
docs: mettre à jour le guide d'installation
style: formater le code selon PEP 8
test: ajouter tests pour MemberService
```

---

## 🎯 Domaines de Contribution

### 💻 Développement de Fonctionnalités
- Implémentez les fonctionnalités manquantes (voir README.md)
- Améliorez les fonctionnalités existantes
- Optimisez les performances

### 🐛 Correction de Bugs
- Identifiez et corrigez les bugs signalés dans les issues
- Améliorez la gestion d'erreurs
- Renforcez la validation des données

### 📚 Documentation
- Améliorez la documentation du projet
- Ajoutez des exemples d'utilisation
- Créez des tutoriels pour les utilisateurs

### 🧪 Tests et Qualité
- Ajoutez des tests unitaires et d'intégration
- Améliorez la couverture de code
- Refactorisez le code pour une meilleure maintenabilité

### 🎨 Interface Utilisateur
- Améliorez l'expérience utilisateur
- Optimisez l'accessibilité
- Modernisez le design

---

## 🏷️ Types d'Issues

Nous utilisons plusieurs labels pour catégoriser les issues :

- 🟢 `good first issue` - Parfait pour les nouveaux contributeurs
- 🆘 `help wanted` - Nous avons besoin d'aide sur ces sujets
- 🐛 `bug` - Quelque chose ne fonctionne pas
- ✨ `enhancement` - Nouvelle fonctionnalité ou amélioration
- 📚 `documentation` - Améliorations de la documentation
- 🧪 `testing` - Liés aux tests et à la qualité
- 🎨 `ui/ux` - Interface utilisateur et expérience

---

## 💬 Communication

### Issues et Discussions
- Utilisez les **Issues** pour signaler des bugs ou proposer des fonctionnalités
- Utilisez les **Discussions** pour des questions générales ou des idées
- Commentez les issues pour indiquer que vous y travaillez

### Demande d'Aide
- N'hésitez pas à poser des questions dans les commentaires d'issues
- Demandez de l'aide si vous êtes bloqué
- La communauté est là pour vous aider !

### Revue de Code
- Soyez constructif dans vos commentaires
- Expliquez le "pourquoi" derrière vos suggestions
- Soyez patient avec les nouveaux contributeurs

---

## ✅ Checklist avant Submission

Avant de soumettre votre PR, vérifiez que :

- [ ] Le code suit les conventions du projet
- [ ] Tous les tests passent localement
- [ ] La documentation est mise à jour si nécessaire
- [ ] Les messages de commit suivent les conventions
- [ ] Vous avez testé vos changements manuellement
- [ ] Vous avez décrit clairement vos changements dans la PR

---

## 🎉 Reconnaissance

Tous les contributeurs sont reconnus et célébrés :

- **README.md** : Tous les contributeurs sont listés
- **Release Notes** : Les contributions majeures sont mises en valeur
- **Community** : Nous valorisons chaque contribution, petite ou grande

---

## 📖 Ressources Supplémentaires

- 📋 [GOOD_FIRST_ISSUES.md](GOOD_FIRST_ISSUES.md) - Issues pour débuter
- 🛠️ [DEVELOPMENT.md](DEVELOPMENT.md) - Guide de développement complet
- 🏗️ [ARCHITECTURE.md](ARCHITECTURE.md) - Architecture du projet (à créer)
- 🐛 [Templates d'Issues](.github/ISSUE_TEMPLATE/) - Pour signaler des problèmes
- 🔄 [Template de PR](.github/pull_request_template.md) - Pour vos contributions

---

## 🤝 Code de Conduite

Nous nous engageons à maintenir un environnement accueillant et inclusif. Soyez respectueux, patient et constructif dans toutes vos interactions.

### Nos Valeurs
- **Respect** : Traitez tous les contributeurs avec respect
- **Inclusion** : Accueillez les contributeurs de tous niveaux
- **Collaboration** : Travaillons ensemble vers un objectif commun
- **Apprentissage** : Partageons nos connaissances et apprenons ensemble

---

**Merci de contribuer au projet LMS ! Votre aide fait la différence ! 🚀**