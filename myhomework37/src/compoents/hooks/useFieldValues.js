import { useState } from 'react';

function useFieldValues(initialFieldValues) {
  const [fieldValues, setFieldValues] = useState(initialFieldValues);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFieldValues((prevFieldValues) => ({
      ...prevFieldValues,
      [name]: value,
    }));
  };

  const clearFieldvalues = () => setFieldValues(initialFieldValues);

  return [fieldValues, handleChange, clearFieldvalues, setFieldValues];
}

export default useFieldValues;
