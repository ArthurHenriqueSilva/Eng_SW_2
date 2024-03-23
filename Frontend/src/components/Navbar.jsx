import React from 'react';
import '../styles/Navbar.css';
import logo from '../assets/tjba.png'

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">
        <img src={logo} alt="Logo Site" />
      </div>
      <ul className="nav-links">
        <li><a href="#home">Pagina Inicial</a></li>
        <li><a href="#about">Sobre o Projeto</a></li>
        <li><a href="#services">Servico Prestado</a></li>
        <li><a href="#contact">Contato</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;
