import React from 'react';
import { NavLink } from 'react-router-dom';
import '../style/Navbar.css';
import logo from '../assets/tjba.png';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">
        <img src={logo} alt="Logo Site" />
      </div>
      <ul className="nav-links">
        <li><a href="#home">Pagina Inicial</a></li>
        <li>
          <NavLink to='/Login'>Login</NavLink>
          </li>
        <li><a href="#services">Servico Prestado</a></li>
        <li><a href="#contact">Contato</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;
