import 'Circle.css';
import { useState } from 'react';

function Circle({ number, backgroundColor, onClick, onContextMenu }) {
  return (
    <div
      className="circle"
      style={{ backgroundColor }}
      onClick={onClick}
      onContextMenu={onContextMenu}
    >
      {number}
    </div>
  );
}

export default Circle;
