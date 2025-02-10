import React from "react";
import { useCalculator } from "../hooks/useCalculator";

function Calculator() {
  const { input, setInput, result, error, handleCalculate } = useCalculator();

  return (
    <div className="calculator">
      <h2>String Calculator</h2>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={handleCalculate}>Calculate</button>
      {result !== null && <h3>Result: {result}</h3>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}

export default Calculator;
