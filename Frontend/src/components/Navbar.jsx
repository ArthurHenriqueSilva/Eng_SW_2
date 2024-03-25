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
        <li>
          <NavLink to='/'>Pagina Inicial </NavLink>
        </li>
        <li>
          <NavLink to='/Login'>Login</NavLink>
        </li>
        <li>
          <NavLink to='/Servico'>Servico Prestado</NavLink>
        </li>
        <li>
          <NavLink to='/Contato'>Contato</NavLink>
      </li>
      </ul>
    </nav>
  );
}

export default Navbar;
