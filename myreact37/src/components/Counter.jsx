import { useReducer, useState } from 'react';
import 'components/Counter.css';

function Counter() {
  const [value, setValue] = useState(0);

  const handleUp = () => {
    setValue(value + 1);
  };

  const handleDown = () => {
    setValue(value - 1);
  };

  return (
    <div
      className="counter"
      style={{ backgroundColor: 'red' }}
      onClick={handleUp}
      onContextMenu={handleDown}
    >
      {value}
    </div>
  );
}

export default Counter;
