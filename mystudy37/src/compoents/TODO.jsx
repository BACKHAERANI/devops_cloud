import { useState } from 'react';

const INITIAL_STATE = [{ content: '파이썬' }, { content: '자바스크립트' }];

function TODO() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  return (
    <div>
      <h1>TODOLIST</h1>
      {todoList.map((todo, index) => (
        <div onClick={() => removeTodo(index)}>{todo.content}</div>
      ))}
    </div>
  );
}

export default TODO;
