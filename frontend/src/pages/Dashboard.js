import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import { motion } from 'framer-motion';
import { useQuery } from 'react-query';
import StatCard from '../components/UI/StatCard';
import LoadingSpinner from '../components/UI/LoadingSpinner';
import { fetchDashboardStats } from '../services/api';
import './Dashboard.css';

const Dashboard = () => {
  const { data: stats, isLoading, error } = useQuery(
    'dashboardStats',
    fetchDashboardStats,
    {
      refetchInterval: 30000, // Actualiser toutes les 30 secondes
    }
  );

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1
      }
    }
  };

  const titleVariants = {
    hidden: { opacity: 0, y: -50 },
    visible: { 
      opacity: 1, 
      y: 0,
      transition: {
        duration: 0.8,
        ease: "easeOut"
      }
    }
  };

  if (isLoading) return <LoadingSpinner fullScreen text="Chargement du tableau de bord..." />;
  if (error) return <div className="alert alert-danger">Erreur lors du chargement des données</div>;

  return (
    <motion.div
      variants={containerVariants}
      initial="hidden"
      animate="visible"
    >
      <Container fluid className="dashboard-container">
        {/* En-tête */}
        <motion.div 
          className="dashboard-header"
          variants={titleVariants}
        >
          <div className="text-center mb-5">
            <h1 className="dashboard-title">
              <motion.i 
                className="bi bi-speedometer2 me-3"
                animate={{ rotate: [0, 10, -10, 0] }}
                transition={{ duration: 2, repeat: Infinity, repeatDelay: 3 }}
              ></motion.i>
              Tableau de Bord
            </h1>
            <p className="dashboard-subtitle">
              Gérez votre bibliothèque avec efficacité et style
            </p>
          </div>
        </motion.div>

        {/* Statistiques principales */}
        <Row className="g-4 mb-5">
          <Col md={4}>
            <StatCard
              title="Total Livres"
              value={stats?.total_books || 0}
              icon="bi-book"
              color="primary"
              delay={0.1}
              description="Nombre total de livres disponibles dans la bibliothèque"
              trend={{ type: 'up', value: 12 }}
            />
          </Col>
          <Col md={4}>
            <StatCard
              title="Catégories"
              value={stats?.total_category || 0}
              icon="bi-tags"
              color="success"
              delay={0.2}
              description="Nombre total de catégories de livres"
            />
          </Col>
          <Col md={4}>
            <StatCard
              title="Auteurs"
              value={stats?.total_authors || 0}
              icon="bi-person"
              color="info"
              delay={0.3}
              description="Nombre total d'auteurs enregistrés"
            />
          </Col>
        </Row>

        {/* Statistiques secondaires */}
        <Row className="g-4 mb-5">
          <Col md={4}>
            <StatCard
              title="Livres Populaires"
              value={stats?.total_popular_books || 0}
              icon="bi-bar-chart"
              color="warning"
              delay={0.4}
              description="Nombre de livres populaires basés sur les emprunts"
              trend={{ type: 'up', value: 8 }}
            />
          </Col>
          <Col md={4}>
            <StatCard
              title="Membres Actifs"
              value={stats?.total_active_members || 0}
              icon="bi-person-lines-fill"
              color="success"
              delay={0.5}
              description="Nombre de membres ayant emprunté des livres récemment"
              trend={{ type: 'up', value: 15 }}
            />
          </Col>
          <Col md={4}>
            <StatCard
              title="Livres en Retard"
              value={stats?.total_overdue_books || 0}
              icon="bi-exclamation-circle"
              color="danger"
              delay={0.6}
              description="Nombre de livres dont la date de retour est dépassée"
              trend={{ type: 'down', value: 5 }}
            />
          </Col>
        </Row>

        {/* Actions rapides */}
        <motion.div
          className="quick-actions"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.7 }}
        >
          <h3 className="section-title">
            <i className="bi bi-lightning me-2"></i>
            Actions Rapides
          </h3>
          <Row className="g-3">
            <Col md={3}>
              <motion.div
                className="quick-action-card"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                <i className="bi bi-plus-circle"></i>
                <span>Ajouter un Livre</span>
              </motion.div>
            </Col>
            <Col md={3}>
              <motion.div
                className="quick-action-card"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                <i className="bi bi-person-plus"></i>
                <span>Nouveau Membre</span>
              </motion.div>
            </Col>
            <Col md={3}>
              <motion.div
                className="quick-action-card"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                <i className="bi bi-arrow-left-right"></i>
                <span>Gérer Emprunts</span>
              </motion.div>
            </Col>
            <Col md={3}>
              <motion.div
                className="quick-action-card"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                <i className="bi bi-bar-chart"></i>
                <span>Voir Rapports</span>
              </motion.div>
            </Col>
          </Row>
        </motion.div>
      </Container>
    </motion.div>
  );
};

export default Dashboard;