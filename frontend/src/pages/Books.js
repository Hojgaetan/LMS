import React, { useState } from 'react';
import { Container, Row, Col, Button, Table, Badge } from 'react-bootstrap';
import { motion } from 'framer-motion';
import { useQuery } from 'react-query';
import StatCard from '../components/UI/StatCard';
import LoadingSpinner from '../components/UI/LoadingSpinner';
import { fetchBooks, fetchBooksStats } from '../services/api';
import './Books.css';

const Books = () => {
  const [selectedBook, setSelectedBook] = useState(null);

  const { data: books, isLoading: booksLoading } = useQuery('books', fetchBooks);
  const { data: stats, isLoading: statsLoading } = useQuery('booksStats', fetchBooksStats);

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1
      }
    }
  };

  if (booksLoading || statsLoading) {
    return <LoadingSpinner fullScreen text="Chargement des livres..." />;
  }

  return (
    <motion.div
      variants={containerVariants}
      initial="hidden"
      animate="visible"
    >
      <Container fluid className="books-container">
        {/* En-tête */}
        <div className="page-header">
          <div className="d-flex justify-content-between align-items-center mb-4">
            <motion.h2 
              className="page-title"
              initial={{ opacity: 0, x: -50 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6 }}
            >
              <i className="bi bi-book me-3"></i>
              Gestion des Livres
            </motion.h2>
            <motion.div
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
            >
              <Button 
                variant="primary" 
                size="lg"
                className="add-book-btn"
              >
                <i className="bi bi-plus-circle me-2"></i>
                Ajouter un Livre
              </Button>
            </motion.div>
          </div>
        </div>

        {/* Statistiques */}
        <Row className="g-4 mb-5">
          <Col md={6}>
            <StatCard
              title="Total Livres"
              value={stats?.total_books || 0}
              icon="bi-book"
              color="primary"
              delay={0.1}
              description="Nombre total de livres dans la bibliothèque"
            />
          </Col>
          <Col md={6}>
            <StatCard
              title="Livres Populaires"
              value={stats?.total_popular_books || 0}
              icon="bi-bar-chart"
              color="warning"
              delay={0.2}
              description="Livres les plus empruntés"
            />
          </Col>
        </Row>

        {/* Table des livres */}
        <motion.div
          className="books-table-container"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.3 }}
        >
          <div className="table-header">
            <h4>
              <i className="bi bi-list me-2"></i>
              Liste des Livres
            </h4>
          </div>
          
          <div className="table-responsive">
            <Table hover className="books-table">
              <thead>
                <tr>
                  <th><i className="bi bi-book me-2"></i>Titre</th>
                  <th><i className="bi bi-person me-2"></i>Auteur</th>
                  <th><i className="bi bi-tags me-2"></i>Catégorie</th>
                  <th><i className="bi bi-check-circle me-2"></i>Disponibilité</th>
                  <th><i className="bi bi-gear me-2"></i>Actions</th>
                </tr>
              </thead>
              <tbody>
                {books?.map((book, index) => (
                  <motion.tr
                    key={book.id}
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.5, delay: index * 0.1 }}
                    className="book-row"
                  >
                    <td className="book-title">{book.title}</td>
                    <td>{book.author}</td>
                    <td>
                      <Badge bg="secondary" className="category-badge">
                        {book.category}
                      </Badge>
                    </td>
                    <td>
                      <Badge 
                        bg={book.available_quantity > 0 ? 'success' : 'danger'}
                        className="availability-badge"
                      >
                        <i className={`bi ${book.available_quantity > 0 ? 'bi-check-circle' : 'bi-x-circle'} me-1`}></i>
                        {book.available_quantity > 0 ? 'Disponible' : 'Emprunté'}
                      </Badge>
                    </td>
                    <td>
                      <div className="action-buttons">
                        <Button
                          variant="outline-info"
                          size="sm"
                          className="action-btn"
                          onClick={() => setSelectedBook(book)}
                        >
                          <i className="bi bi-eye"></i>
                        </Button>
                        <Button
                          variant="outline-warning"
                          size="sm"
                          className="action-btn"
                        >
                          <i className="bi bi-pencil"></i>
                        </Button>
                        <Button
                          variant="outline-danger"
                          size="sm"
                          className="action-btn"
                        >
                          <i className="bi bi-trash"></i>
                        </Button>
                      </div>
                    </td>
                  </motion.tr>
                ))}
              </tbody>
            </Table>
          </div>
        </motion.div>
      </Container>
    </motion.div>
  );
};

export default Books;