import { useState } from 'react';

function useFieldvalues(initialFieldValues) {
  const [fieldValues, setFieldValues] = useState(initialFieldValues);

  const clearFieldValues = () => setFieldValues(initialFieldValues);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFieldValues((prevFieldValues) => ({
      ...prevFieldValues,
      [name]: value,
    }));

    //    함수안쓴버전
    // setFieldValues({
    //   ...fieldValues,
    //   [name]: value,
    // });
  };

  return [fieldValues, handleChange, clearFieldValues];
}

export default useFieldvalues;
