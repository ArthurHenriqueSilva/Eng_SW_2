import React, { useState } from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import Filter from '../components/Filter';
import Table from '../components/Table';
import '../style/consulta.css';

export function Consulta() {
  const [primeiroAcesso, setPrimeiroAcesso] = useState(false);
  const [dados, setDados] = useState([]);

  const dadosTeste = [
    {
      nome: 'João',
      cargo: 'Analista',
      lotacao: 'Departamento X',
      rendimentos: 5000,
      descontos: 1000
    },
    {
      nome: 'Maria',
      cargo: 'Gerente',
      lotacao: 'Departamento Y',
      rendimentos: 8000,
      descontos: 1500
    },
  ];

  return (
    <>
      <Navbar />
      <div id='container-consulta'>
        <Filter setDados={setDados} />
        <Table dados={dadosTeste} primeiroAcesso={primeiroAcesso} />   
      </div>
      <Footer />
    </>
  );
}
