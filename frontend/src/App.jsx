import { Routes, Route } from 'react-router-dom';
import NavBar from "./components/layout/Navbar";
import Dashboard from './pages/Dashboard';
import Salary from './pages/Salary';
import Budget from './pages/Budget';

function App() {
  return (
    <div>
      <NavBar />
      <Routes>
        <Route path='/' element={<h1 className="text-4xl text-center mt-8"> Budget App </h1>} />
        <Route path='/dashboard' element={<Dashboard />} />
        <Route path='/salary' element={<Salary />} />
        <Route path='/budget' element={<Budget />} />
        
      </Routes>
    </div>
  )
}

export default App
