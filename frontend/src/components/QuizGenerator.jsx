import { useState } from "react";
import axios from "axios";

function QuizGenerator() {
  const [topic, setTopic] = useState("");
  const [quiz, setQuiz] = useState([]);
  const [loading, setLoading] = useState(false);
  const [answers, setAnswers] = useState({});
  const [score, setScore] = useState(null);
  const [feedback, setFeedback] = useState("");
  const [corrections, setCorrections] = useState([]);

  const generateQuiz = async () => {
  if (!topic.trim()) return;

  try {
    setLoading(true);

    const response = await axios.post(
      "http://127.0.0.1:8000/generate-quiz",
      {
        topic,
        difficulty: "beginner",
        num_questions: 5,
        language: "English",
      }
    );

    console.log(response.data);

    setQuiz(Array.isArray(response.data) ? response.data : []);
  } catch (error) {
    console.error(error);
    alert("Failed to generate quiz");
  } finally {
    setLoading(false);
  }
};

const submitQuiz = async () => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/evaluate-quiz",
      {
        topic,
        quiz,
        user_answers: answers,
        language: "English",
      }
    );

    console.log(response.data);

    setScore(response.data.score);
    setFeedback(response.data.feedback);
    setCorrections(response.data.corrections || []);
  } catch (error) {
    console.error(error);
    alert("Failed to evaluate quiz");
  }
};
  return (
    <div className="bg-white rounded-2xl shadow-lg p-8 mt-6">
      <h2 className="text-2xl font-bold mb-4">
        Quiz Generator
      </h2>

      <input
        type="text"
        placeholder="Enter a topic"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        className="w-full border rounded-lg px-4 py-3"
      />

      <button onClick={generateQuiz}  disabled={loading} className="mt-4 w-full border rounded-lg py-3 font-semibold">
        Generate Quiz
      </button>

      {quiz.length > 0 && (
    <div className="mt-6 space-y-6">
    {quiz.map((question, index) => (
      <div
        key={index}
        className="border rounded-lg p-4"
      >
        <h3 className="font-semibold mb-3">
          {index + 1}. {question.question}
        </h3>

        <div className="space-y-2">
          {question.options.map((option, optionIndex) => (
           <label key={optionIndex} className="flex items-center gap-2 border rounded p-2 cursor-pointer">
            <input type="radio" name={`question-${index}`} value={option} 
            onChange={() => setAnswers((prev) => ({ ...prev, [index]: option }))} />
        
        {option}
    </label>
          ))}
        </div>
      </div>
    ))}
  </div>

  
)}
    <button
    onClick={submitQuiz}
    className="w-full mt-6 rounded-lg py-3 font-semibold border"
    >
    Submit Quiz
    </button>
    {score && (
  <div className="mt-6 border rounded-xl p-6">
    <h2 className="text-2xl font-bold">
      Quiz Result
    </h2>

    <p className="text-xl mt-3">
      Score: {score}
    </p>

    <p className="mt-3">
      {feedback}
    </p>
  </div>
)}
    {score !== null && (
  <div className="mt-6 border rounded-lg p-4">
    <h3 className="text-xl font-bold">
      Score: {score}
    </h3>

    <p className="mt-3 whitespace-pre-wrap">
      {feedback}
    </p>
    
  </div>
)}
    </div>
  );
}

export default QuizGenerator;