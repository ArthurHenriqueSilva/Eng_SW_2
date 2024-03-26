import React, { useState } from 'react';
import {NavLink} from 'react-router-dom'
import '../style/login.css';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();

    const formData = {
      email: email,
      password: password
    };

    try {
      const response = await fetch('http://localhost:5000/login', {
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
    <div className='login'>
      <div className="content-login">
        <h1>LOGIN</h1>
        <h3>Acesse sua conta</h3>
        <form onSubmit={handleLogin}>
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
            placeholder="Password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            required 
          /> <br />
          <button type="submit">Login</button> <br />
          <NavLink to='/Sign'>
            <button>Quero me cadastrar</button> <br />
          </NavLink>
        </form>
      </div>
    </div>
  );
};

export default Login;
