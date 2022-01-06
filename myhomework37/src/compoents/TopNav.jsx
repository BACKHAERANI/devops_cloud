import { Link } from 'react-router-dom';

function TopNav() {
  return (
    <div className="my-3">
      <ul className="flex gap-5">
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        <li>
          <NavLink to="/Todos">Todos</NavLink>
        </li>
        <li>
          <NavLink to="/Reviews">Reviews</NavLink>
          {/* <a href="/Reviews">Reviews</a> */}
        </li>
      </ul>
    </div>
  );
}

function NavLink({ to, children }) {
  return (
    <Link
      to={to}
      className="pd-1 text-sm border-red-400 hover:text-red-400 hover:border-b-4 duration-75"
    >
      {children}
    </Link>
  );
}

export default TopNav;
