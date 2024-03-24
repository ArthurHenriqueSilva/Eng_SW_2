import React from 'react';
import '../style/login.css'

const Login = () => {

  return (
    <div className='login'>
      <div className="content-login">
        <h2>Login</h2>
        <form>
          <input type="email" name="email" placeholder="Email" required />
          <input type="password" name="password" placeholder="Password" required />
          <button type="submit">Login</button>
          <button>Quero me cadastrar</button>
        </form>

      </div>

    </div>
  );
};

export default Login;
