import { useState } from 'react';
import Todo from './Todo';
import 'components/TodoList.css';
import TOdoForm from './TodoForm';
import useFieldvalues from 'hooks/useFieldValues';

const INITIAL_STATE = [
  { content: '자유롭게 살기', color: 'red' },
  { content: '건강해지기', color: 'purple' },
  { content: '열심히 살기', color: 'red' },
  { content: '파이썬', color: 'purple' },
  { content: '리액트', color: 'blue' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const [fieldValues, handleChange, clearFieldValues] = useFieldvalues({
    content: '',
    color: 'orange',
  });

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  const todo = { ...fieldValues };

  const appendTodo = () => {
    console.log('새로운 todo를 추가하겠습니다.');

    // setter에 값 지정방식
    // setTodoList([...todoList, todo]);
    // clearFieldValues();

    //함수방식

    setTodoList((prevTodoList) => [...prevTodoList, todo]);
    clearFieldValues();
  };

  return (
    <div className="todo-list">
      <h1>Todo List</h1>

      <TOdoForm
        handleChange={handleChange}
        fieldValues={fieldValues}
        handleSubmit={appendTodo}
      />
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
