import { useState } from 'react';
import View from 'compoents/Review';
import './Review-list.css';
import usefieldValues from './hooks/useFieldValues';
import ReviewForm from './ReviewForm';

const Basic_Review = [
  { content: '스파이더맨...보고 싶었는데 볼 시간이 없었어요...' },
  { content: 'MY...MJ...' },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(Basic_Review);
  const [fieldValues, handleChange, clearFieldValues] = usefieldValues({
    content: '',
  });

  const appendReview = () => {
    const review = { ...fieldValues };
    setReviewList((prevReviewList) => [...prevReviewList, review]);
    clearFieldValues();
  };

  return (
    <div className="Review-list">
      <h1>ReviewList</h1>
      <hr />
      <ReviewForm
        fieldValues={fieldValues}
        handleSubmit={appendReview}
        handleChange={handleChange}
      >
        New Review
      </ReviewForm>
      <hr />
      {reviewList.map((review) => (
        <View review={review}>{review.content}</View>
      ))}
    </div>
  );
}

export default ReviewList;
