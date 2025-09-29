import React, { useState } from 'react';
import { Navbar as BootstrapNavbar, Nav, NavDropdown, Container } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';
import { motion } from 'framer-motion';
import './Navbar.css';

const Navbar = () => {
  const [expanded, setExpanded] = useState(false);

  const handleToggle = () => setExpanded(!expanded);
  const handleSelect = () => setExpanded(false);

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
      >
        <Container fluid>
          <LinkContainer to="/">
            <BootstrapNavbar.Brand className="navbar-brand-custom">
              <motion.div
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="brand-content"
              >
                <i className="bi bi-journal-bookmark-fill me-2"></i>
                <span className="brand-text">Library MS</span>
              </motion.div>
            </BootstrapNavbar.Brand>
          </LinkContainer>

          <BootstrapNavbar.Toggle aria-controls="basic-navbar-nav" />
          
          <BootstrapNavbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto" onSelect={handleSelect}>
              <LinkContainer to="/">
                <Nav.Link className="nav-link-custom">
                  <i className="bi bi-speedometer2 me-2"></i>
                  Tableau de Bord
                </Nav.Link>
              </LinkContainer>
              
              <LinkContainer to="/books">
                <Nav.Link className="nav-link-custom">
                  <i className="bi bi-book me-2"></i>
                  Livres
                </Nav.Link>
              </LinkContainer>
              
              <LinkContainer to="/members">
                <Nav.Link className="nav-link-custom">
                  <i className="bi bi-people me-2"></i>
                  Membres
                </Nav.Link>
              </LinkContainer>
              
              <LinkContainer to="/loans">
                <Nav.Link className="nav-link-custom">
                  <i className="bi bi-arrow-left-right me-2"></i>
                  Emprunts
                </Nav.Link>
              </LinkContainer>
              
              <LinkContainer to="/reports">
                <Nav.Link className="nav-link-custom">
                  <i className="bi bi-bar-chart me-2"></i>
                  Rapports
                </Nav.Link>
              </LinkContainer>

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
                <NavDropdown.Item href="#register">
                  <i className="bi bi-person-plus me-2"></i>
                  Inscription
                </NavDropdown.Item>
                <NavDropdown.Item href="#login">
                  <i className="bi bi-box-arrow-in-right me-2"></i>
                  Connexion
                </NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#profile">
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