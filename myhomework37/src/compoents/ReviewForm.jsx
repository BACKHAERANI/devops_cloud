function ReviewForm({ fieldValues, handleChange, handleSubmit, handleForm }) {
  return (
    <div>
      <h3>평점</h3>
      <select onChange={handleChange} name="score">
        <option>{0}</option>
        <option>{1}</option>
        <option>{2}</option>
        <option>{3}</option>
        <option>{4}</option>
        <option>{5}</option>
      </select>
      <h3>리뷰</h3>
      <textarea
        type="text"
        onChange={handleChange}
        name="content"
        value={fieldValues.content}
      ></textarea>
      <hr />
      <button
        onClick={() => {
          handleSubmit();
          handleForm();
        }}
      >
        저장하기
      </button>
    </div>
  );
}

export default ReviewForm;
