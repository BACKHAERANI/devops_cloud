function TopNav({ changePage }) {
  return (
    <ul>
      <li>
        <a onClick={() => changePage("Lotto")}>Lotto</a>
      </li>
      <li>
        <a onClick={() => changePage("Profile")}>ProfileCard</a>
      </li>
    </ul>
  );
}

export default TopNav;
