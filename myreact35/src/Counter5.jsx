import { useReducer } from "react";

function reducer(state, action) {
  switch (action.type) {
    case "PLUS":
      return state + 1;
    case "MINUS":
      return state - 1;
    default:
      return state;
  }
}

function Counter5() {
  const [number, dispatch] = useReducer(reducer, 0);

  const handlePlus = () => {
    dispatch({ type: "PLUS" });
  };

  const handleMinus = () => {
    dispatch({ type: "MINUS" });
  };

  // const handlegreen = () => {
  //   dispatch({ type: "color" });
  // };

  return (
    <div>
      <h1>Counter5</h1>
      <span>{number}</span>
      <hr />
      <button onClick={handlePlus}>+1</button>
      <button onClick={handleMinus}>-1</button>
      <hr />
      {/* <button onClick={handlegreen}>초록</button> */}
      {/* <button onClick={handleblue}>파랑</button>
      <button onClick={handlered}>빨강</button> */}
    </div>
  );
}

export default Counter5;
