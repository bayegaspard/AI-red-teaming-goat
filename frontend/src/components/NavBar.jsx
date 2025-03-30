import { Link } from "react-router-dom";

function NavBar() {
  return (
    <nav>
      <Link to="/">Home</Link> | <Link to="/lesson1">Lesson 1: Prompt Injection</Link>
    </nav>
  );
}

export default NavBar;
