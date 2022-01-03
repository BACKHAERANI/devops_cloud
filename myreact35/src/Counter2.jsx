import { useState } from "react";

function reducer(action, prevState) {
  const { type, amount } = action;
  if (type === "PLUS") {
    return prevState + amount;
  } else if (type === "MINUS") {
    return prevState - amount;
  }
}

function reducer_color(action, prevState) {
  const { type, color } = action;
  if (type === "CHANGE_COLOR") {
    return color;
  }
}

function Counter2() {
  const [value, setValue] = useState(0);

  const handlePlus = () => {
    const action = { type: "PLUS", amount: 1 };
    setValue((preValue) => {
      return reducer(action, preValue);
    });
  };

  const handleMinus = () => {
    const action = { type: "MINUS", amount: 1 };
    setValue((preValue) => {
      return reducer(action, preValue);
    });
  };

  const [color, setColor] = useState("red");

  const handlegreen = () => {
    const action = { type: "CHANGE_COLOR", color: "green" };
    setColor((preValue) => {
      return reducer_color(action, preValue);
    });
  };

  const handleblue = () => {
    const action = { type: "CHANGE_COLOR", color: "blue" };
    setColor((preValue) => {
      return reducer_color(action, preValue);
    });
  };

  const handlered = () => {
    const action = { type: "CHANGE_COLOR", color: "red" };
    setColor((preValue) => {
      return reducer_color(action, preValue);
    });
  };

  return (
    <div>
      <h2>Counter2</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
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

export default Counter2;
