import { useReducer } from "react";

function reducer(prevState, action) {
  const { type } = action;
  if (type === "GENERATE_NUMBERS") {
    let randomNumber = [];

    for (let i = 0; i < 7; i++) {
      let number = Math.floor(Math.random() * 45) + 1;
      if (randomNumber.indexOf(number) === -1) {
        randomNumber.push(number);
      } else {
        i--;
      }
    }
    randomNumber.sort((a, b) => a - b);
    return { ...prevState, numbers: randomNumber };
  }
}

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
      {state.numbers.map((number, index) => {
        return (
          <div
            style={{ ...defaultStyle, backgroundColor: state.colors[index] }}
          >
            {number}
          </div>
        );
      })}
      <hr />
      <button onClick={() => dispatch({ type: "GENERATE_NUMBERS" })}>
        랜덤뽑기
      </button>
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
