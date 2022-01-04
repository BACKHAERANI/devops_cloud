import { useState } from "react";

function reducer(action, prevState) {
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
  } else if (type === "SHUFFLE_NUMBERS") {
    return {
      ...prevState,
      numbers: prevState.numbers.sort(() => Math.random() - Math.random()),
    };
  } else if (type === "SHUFFLE_COLORS") {
    return {
      ...prevState,
      colors: prevState.colors.sort(() => Math.random() - Math.random()),
    };
  }
}

function SevenNumbers() {
  const [value, setValue] = useState({
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

  const handlenew = () => {
    const action = { type: "GENERATE_NUMBERS" };
    setValue((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const handlerandom = () => {
    const action = { type: "SHUFFLE_NUMBERS" };
    setValue((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const handlecolor = () => {
    const action = { type: "SHUFFLE_COLORS" };
    setValue((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const changeCircleColor = (circleIndex) => {
    setValue((prevState) => ({
      ...prevState,
      colors: prevState.colors.map((color, index) => {
        if (circleIndex === index) {
          return `#${Math.round(Math.random() * 0xffffff).toString(16)}`;
        } else {
          return color;
        }
      }),
    }));
  };

  const removeCircle = (circleIndex) => {
    setValue((prevState) => ({
      ...prevState,
      numbers: prevState.numbers.filter(
        (number, index) => circleIndex !== index
      ),
      colors: prevState.colors.filter((color, index) => circleIndex !== index),
    }));
  };

  return (
    <div>
      <h2>7개의 숫자</h2>
      {value.numbers.map((number, index) => {
        return (
          <div
            number={number}
            onClick={() => changeCircleColor(index)}
            onContextMenu={(e) => {
              removeCircle(index);
              e.preventDefault();
              console.log("right clicked");
            }}
            style={{ ...defaultStyle, backgroundColor: value.colors[index] }}
          >
            {number}
          </div>
        );
      })}
      <hr />
      <button onClick={handlenew}>랜덤뽑기</button>
      <button onClick={handlerandom}>랜덤섞기</button>
      <button onClick={handlecolor}>컬러섞기</button>
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
