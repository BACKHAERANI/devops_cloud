function TodoForm({ fieldValues, handleChange, handleSubmit }) {
  const hanleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div className="border-2 border-purple-300 p-3">
      <h2 className="text-lg underline">TodoForm</h2>

      <select onChange={handleChange} name="color" value={fieldValues.color}>
        <option>purple</option>
        <option>orange</option>
        <option>yellow</option>
      </select>

      <input
        type="text"
        className="border-2 border-gray-200"
        onChange={handleChange}
        onKeyPress={hanleKeyPress}
        name="content"
        value={fieldValues.content}
      />
    </div>
  );
}

export default TodoForm;
