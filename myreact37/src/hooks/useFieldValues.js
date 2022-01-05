import { useState } from 'react';

function useFieldvalues() {
  const [fieldValues, setFieldValues] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;

    //    함수안쓴버전
    setFieldValues({
      ...fieldValues,
      [name]: value,
    });
  };

  return [fieldValues, handleChange];
}

export default useFieldvalues;
