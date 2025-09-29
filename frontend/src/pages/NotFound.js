import React from 'react';
import { Container, Button } from 'react-bootstrap';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';

const NotFound = () => {
  const navigate = useNavigate();

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.8 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.6 }}
    >
      <Container fluid>
        <div className="text-center py-5">
          <motion.div
            initial={{ opacity: 0, y: -50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            <h1 className="display-1 gradient-text">404</h1>
            <h2 className="mb-4">Page non trouvée</h2>
            <p className="text-muted mb-4">
              La page que vous recherchez n'existe pas ou a été déplacée.
            </p>
            <Button 
              variant="primary" 
              size="lg"
              onClick={() => navigate('/')}
            >
              <i className="bi bi-house me-2"></i>
              Retour à l'accueil
            </Button>
          </motion.div>
        </div>
      </Container>
    </motion.div>
  );
};

export default NotFound;