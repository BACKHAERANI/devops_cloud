import { useReducer, useState } from 'react';
import './Counter.css';

const ACTION_TYPES = {
  INCREASE: 'INCREASE',
  DECREASE: 'DECREASE',
};

function reducer(prevState, action) {
  const { type } = action;
  if (type === ACTION_TYPES.INCREASE) {
    return prevState + 1;
  }
  return prevState; // 방어
}

function Counter() {
  // const [value, setValue] = useState(0);
  const [value, dispatch] = useReducer(reducer, 0);

  const handleClick = () => {
    // setValue((prevValue) => prevValue + 1);
    dispatch({ type: ACTION_TYPES.INCREASE });
  };

  const handleRightClick = (e) => {
    e.preventDefault();
    // setValue((prevValue) => prevValue - 1);
    dispatch({ type: ACTION_TYPES.DECREASE });
  };

  return (
    <div
      className="counter"
      style={{ backgroundColor: 'red' }}
      onClick={handleClick}
      onContextMenu={handleRightClick}
    >
      {value}
    </div>
  );
}

export default Counter;
