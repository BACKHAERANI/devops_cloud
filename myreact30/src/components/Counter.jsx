import {useState} from 'react';

function Counter({initial, color}) {
  const [value, setValue] = useState(initial);
  const handleClick = () => {
  setValue(value+1);
};
  const handleContextMenu = (e) =>{
    e.preventDefault();
    setValue(value-1);
  };
  return( <div 
    style={{...style, backgroundColor: color}} 
    onClick={handleClick}
    onContextMenu={handleContextMenu}>
    {value}</div>
    )}

    const style = {
      width: "100px",
      height: "100px",
      borderRadius: "20px",
      lineHeight: "100px",
      textAlign: "center",
      display: "inline-block",
      fontSize: "3rem",
      margin: "1rem",
      userSelect: "none",
    };

export default Counter;


