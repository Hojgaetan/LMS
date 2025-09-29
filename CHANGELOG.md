# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur (Keep a Changelog) et ce projet adhère au versionnage sémantique (SemVer).

## [0.1.0] - 2025-09-29
### Ajouté
- Première version publique du LMS.
- Architecture MVC : models, services, controllers, views.
- Gestion des livres : ajout, mise à jour, suppression, recherche basique, affichage des détails.
- Gestion des auteurs (basique) : ajout d'auteurs.
- Gestion des catégories (basique) : ajout de catégories.
- Interface Web Flask (+ templates, static assets).
- Mode CLI (menu basique) pour opérations manuelles.
- Initialisation / réinitialisation de la base SQLite via `DatabaseService`.
- Documentation initiale : README, CONTRIBUTING, DEVELOPMENT, GOOD_FIRST_ISSUES, UML.

### Partiellement implémenté
- Recherche de livres avancée.
- Gestion de l'inventaire (stock / disponibilité).
- Navigation par catégorie.

### Planifié (non encore implémenté)
- Gestion avancée des membres (CRUD complet, historique, statut).
- Emprunts (prêt, retour, prolongation, relances, retards, rapports).
- Rapports analytiques (popularité, activité, inventaire, retards).
- Authentification / rôles, configuration système.
- Sauvegarde / restauration base de données, logging d'activité.

---

[0.1.0]: https://github.com/Hojgaetan/LMS/releases/tag/v0.1.0

