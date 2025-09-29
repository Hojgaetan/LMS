import axios from 'axios';

// Configuration de base d'Axios
const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:5000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Intercepteur pour les requêtes
api.interceptors.request.use(
  (config) => {
    // Ajouter des headers d'authentification si nécessaire
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Intercepteur pour les réponses
api.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    // Gestion globale des erreurs
    if (error.response?.status === 401) {
      // Rediriger vers la page de connexion
      localStorage.removeItem('authToken');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Services API

// Dashboard
export const fetchDashboardStats = async () => {
  try {
    // Récupérer les statistiques depuis différents endpoints
    const [books, categories, authors, popularBooks, activeMembers, overdueBooks] = await Promise.all([
      api.get('/books/total-books'),
      api.get('/book_category/total-category'),
      api.get('/authors/total-authors'),
      api.get('/books/total-popular-books'),
      api.get('/members/total-active-members'),
      api.get('/books/total-overdue-books'),
    ]);

    return {
      total_books: books.total_books || 0,
      total_category: categories.total_category || 0,
      total_authors: authors.total_authors || 0,
      total_popular_books: popularBooks.total_popular_books || 0,
      total_active_members: activeMembers.total_active_members || 0,
      total_overdue_books: overdueBooks.total_overdue_books || 0,
    };
  } catch (error) {
    console.error('Erreur lors de la récupération des statistiques:', error);
    // Retourner des valeurs par défaut en cas d'erreur
    return {
      total_books: 0,
      total_category: 0,
      total_authors: 0,
      total_popular_books: 0,
      total_active_members: 0,
      total_overdue_books: 0,
    };
  }
};

// Books
export const fetchBooks = async () => {
  const response = await api.get('/books/books');
  return response.books || [];
};

export const fetchBooksStats = async () => {
  try {
    const [totalBooks, popularBooks] = await Promise.all([
      api.get('/books/total-books'),
      api.get('/books/total-popular-books'),
    ]);

    return {
      total_books: totalBooks.total_books || 0,
      total_popular_books: popularBooks.total_popular_books || 0,
    };
  } catch (error) {
    console.error('Erreur lors de la récupération des statistiques des livres:', error);
    return {
      total_books: 0,
      total_popular_books: 0,
    };
  }
};

export const addBook = async (bookData) => {
  return await api.post('/books/add', bookData);
};

export const updateBook = async (bookId, bookData) => {
  return await api.post('/books/edit', { id: bookId, ...bookData });
};

export const deleteBook = async (bookId) => {
  return await api.post('/books/delete', { book_id: bookId });
};

// Members
export const fetchMembers = async () => {
  // À implémenter quand l'endpoint sera disponible
  return [];
};

export const fetchMembersStats = async () => {
  try {
    const [totalMembers, activeMembers] = await Promise.all([
      api.get('/members/total-members'),
      api.get('/members/total-active-members'),
    ]);

    return {
      total_members: totalMembers.total_members || 0,
      total_active_members: activeMembers.total_active_members || 0,
    };
  } catch (error) {
    console.error('Erreur lors de la récupération des statistiques des membres:', error);
    return {
      total_members: 0,
      total_active_members: 0,
    };
  }
};

export const addMember = async (memberData) => {
  return await api.post('/members/add', memberData);
};

export const updateMember = async (memberData) => {
  return await api.post('/members/update', memberData);
};

export const deleteMember = async (memberId) => {
  return await api.post('/members/delete', { member_id: memberId });
};

// Loans
export const fetchLoans = async () => {
  // À implémenter quand l'endpoint sera disponible
  return [];
};

// Reports
export const fetchReports = async () => {
  // À implémenter quand l'endpoint sera disponible
  return [];
};

export default api;