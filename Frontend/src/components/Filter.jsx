import React from 'react';
import { NavLink } from 'react-router-dom';
import '../style/Filter.css';
import logo from '../assets/tjba.png';
import search from '../assets/search-icon.svg'
import sort from '../assets/sort.svg'

const Filter = () => {
  return (
    <div className="contentFilter">
        <form action="">
            <div id='l1'>
                
                <input type="text" name="" id="" placeholder='Nome'/>
                <button id='sort'>
                    <img src={sort} alt="" />
                </button>
                <label htmlFor="">Faixa Salarial:</label>
                <input type='number' name="" id="" placeholder='R$ XX.XXX,XX'/> 
                <label htmlFor="">ate</label>
                <input type="number" placeholder='R$ XX.XXX,XX'/>
                <button id='search'>
                    <img src={search} alt="" />
                </button>
            </div>

            <div id='l2'>
                <select name="" id="">
                    <option value="">Ano...</option>              
                </select>
                <select name="" id="">
                    <option value="">Mes...</option>
                </select>
                <select name="" id="">
                    <option value="">Lotacao...</option>
                </select>
                <select name="" id="">
                    <option value="">
                        Cargo...
                    </option>
                </select>
                <input type="checkbox" name="diaria" id=""/>
                <label htmlFor="diaria">Possui diaria</label>
                <input type="checkbox" name="" id="" />
                <label htmlFor="diaria">Possui gratificacao</label>
            </div>



        </form> 
    </div>
    
  );
}

export default Filter;
