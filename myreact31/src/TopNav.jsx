function TopNav({ changePage }) {
  return (
    <ul>
      <li>
        <a onClick={() => changePage("Lotto")}>Lotto</a>
      </li>
      <li>
        <a onClick={() => changePage("Profile1")}>ProfileCard1</a>
      </li>
      <li>
        <a onClick={() => changePage("Profile2")}>ProfileCard2</a>
      </li>
      <li>
        <a onClick={() => changePage("Profile3")}>ProfileCard3</a>
      </li>
      <li>
        <a onClick={() => changePage("Profile4")}>ProfileCard4</a>
      </li>
    </ul>
  );
}

export default TopNav;
