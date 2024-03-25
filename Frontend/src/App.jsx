import {Landing} from './pages/landing'
import {LoginPage} from './pages/login'
import {Consulta} from './pages/consulta'
import {ContatoPage} from './pages/contato'
import {ServicoPage} from './pages/servico'

import './style/App.css'
import { Routes, Route } from 'react-router-dom'

function App() {
  return (
    <Routes>
      <Route path='/' element={<Landing />}/>
      <Route path='/Login' element={<LoginPage />}/>
      <Route path='/Consulta' element={<Consulta/>}/>
      <Route path='/Contato' element={<ContatoPage/>}/>
      <Route path='/Servico' element={<ServicoPage/>}/>
    </Routes>
  )
}

export default App
