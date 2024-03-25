import React from 'react';
import { NavLink } from 'react-router-dom';
import '../style/Servico.css';
import logo from '../assets/tjba.png';

const Servico = () => {
  return (
    <div className="servico-container">
      <img src={logo} alt="TJBA Logo" className="logo" />
      <h2>Serviço de Acesso à Folha de Pagamento do Tribunal de Justiça da Bahia</h2>
      <p>
        Este aplicativo faz parte de um projeto acadêmico da disciplina de Engenharia de Software.
        Sua finalidade é facilitar o acesso aos dados da folha de pagamento do Tribunal de Justiça
        da Bahia, proporcionando uma maneira eficiente e simplificada para os usuários obterem as
        informações necessárias.
      </p>
      <NavLink to="/Consulta">
        <button id='toconsulta'>
        Acessar Aplicativo
        </button>
      </NavLink>
    </div>
  );
}

export default Servico;
