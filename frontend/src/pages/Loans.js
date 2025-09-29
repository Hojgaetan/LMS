import React from 'react';
import { Container } from 'react-bootstrap';
import { motion } from 'framer-motion';

const Loans = () => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
    >
      <Container fluid>
        <div className="text-center py-5">
          <motion.h2
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="gradient-text"
          >
            <i className="bi bi-arrow-left-right me-3"></i>
            Gestion des Emprunts
          </motion.h2>
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="text-muted mt-3"
          >
            Cette page est en cours de développement...
          </motion.p>
        </div>
      </Container>
    </motion.div>
  );
};

export default Loans;