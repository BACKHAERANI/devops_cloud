import {useState} from 'react';

function Lotto_Random_Number({color}){
  const [numberList, setNumberList] = useState([]);

  const lotto_random_number = () => {
    let lottoList = [];

    for (let i = 0; i < 7; i++) {
      let randomN = Math.floor(Math.random() * 44) + 1;

      for (const l in lottoList) {
        if (randomN == lottoList[l]) {
          randomN = Math.floor(Math.random() * 44) + 1;
        }
      }
      lottoList.push(randomN);
    }
    lottoList.sort((a, b) => a - b);
    return lottoList;
  };

const handleClick = () => {
  setNumberList(lotto_random_number); 
};

return (
  <>
<button onClick={handleClick}>Clikck</button>

{numberList.map((number)=>(
<div style={{...style, backgroundColor: color}}> {number} </div>))}
  </>
);
}

const style = {
  width: "100px",
  height: "100px",
  borderRadius: "50px",
  lineHeight: "100px",
  textAlign: "center",
  display: "inline-block",
  fontSize: "3rem",
  margin: "1rem",
  userSelect: "none",
};

export default Lotto_Random_Number;