import { useState } from 'react';
import Todo from './Todo';
import 'components/TodoList.css';
import TOdoForm from './TodoForm';
import useFieldvalues from 'hooks/useFieldValues';

const INITIAL_STATE = [
  { content: '자유롭게 살기' },
  { content: '건강해지기' },
  { content: '열심히 살기' },
  { content: '파이썬' },
  { content: '리액트' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const [fieldValues, handleChange, clearFieldValues] = useFieldvalues({
    content: '',
    color: 'Orange',
  });

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  return (
    <div className="todo-list">
      <h1>Todo List</h1>

      <TOdoForm handleChange={handleChange} fieldValues={fieldValues} />
      <hr />
      {JSON.stringify(fieldValues)}

      <button
        className="bg-red-500 text-gray-100 cursor-print"
        onClick={clearFieldValues}
      >
        clear
      </button>

      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} />
      ))}
    </div>
  );
}

export default TodoList;
