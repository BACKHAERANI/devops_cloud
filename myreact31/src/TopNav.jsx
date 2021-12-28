function TopNav({ changePage }) {
  return (
    <ul>
      <li>
        <a onClick={() => changePage("Lotto")}>Lotto</a>
      </li>
      <li>
        <a onClick={() => changePage("Profile1")}>ProfileCard</a>
      </li>
    </ul>
  );
}

export default TopNav;
