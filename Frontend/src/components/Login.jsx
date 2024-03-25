import React from 'react';
import '../style/login.css'

const Login = () => {

  return (
    <div className='login'>
      <div className="content-login">
        <h1>LOGIN</h1>
        <h3>Acesse sua conta</h3>
        <form>
          <input type="email" name="email" placeholder="Email" required /> <br />
          <input type="password" name="password" placeholder="Password" required /> <br />
          <button type="submit">Login</button> <br />
          <button>Quero me cadastrar</button> <br />
        </form>

      </div>

    </div>
  );
};

export default Login;
