import axios from "axios";

const API_BASE_URL = "http://localhost:5000/api";

export const calculateString = async (input) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/calculate`, { input });
    return response.data.result;
  } catch (error) {
    throw new Error(error.response?.data?.error || "Server Error");
  }
};
