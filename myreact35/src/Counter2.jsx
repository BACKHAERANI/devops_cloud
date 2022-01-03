import { useState } from "react";

function dispatch(action, prevState) {
  const { type, amount } = action;
  if (type === "PLUS") {
    return prevState + amount;
  } else if (type === "MINUS") {
    return prevState - amount;
  }
}

function Counter2() {
  const [value, setValue] = useState(0);

  const handlePlus = () => {
    const action = { type: "PLUS", amount: 1 };
    setValue((preValue) => {
      return dispatch(action, preValue);
    });
  };

  const handleMinus = () => {
    const action = { type: "MINUS", amount: 1 };
    setValue((preValue) => {
      return dispatch(action, preValue);
    });
  };

  return (
    <div>
      <h2>Counter2</h2>
      {value}
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
    </div>
  );
}

export default Counter2;
