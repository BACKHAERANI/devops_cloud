function TodoForm({ fieldValues, handleChange }) {
  return (
    <div>
      <h2>TodoForm</h2>

      <input
        type="text"
        className="border-2 border-gray-200"
        onChange={handleChange}
        name="content"
        value={fieldValues.content}
      />

      <select onChange={handleChange} name="color" value={fieldValues.color}>
        <option>Amber</option>
        <option>Orange</option>
        <option>Yellow</option>
      </select>
    </div>
  );
}

export default TodoForm;
