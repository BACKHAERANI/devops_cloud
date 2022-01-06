import Star from 'compoents/Star';

function Review({ review }) {
  return (
    <div
      className="bg-white-200 
    hover:bg-green-400 m-1 p-1  border-green-200 border-2 
    hover:border-green-300 
    hover:cursor-pointer"
    >
      {review.content}
      <Star />
    </div>
  );
}

export default Review;
