import 'components/Todo.css';

function Todo({ todo, onClick }) {
  return (
    <div
      className={`bg-${todo.color}-100 
      hover:bg-${todo.color}-400 m-1 p-1 rounded-lg text-lg border-purple-300 border-2 
      hover:border-purple-600 
      hover:scale-105 cursor-pointer`}
      onClick={onClick}
    >
      {todo.content}
      {todo.color}
    </div>
  );
}

export default Todo;
