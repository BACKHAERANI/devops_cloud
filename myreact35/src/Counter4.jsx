import { useState } from "react";

function reducer(action, prevState) {
  const { type, amount, color } = action;
  if (type === "PLUS") {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === "MINUS") {
    return { ...prevState, value: prevState.value - amount };
  } else if (type === "CHANGE_COLOR") {
    return { ...prevState, color };
  }
}
// function reducer_color(action, prevState) {
//   const { type, color } = action;
//   if (type === "CHANGE_COLOR") {
//     return { ...prevState, color };
//   }
// }

function Counter4() {
  // const [value, setValue] = useState(0);
  // const [color, setColor] = useState("red");

  const [state, setState] = useState({ value: 0, color: "red" });
  const { value, color } = state;

  const handlePlus = () => {
    // setValue(value + 1);
    // setState((prevState) => ({ ...prevState, value: prevState.value + 1 }));
    const action = { type: "PLUS", amount: 1 };
    setState((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const handleMinus = () => {
    //setValue(value - 1);
    // setState((prevState) => ({ ...prevState, value: prevState.value - 1 }));
    const action = { type: "MINUS", amount: 1 };
    setState((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const handlegreen = () => {
    // setColor("green");
    const action = { type: "CHANGE_COLOR", color: "green" };
    setState((preValue) => {
      return reducer(action, preValue);
    });
  };

  const handleblue = () => {
    //setColor("blue");
    // setState((prevState) => ({ ...prevState, color: "blue" }));
    const action = { type: "CHANGE_COLOR", color: "blue" };
    setState((preValue) => {
      return reducer(action, preValue);
    });
  };

  const handlered = () => {
    //setColor("red");
    // setState((prevState) => ({ ...prevState, color: "red" }));
    const action = { type: "CHANGE_COLOR", color: "red" };
    setState((preValue) => {
      return reducer(action, preValue);
    });
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
