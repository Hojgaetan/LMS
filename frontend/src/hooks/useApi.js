import { useState, useEffect } from 'react';
import { useQuery, useMutation, useQueryClient } from 'react-query';
import toast from 'react-hot-toast';

// Hook personnalisé pour les requêtes avec gestion d'erreurs
export const useApiQuery = (key, queryFn, options = {}) => {
  return useQuery(key, queryFn, {
    onError: (error) => {
      const message = error.response?.data?.message || 'Une erreur est survenue';
      toast.error(message);
    },
    ...options,
  });
};

// Hook personnalisé pour les mutations avec gestion d'erreurs et succès
export const useApiMutation = (mutationFn, options = {}) => {
  const queryClient = useQueryClient();

  return useMutation(mutationFn, {
    onSuccess: (data, variables, context) => {
      if (options.successMessage) {
        toast.success(options.successMessage);
      }
      if (options.invalidateQueries) {
        options.invalidateQueries.forEach(key => {
          queryClient.invalidateQueries(key);
        });
      }
      if (options.onSuccess) {
        options.onSuccess(data, variables, context);
      }
    },
    onError: (error, variables, context) => {
      const message = error.response?.data?.message || 'Une erreur est survenue';
      toast.error(message);
      if (options.onError) {
        options.onError(error, variables, context);
      }
    },
    ...options,
  });
};

// Hook pour gérer l'état de chargement global
export const useGlobalLoading = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [loadingMessage, setLoadingMessage] = useState('');

  const startLoading = (message = 'Chargement...') => {
    setIsLoading(true);
    setLoadingMessage(message);
  };

  const stopLoading = () => {
    setIsLoading(false);
    setLoadingMessage('');
  };

  return {
    isLoading,
    loadingMessage,
    startLoading,
    stopLoading,
  };
};

// Hook pour gérer les notifications
export const useNotifications = () => {
  const showSuccess = (message) => {
    toast.success(message, {
      duration: 4000,
      icon: '✅',
    });
  };

  const showError = (message) => {
    toast.error(message, {
      duration: 5000,
      icon: '❌',
    });
  };

  const showWarning = (message) => {
    toast(message, {
      duration: 4000,
      icon: '⚠️',
      style: {
        background: '#f59e0b',
        color: '#fff',
      },
    });
  };

  const showInfo = (message) => {
    toast(message, {
      duration: 4000,
      icon: 'ℹ️',
      style: {
        background: '#3b82f6',
        color: '#fff',
      },
    });
  };

  return {
    showSuccess,
    showError,
    showWarning,
    showInfo,
  };
};

// Hook pour gérer la pagination
export const usePagination = (data = [], itemsPerPage = 10) => {
  const [currentPage, setCurrentPage] = useState(1);

  const totalPages = Math.ceil(data.length / itemsPerPage);
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const currentData = data.slice(startIndex, endIndex);

  const goToPage = (page) => {
    if (page >= 1 && page <= totalPages) {
      setCurrentPage(page);
    }
  };

  const goToNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(currentPage + 1);
    }
  };

  const goToPreviousPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  // Reset to first page when data changes
  useEffect(() => {
    setCurrentPage(1);
  }, [data.length]);

  return {
    currentPage,
    totalPages,
    currentData,
    goToPage,
    goToNextPage,
    goToPreviousPage,
    hasNextPage: currentPage < totalPages,
    hasPreviousPage: currentPage > 1,
  };
};

// Hook pour gérer les filtres et la recherche
export const useFilters = (data = [], filterFn) => {
  const [filters, setFilters] = useState({});
  const [searchTerm, setSearchTerm] = useState('');

  const filteredData = data.filter(item => {
    // Appliquer la recherche
    const matchesSearch = searchTerm === '' || 
      Object.values(item).some(value => 
        String(value).toLowerCase().includes(searchTerm.toLowerCase())
      );

    // Appliquer les filtres personnalisés
    const matchesFilters = filterFn ? filterFn(item, filters) : true;

    return matchesSearch && matchesFilters;
  });

  const updateFilter = (key, value) => {
    setFilters(prev => ({
      ...prev,
      [key]: value,
    }));
  };

  const clearFilters = () => {
    setFilters({});
    setSearchTerm('');
  };

  return {
    filters,
    searchTerm,
    filteredData,
    setSearchTerm,
    updateFilter,
    clearFilters,
  };
};