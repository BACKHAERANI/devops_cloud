import { useState } from "react";

function dispatch_color(action, prevState) {
  const { type, color } = action;
  if (type === "CHANGE_COLOR") {
    return color;
  }
}

function Counter3() {
  const [color, setColor] = useState("red");

  const handlegreen = () => {
    const action = { type: "CHANGE_COLOR", color: "green" };
    setColor((preValue) => {
      return dispatch_color(action, preValue);
    });
  };

  const handleblue = () => {
    const action = { type: "CHANGE_COLOR", color: "blue" };
    setColor((preValue) => {
      return dispatch_color(action, preValue);
    });
  };

  const handlered = () => {
    const action = { type: "CHANGE_COLOR", color: "red" };
    setColor((preValue) => {
      return dispatch_color(action, preValue);
    });
  };

  return (
    <div style={{ backgroundColor: color }}>
      <h2>Counter3</h2>
      {color}
      <hr />
      <button onClick={handlegreen}>초록</button>
      <button onClick={handleblue}>파랑</button>
      <button onClick={handlered}>빨강</button>
    </div>
  );
}

export default Counter3;
