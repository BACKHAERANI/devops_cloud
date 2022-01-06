import Star from 'compoents/Star';
import { useState } from 'react';

function Review({ review }) {
  const [showMenu, setShowMenu] = useState(false);

  return (
    <div
      onMouseEnter={() => setShowMenu(true)}
      onMouseLeave={() => setShowMenu(false)}
      className="bg-white 
    hover:bg-green-200 m-1 p-1 pt-4  border-green-200 border-2 
    hover:border-green-500 relative "
    >
      {showMenu && (
        <div className="text-xs absolute top-0 right-0 hover:cursor-pointer ">
          <span className="mr-1 text-blue-700 hover:bg-blue-400">수정</span>
          <span className="text-red-500 hover:bg-red-300">삭제</span>
        </div>
      )}

      {review.content}
      <Star score={review.score} />
    </div>
  );
}

export default Review;
