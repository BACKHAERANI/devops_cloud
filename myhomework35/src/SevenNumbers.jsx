import { useReducer } from "react";

function SevenNumbers() {
  const [state, dispatch] = useReducer(reducer, {
    numbers: [0, 0, 0, 0, 0, 0, 0],
    colors: [
      "#1B62BF",
      "#1755A6",
      "#37A647",
      "#F29F05",
      "#F23838",
      "purple",
      "pink",
    ],
  });

  return (
    <div>
      <h2>7개의 숫자</h2>
      {numbers.map((number, index) => {
        return (
          <div
            style={{ ...defaultStyle, backgroundColor: state.colors[index] }}
          >
            {number}
          </div>
        );
      })}
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

export default SevenNumbers;
