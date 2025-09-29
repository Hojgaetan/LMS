import React from 'react';
import { Card } from 'react-bootstrap';
import { motion } from 'framer-motion';
import './StatCard.css';

const StatCard = ({ 
  title, 
  value, 
  icon, 
  color = 'primary', 
  delay = 0,
  description,
  trend 
}) => {
  const cardVariants = {
    hidden: { 
      opacity: 0, 
      y: 50,
      scale: 0.9
    },
    visible: { 
      opacity: 1, 
      y: 0,
      scale: 1,
      transition: {
        duration: 0.6,
        delay: delay,
        ease: "easeOut"
      }
    }
  };

  const iconVariants = {
    hidden: { scale: 0, rotate: -180 },
    visible: { 
      scale: 1, 
      rotate: 0,
      transition: {
        duration: 0.8,
        delay: delay + 0.2,
        ease: "easeOut"
      }
    }
  };

  return (
    <motion.div
      variants={cardVariants}
      initial="hidden"
      animate="visible"
      whileHover={{ 
        y: -10,
        transition: { duration: 0.3 }
      }}
    >
      <Card className={`stat-card stat-card-${color}`}>
        <Card.Body className="stat-card-body">
          <div className="stat-card-header">
            <div className="stat-card-info">
              <h6 className="stat-card-title">
                {title}
                {description && (
                  <i 
                    className="bi bi-question-circle stat-card-help" 
                    title={description}
                  ></i>
                )}
              </h6>
              <div className="stat-card-value">
                {value}
                {trend && (
                  <span className={`stat-card-trend ${trend.type}`}>
                    <i className={`bi bi-arrow-${trend.type === 'up' ? 'up' : 'down'}`}></i>
                    {trend.value}%
                  </span>
                )}
              </div>
            </div>
            <motion.div 
              className="stat-card-icon"
              variants={iconVariants}
            >
              <i className={`bi ${icon}`}></i>
            </motion.div>
          </div>
        </Card.Body>
        <div className="stat-card-glow"></div>
      </Card>
    </motion.div>
  );
};

export default StatCard;