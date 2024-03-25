import React from 'react';
import '../style/Contato.css'
import github from '../assets/github.svg'

const Contato = () => {
  const contatos = [
    { nome: 'ARTHUR HENRIQUE SILVA DE LIMA', github: 'https://github.com/arthurhenriquesilva' },
    { nome: 'DÉBORAH ABREU SALES', github: 'https://github.com/deborahsales' },
    { nome: 'GABRIELA ANDRADE MOTA', github: 'https://github.com/gabigam' },
    { nome: 'SANDERSON LACY ALVES DOS SANTOS', github: 'https://github.com/sandersonlacy' },
    { nome: 'VINÍCIUS DIAS VALENÇA', github: 'https://github.com/ViniDias1' },
  ];

  return (
    <div className="contatos">
        <a href="https://github.com/">
        <img src={github} alt="Github Link" />
        </a>
        <h2>Contatos</h2>
        <ul>
            {contatos.map((contato, index) => (
            <li key={index}>
                <a href={contato.github} target="_blank" rel="noopener noreferrer">
                {contato.nome}
                </a>
            </li>
            ))}
        </ul>
    </div>
  );
};

export default Contato;
