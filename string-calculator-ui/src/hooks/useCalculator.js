import { useState } from "react";
import { calculateString } from "../services/apiService";

export const useCalculator = () => {
  const [input, setInput] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleCalculate = async () => {
    try {
      const response = await calculateString(input);
      setResult(response);
      setError("");
    } catch (err) {
      setError(err.message);
    }
  };

  return { input, setInput, result, error, handleCalculate };
};
