import React, { useState, useEffect, useRef } from 'react';
import { Navbar as BootstrapNavbar, Nav, NavDropdown, Container } from 'react-bootstrap';
import { NavLink, Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import './Navbar.css';

const Navbar = () => {
  const [expanded, setExpanded] = useState(false);
  const navRef = useRef(null);

  const handleToggle = () => setExpanded(!expanded);
  const handleSelect = () => setExpanded(false);

  const updateNavHeight = () => {
    if (navRef.current) {
      const h = navRef.current.offsetHeight;
      // Met à jour la variable CSS globale
      document.documentElement.style.setProperty('--navbar-height', h + 'px');
    }
  };

  useEffect(() => {
    // Initialisation
    updateNavHeight();
    // Écoute le resize
    window.addEventListener('resize', updateNavHeight);
    return () => window.removeEventListener('resize', updateNavHeight);
  }, []);

  useEffect(() => {
    // Recalcule après expansion/collapse (attendre la fin d'animation Bootstrap)
    const t = setTimeout(updateNavHeight, 300);
    return () => clearTimeout(t);
  }, [expanded]);

  const navLinkClass = ({ isActive }) => `nav-link-custom${isActive ? ' active' : ''}`;

  return (
    <motion.div
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
    >
      <BootstrapNavbar 
        expand="lg" 
        className="custom-navbar" 
        fixed="top"
        expanded={expanded}
        onToggle={handleToggle}
        ref={navRef}
      >
        <Container fluid>
          <Link to="/" className="navbar-brand-custom" onClick={handleSelect}>
            <BootstrapNavbar.Brand as="span" className="navbar-brand-custom">
              <motion.div
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="brand-content"
              >
                <i className="bi bi-journal-bookmark-fill me-2"></i>
                <span className="brand-text">Library MS</span>
              </motion.div>
            </BootstrapNavbar.Brand>
          </Link>

          <BootstrapNavbar.Toggle aria-controls="basic-navbar-nav" />
          
          <BootstrapNavbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto">
              <Nav.Link as={NavLink} to="/" className={navLinkClass} onClick={handleSelect} end>
                <i className="bi bi-speedometer2 me-2"></i>
                Tableau de Bord
              </Nav.Link>

              <Nav.Link as={NavLink} to="/books" className={navLinkClass} onClick={handleSelect}>
                <i className="bi bi-book me-2"></i>
                Livres
              </Nav.Link>

              <Nav.Link as={NavLink} to="/members" className={navLinkClass} onClick={handleSelect}>
                <i className="bi bi-people me-2"></i>
                Membres
              </Nav.Link>

              <Nav.Link as={NavLink} to="/loans" className={navLinkClass} onClick={handleSelect}>
                <i className="bi bi-arrow-left-right me-2"></i>
                Emprunts
              </Nav.Link>

              <Nav.Link as={NavLink} to="/reports" className={navLinkClass} onClick={handleSelect}>
                <i className="bi bi-bar-chart me-2"></i>
                Rapports
              </Nav.Link>

              <NavDropdown 
                title={
                  <span>
                    <i className="bi bi-person-circle me-2"></i>
                    Compte
                  </span>
                } 
                id="account-dropdown"
                className="nav-dropdown-custom"
              >
                <NavDropdown.Item as={NavLink} to="/register" onClick={handleSelect}>
                  <i className="bi bi-person-plus me-2"></i>
                  Inscription
                </NavDropdown.Item>
                <NavDropdown.Item as={NavLink} to="/login" onClick={handleSelect}>
                  <i className="bi bi-box-arrow-in-right me-2"></i>
                  Connexion
                </NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item as={NavLink} to="/profile" onClick={handleSelect}>
                  <i className="bi bi-gear me-2"></i>
                  Paramètres
                </NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </BootstrapNavbar.Collapse>
        </Container>
      </BootstrapNavbar>
    </motion.div>
  );
};

export default Navbar;