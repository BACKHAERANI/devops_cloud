import { useState } from 'react';
import Todo from 'compoents/Todoreturn';
import './Todo-list.css';
import TodoForm from './TodoForm';
import useFieldValues from 'hook/useFieldValues';

const INITIAL_STATE = [{ content: '파이썬' }, { content: '자바스크립트' }];

function TODO() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);
  const [fieldValues, handlechange, clearFieldValues] = useFieldValues({
    content: '',
    color: 'purple',
  });

  // const [inputText, setInputText] = useState('');

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  // const changedInputText = (e) => {
  //   setInputText(e.target.value);
  // };

  // const appedInputText = (e) => {
  //   if (e.key === 'Enter') {
  //     setTodoList((prevTodoList) => {
  //       return [...prevTodoList, { content: inputText }];
  //     });
  //     setInputText('');
  //   }
  // };

  return (
    <div className="todo-list">
      <h1>TODOLIST</h1>
      <TodoForm fieldValues={fieldValues} handleChange={handlechange} />
      <hr />
      {JSON.stringify(fieldValues)}

      <button
        className="bg-purple-500 text-gray-200 cursor-point"
        onClick={() => clearFieldValues()}
      >
        clear
      </button>
      {/* <input
        type="text"
        value={inputText}
        onChange={changedInputText}
        onKeyPress={appedInputText}
      /> */}
      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)}>
          {todo.content}
        </Todo>
      ))}
    </div>
  );
}

export default TODO;
