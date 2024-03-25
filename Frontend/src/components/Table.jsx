import React from 'react';
import '../style/Table.css'

const Table = ({ dados, primeiroAcesso }) => {
  // Verificar se é o primeiro acesso e exibir mensagem encorajadora
  if (primeiroAcesso) {
    return (
      <table id='primeiroacesso'>
        <tbody>
          <tr>
            <td colSpan="6">Utilize os filtros para buscar dados.</td>
          </tr>
        </tbody>
      </table>
    );
  }

  // Verificar se dados é undefined, vazio ou nulo
  if (!dados || dados.length === 0) {
    return (
      <table id='notfound'>
        <tbody>
          <tr>
            <td colSpan="6">Não foram encontrados dados referentes à busca.</td>
          </tr>
        </tbody>
      </table>
    );
  }

  return (
    <div id="container-default">
      <table id='default'>
        <caption>Resultado da Consulta</caption>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Cargo</th>
            <th>Lotação</th>
            <th>Rendimentos</th>
            <th>Descontos</th>
            <th>Líquido</th>
          </tr>
        </thead>
        <tbody>
          {dados.map((funcionario, index) => (
            <tr key={index}>
              <td>{funcionario.nome}</td>
              <td>{funcionario.cargo}</td>
              <td>{funcionario.lotacao}</td>
              <td>R${funcionario.rendimentos}</td>
              <td>R${funcionario.descontos}</td>
              <td>R${funcionario.rendimentos - funcionario.descontos}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>

  );
};

export default Table;
