import './Todo.css';

function Todo({ todo, onClick }) {
  return (
    <div
      className="m-1 p-1 rounded-lg text-lg border-blue-200 border-2 hover:border-blue-500 hover:scale-105 cursor-pointer"
      onClick={onClick}
      style={{ backgroundColor: todo.color }}
    >
      {todo.content}_{todo.color}
    </div>
  );
}

export default Todo;
