import { useState } from "react";

function Counter4() {
  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  const handlePlus = () => {
    // setValue(value + 1);
    setValue((preValue) => preValue + 1);
  };
  const handleMinus = () => {
    //setValue(value - 1);
    setValue((preValue) => preValue - 1);
  };

  const handlegreen = () => {
    // setColor("green");
    setColor(() => "green");
  };

  const handleblue = () => {
    //setColor("blue");
    setColor(() => "blue");
  };

  const handlered = () => {
    //setColor("red");
    setColor(() => "red");
  };

  return (
    <div>
      <h2>Counter</h2>
      <span style={{ ...defaultStyle, backgroundColor: color }}>{value}</span>
      <hr />
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>
      <hr />
      <button onClick={handlegreen}>초록</button>
      <button onClick={handleblue}>파랑</button>
      <button onClick={handlered}>빨강</button>
    </div>
  );
}

const defaultStyle = {
  width: "100px",
  height: "100px",
  borderRadius: "50px",
  lineHeight: "100px",
  textAlign: "center",
  display: "inline-block",
  fontSize: "3rem",
  userSelect: "none",
};

export default Counter4;
