import { useState } from 'react';
import View from 'compoents/Review';
import './Review-list.css';
import usefieldValues from './hooks/useFieldValues';
import ReviewForm from './ReviewForm';

const INITIAL_STATE = [
  {
    id: 1,
    content: '스파이더맨...보고 싶었는데 볼 시간이 없었어요...',
    score: 3,
  },
  { id: 2, content: 'MY...MJ...', score: 4 },
  { id: 3, content: '스파이더맨...도 좋지만...토르', score: 4 },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [form, setForm] = useState(false);
  const [fieldValues, handleChange, clearFieldValues, setFieldValues] =
    usefieldValues({
      content: '',
      score: 5,
    });

  const appendReview = () => {
    let { id: reviewId } = fieldValues;
    if (!reviewId) {
      reviewId = new Date().getTime();
      const createdreview = { ...fieldValues, id: reviewId };
      setReviewList((prevReviewList) => [...prevReviewList, createdreview]);
    } else {
      const editedreview = { ...fieldValues };
      setReviewList((prevReviewList) =>
        prevReviewList.map((review) => {
          if (review.id === editedreview.id) return editedreview;
          return review;
        }),
      );
    }
    clearFieldValues();
  };

  const appendForm = () => {
    setForm((prev) => !prev);
  };

  const deleteReview = (deletingReview) => {
    console.log('Deleting', deletingReview);
    setReviewList((prevReviewList) =>
      prevReviewList.filter((review) => deletingReview.id !== review.id),
    );
  };

  const willEditReview = (editingReview) => {
    console.log('Editing', editingReview);
    setFieldValues(editingReview);
    setForm(true);
  };

  return (
    <div className="Review-list">
      <h1>ReviewList</h1>
      <hr />

      {form && (
        <ReviewForm
          fieldValues={fieldValues}
          handleSubmit={appendReview}
          handleChange={handleChange}
          handleForm={appendForm}
        />
      )}
      {!form && <button onClick={appendForm}>New Review</button>}

      <hr />
      {reviewList.map((review) => (
        <View
          key={review.id}
          review={review}
          handleDelete={() => deleteReview(review)}
          handleEdit={() => willEditReview(review)}
        >
          {review.content}
        </View>
      ))}
    </div>
  );
}

export default ReviewList;
