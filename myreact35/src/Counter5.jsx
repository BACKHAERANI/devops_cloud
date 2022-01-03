import { useReducer } from "react";

function reducer(prevstate, action) {
  const { type, amount, color } = action;
  if (type === "PLUS") {
    return { ...prevstate, value: prevstate.value + amount };
  } else if (type === "MINUS") {
    return { ...prevstate, value: prevstate.value - amount };
  } else if (type === "CHANGE_COLOR") {
    return { ...prevstate, color };
  }
}

function Counter5() {
  const [state, dispatch] = useReducer(reducer, {
    value: 0,
    color: "red",
  });

  const handlePlus = () => {
    dispatch({ type: "PLUS", amount: 1 });
  };

  const handleMinus = () => {
    dispatch({ type: "MINUS", amount: 1 });
  };

  const handleColor = (color) => {
    dispatch({ type: "CHANGE_COLOR", color: color });
  };

  return (
    <>
      <h2>Counter6</h2>

      <div style={{ ...defaultStyle, backgroundColor: state.color }}>
        {state.value}
      </div>

      <hr />

      <button onClick={handlePlus}>Plus</button>
      <button onClick={handleMinus}>Minus</button>

      <button onClick={() => handleColor("red")}>Red</button>
      <button onClick={() => handleColor("green")}>Green</button>
      <button onClick={() => handleColor("blue")}>Blue</button>
    </>
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

export default Counter5;
