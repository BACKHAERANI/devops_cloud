import { useState } from 'react';

const INITIAL_STATE = [{ content: '파이썬' }, { content: '자바스크립트' }];

function TODO() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);
  const [inputText, setInputText] = useState('');

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  const changedInputText = (e) => {
    setInputText(e.target.value);
  };

  const appedInputText = (e) => {
    setTodoList((prevTodoList) => {
      return [...prevTodoList, { content: inputText }];
    });
    setInputText('');
  };

  return (
    <div>
      <h1>TODOLIST</h1>
      <input
        type="text"
        value={inputText}
        onChange={changedInputText}
        onKeyPress={appedInputText}
      />
      {todoList.map((todo, index) => (
        <div onClick={() => removeTodo(index)}>{todo.content}</div>
      ))}
    </div>
  );
}

export default TODO;
