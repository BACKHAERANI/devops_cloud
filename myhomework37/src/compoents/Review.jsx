function Review({ review }) {
  return (
    <div
      className="bg-blue-200 
    hover:bg-blue-400 m-1 p-1 rounded-lg text-lg border-blue-200 border-2 
    hover:border-blue-500 
    hover:scale-105 cursor-pointer"
    >
      {review.content}
    </div>
  );
}

export default Review;
