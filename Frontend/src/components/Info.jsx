import React from 'react';
import '../style/Info.css';

const Info = () => {
  return (
    <div className="info">
      <div className="content-info">
        <h2>Folha de Pagamento</h2>
        <p>Pesquise na base de dados do Tribunal de Justiça da Bahia</p>
        <p>Utilize Filtros para navegar na folha de pagamento do TJBA.</p>
        <p>Cadastre-se e tenha acesso as consultas favoritas!</p>
        <button id='btn'>Acessar a ferramenta</button>
      </div>
    </div>
  );
}

export default Info;
