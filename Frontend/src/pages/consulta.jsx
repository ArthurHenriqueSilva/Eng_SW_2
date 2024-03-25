import React, { useState } from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import Filter from '../components/Filter';
import Table from '../components/Table';
import '../style/consulta.css'
export function Consulta() {
  const [primeiroAcesso, setPrimeiroAcesso] = useState(false);
  const [dados, setDados] = useState([
    { nome: 'João', cargo: 'Desenvolvedor', lotacao: 'São Paulo', rendimentos: 5000, descontos: 1000 },
    { nome: 'Maria', cargo: 'Designer', lotacao: 'Rio de Janeiro', rendimentos: 4500, descontos: 800 }
  ]);

  return (
    <>
      <Navbar />
      <div id='container-consulta'>
      <Filter/>
      <Table dados={dados} primeiroAcesso={primeiroAcesso} />   
      </div>
      <Footer />
    </>
  );
}
