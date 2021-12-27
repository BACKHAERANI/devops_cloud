import { useState } from "react";

function makeLottoNumbers() {
  const lottolist = [];

  for (let i = 0; i < 7; i++) {
    const number = Math.floor(Math.random() * 45) + 1;
    if (lottolist.indexOf(number) === -1) {
      lottolist.push(number);
    } else {
      i--;
    }
  }
  lottolist.sort((a, b) => a - b);
  return lottolist;
}

function PageLotto() {
  const [numbers, setNumbers] = useState([]);

  const handleClick = () => {
    setNumbers(makeLottoNumbers());
  };

  return (
    <div>
      <h2>Lotto</h2>
      <button onClick={handleClick}>예지</button>
      <hr />
      {numbers.map((number) => {
        return <span style={{ marginRight: "5rem" }}>{number}</span>;
      })}
    </div>
  );
}

export default PageLotto;
