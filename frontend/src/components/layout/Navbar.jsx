import { NavLink } from 'react-router-dom';

const links = [
  { to: '/', label: '🏠' },
  { to: '/dashboard', label: 'Dashboard' },
  { to: '/salary', label: 'Salary' },
  { to: '/budget', label: 'Budget' }
];

const NavBar = () => (
  <nav className="flex justify-center bg-sky-300 p-4 space-x-12 sticky top-0 shadow-md">
    {links.map(({ to, label }) => (
      <NavLink
        key={to}
        to={to}
        className={({ isActive }) => 
          isActive ? 'border-b-2 pb-1' : 'pb-1'
        }
      >
        {label}
      </NavLink>
    ))}
  </nav>
);

export default NavBar;
