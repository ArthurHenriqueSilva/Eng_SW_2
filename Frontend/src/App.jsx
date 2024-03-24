import {Landing} from './pages/landing'
import {LoginPage} from './pages/login'
import './style/App.css'
import { Routes, Route } from 'react-router-dom'

function App() {
  return (
    <Routes>
      <Route path='/' element={<Landing />}/>
      <Route path='/Login' element={<LoginPage />}/>
    </Routes>
  )
}

export default App
