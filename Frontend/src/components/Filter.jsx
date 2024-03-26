import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import CurrencyFormat from 'react-currency-format'
import '../style/Filter.css';
import searchIcon from '../assets/search-icon.svg';
import sortIcon from '../assets/sort.svg';

const Filter = ({ setDados }) => {
  const [nome, setNome] = useState('');
  const [faixaSalarialInicio, setFaixaSalarialInicio] = useState('');
  const [faixaSalarialFim, setFaixaSalarialFim] = useState('');
  const [ano, setAno] = useState('');
  const [mes, setMes] = useState('');
  const [lotacao, setLotacao] = useState('');
  const [cargo, setCargo] = useState('');
  const [possuiDiaria, setPossuiDiaria] = useState(false);
  const [possuiGratificacao, setPossuiGratificacao] = useState(false);
  const history = useNavigate();

  const formatarMoeda = (value) => {
    if (!value) return '';
    const digitsOnly = value.replace(/[^\d]/g, '');

    const formattedValue = Number(digitsOnly).toLocaleString('pt-BR', {
      style: 'currency',
      currency: 'BRL',
      minimumFractionDigits: 2,
    });

    return formattedValue;
  };

  const handleSearch = (e) => {
    e.preventDefault();
  
    const queryParams = {
      nome,
      lim_inferior_remun: formatarMoeda(faixaSalarialInicio),
      lim_superior_remun: formatarMoeda(faixaSalarialFim),
      ano,
      mes,
      lotacao,
      cargo,
      diaria: possuiDiaria,
      gratificacao: possuiGratificacao,
    };
  
    fetch('http://localhost:5000/consulta', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(queryParams),
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(data => {
        setDados(data);
        history.push(`/search`);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  };

  return (
    <div className="contentFilter">
      <form onSubmit={handleSearch}>
      <div id="l1">
          <input
            className='text'
            type="text"
            placeholder="Nome"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
          />
          <button type="button" id="sort">
            <img src={sortIcon} alt="" />
          </button>
          <label>Faixa Salarial:</label>
          <CurrencyFormat
            thousandSeparator="."
            decimalSeparator=","
            prefix="R$ "
            placeholder="R$ XX.XXX,XX"
            value={faixaSalarialInicio}
            onValueChange={({ formattedValue, value }) => setFaixaSalarialInicio(value)}
          />
          <label>até</label>
          <CurrencyFormat
            thousandSeparator="."
            decimalSeparator=","
            prefix="R$ "
            placeholder="R$ XX.XXX,XX"
            value={faixaSalarialFim}
            onValueChange={({ formattedValue, value }) => setFaixaSalarialFim(value)}
          />
          <button type="submit" id="search">
            <img src={searchIcon} alt="" />
          </button>
        </div>

        <div id="l2">
          <select value={ano} onChange={(e) => setAno(e.target.value)}>
            <option value="">Ano...</option>
          </select>
          <select value={mes} onChange={(e) => setMes(e.target.value)}>
            <option value="">Mês...</option>
          </select>
          <select value={lotacao} onChange={(e) => setLotacao(e.target.value)}>
            <option value="">Lotação...</option>
          </select>
          <select value={cargo} onChange={(e) => setCargo(e.target.value)}>
            <option value="">Cargo...</option>
          </select>
          <input
            type="checkbox"
            id="diaria"
            checked={possuiDiaria}
            onChange={(e) => setPossuiDiaria(e.target.checked)}
          />
          <label htmlFor="diaria">Possui diária</label>
          <input
            type="checkbox"
            id="gratificacao"
            checked={possuiGratificacao}
            onChange={(e) => setPossuiGratificacao(e.target.checked)}
          />
          <label htmlFor="gratificacao">Possui gratificação</label>
        </div>
      </form>
    </div>
  );
};

export default Filter;
