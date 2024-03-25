import React, { useState } from 'react';
import {NavLink} from 'react-router-dom'
import '../style/sign.css';

const Sign = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSign = async (e) => {
        e.preventDefault();

        const formData = {
            name: name,
            email: email,
            password: password
        };

        try {
            const response = await fetch('http://localhost:5000/users', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const responseData = await response.json();
      
            if (response.ok) {
                console.log(responseData.user_created.message);
            } else {
                console.error(responseData.error);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div className='sign'>
            <div className="content-sign">
                <h1>CADASTRO</h1>
                <h3>Crie sua conta</h3>
                <form onSubmit={handleSign}>
                    <input 
                        type="text" 
                        name="name" 
                        placeholder="Nome" 
                        value={name} 
                        onChange={(e) => setName(e.target.value)} 
                        required 
                    /> <br />
                    <input 
                        type="email" 
                        name="email" 
                        placeholder="Email" 
                        value={email} 
                        onChange={(e) => setEmail(e.target.value)} 
                        required 
                    /> <br />
                    <input 
                        type="password" 
                        name="password" 
                        placeholder="Senha" 
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)} 
                        required 
                    /> <br />
                    <button type="submit">Cadastrar</button> <br />
                    <NavLink to='/Login'>
                        <button>Ja possuo uma conta</button>
                    </NavLink>
                </form>
            </div>
        </div>
    );
};

export default Sign;
