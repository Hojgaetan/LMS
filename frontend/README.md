# Frontend React - Library Management System

Ce dossier contient l'application React pour le système de gestion de bibliothèque (LMS).

## 🚀 Démarrage Rapide

### Prérequis
- Node.js 16+ 
- npm ou yarn

### Installation

1. **Naviguer vers le dossier frontend**
```bash
cd frontend
```

2. **Installer les dépendances**
```bash
npm install
```

3. **Démarrer l'application en mode développement**
```bash
npm start
```

L'application sera accessible sur http://localhost:3000

### Scripts Disponibles

- `npm start` - Démarre l'application en mode développement
- `npm run build` - Construit l'application pour la production
- `npm test` - Lance les tests
- `npm run eject` - Éjecte la configuration (irréversible)

## 🏗️ Architecture

### Structure des Dossiers
```
frontend/
├── public/                 # Fichiers statiques
├── src/
│   ├── components/        # Composants réutilisables
│   │   ├── Layout/       # Composants de mise en page
│   │   └── UI/           # Composants d'interface
│   ├── pages/            # Pages de l'application
│   ├── services/         # Services API
│   ├── hooks/            # Hooks personnalisés
│   ├── styles/           # Styles CSS
│   └── utils/            # Utilitaires
└── package.json
```

### Technologies Utilisées

- **React 18** - Bibliothèque UI
- **React Router** - Routage
- **React Bootstrap** - Composants UI
- **React Query** - Gestion des données
- **Framer Motion** - Animations
- **Axios** - Client HTTP
- **React Hook Form** - Gestion des formulaires
- **React Hot Toast** - Notifications

## 🎨 Design System

### Couleurs
- Primary: `#667eea`
- Secondary: `#764ba2`
- Accent: `#f093fb`
- Success: `#10b981`
- Warning: `#f59e0b`
- Danger: `#ef4444`

### Composants

#### StatCard
Composant pour afficher les statistiques avec animations.

```jsx
<StatCard
  title="Total Livres"
  value={150}
  icon="bi-book"
  color="primary"
  description="Nombre total de livres"
/>
```

#### LoadingSpinner
Composant de chargement avec animations.

```jsx
<LoadingSpinner 
  size="lg" 
  text="Chargement..." 
  fullScreen={true} 
/>
```

## 🔌 API Integration

### Configuration
L'URL de l'API est configurée dans `src/services/api.js`:

```javascript
const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:5000',
});
```

### Utilisation avec React Query

```javascript
import { useQuery } from 'react-query';
import { fetchBooks } from '../services/api';

const { data: books, isLoading } = useQuery('books', fetchBooks);
```

## 🎭 Animations

### Framer Motion
Animations fluides avec Framer Motion:

```jsx
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.6 }}
>
  Contenu animé
</motion.div>
```

### Animations CSS
Animations CSS personnalisées dans `src/styles/index.css`.

## 📱 Responsive Design

L'application est entièrement responsive avec:
- Breakpoints Bootstrap
- Grille flexible
- Navigation mobile optimisée

## 🧪 Tests

### Lancer les tests
```bash
npm test
```

### Structure des tests
```
src/
├── components/
│   └── __tests__/
├── pages/
│   └── __tests__/
└── services/
    └── __tests__/
```

## 🚀 Déploiement

### Build de production
```bash
npm run build
```

### Variables d'environnement
Créer un fichier `.env` dans le dossier frontend:

```
REACT_APP_API_URL=http://localhost:5000
REACT_APP_VERSION=1.0.0
```

## 🔧 Configuration

### Proxy API
Le proxy vers l'API Flask est configuré dans `package.json`:

```json
{
  "proxy": "http://localhost:5000"
}
```

### ESLint et Prettier
Configuration dans `.eslintrc.js` et `.prettierrc`.

## 📚 Ressources

- [React Documentation](https://reactjs.org/)
- [React Bootstrap](https://react-bootstrap.github.io/)
- [Framer Motion](https://www.framer.com/motion/)
- [React Query](https://react-query.tanstack.com/)

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.