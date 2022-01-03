import { useState } from "react";

function Counter4() {
  // const [value, setValue] = useState(0);
  // const [color, setColor] = useState("red");

  const [state, setState] = useState({ value: 0, color: "red" });
  const { value, color } = state;

  const handlePlus = () => {
    // setValue(value + 1);
    setState((prevState) => ({ ...prevState, value: prevState.value + 1 }));
  };
  const handleMinus = () => {
    //setValue(value - 1);
    setState((prevState) => ({ ...prevState, value: prevState.value - 1 }));
  };

  const handlegreen = () => {
    // setColor("green");
    setState((prevState) => ({ ...prevState, color: "green" }));
  };

  const handleblue = () => {
    //setColor("blue");
    setState((prevState) => ({ ...prevState, color: "blue" }));
  };

  const handlered = () => {
    //setColor("red");
    setState((prevState) => ({ ...prevState, color: "red" }));
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
