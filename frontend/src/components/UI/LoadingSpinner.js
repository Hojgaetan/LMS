import React from 'react';
import { Spinner } from 'react-bootstrap';
import { motion } from 'framer-motion';
import './LoadingSpinner.css';

const LoadingSpinner = ({ size = 'md', text = 'Chargement...', fullScreen = false }) => {
  const spinnerSizes = {
    sm: { width: '1rem', height: '1rem' },
    md: { width: '2rem', height: '2rem' },
    lg: { width: '3rem', height: '3rem' }
  };

  const LoadingContent = () => (
    <motion.div 
      className={`loading-spinner ${fullScreen ? 'loading-fullscreen' : ''}`}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      <div className="loading-content">
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
        >
          <Spinner 
            animation="border" 
            style={spinnerSizes[size]}
            className="loading-spinner-element"
          />
        </motion.div>
        {text && <p className="loading-text">{text}</p>}
        }
      </div>
    </motion.div>
  );

  return <LoadingContent />;
};

export default LoadingSpinner;