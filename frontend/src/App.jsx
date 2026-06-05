import { useState } from "react";
import axios from "axios";
import QuizGenerator from "./components/QuizGenerator";

function App() {
  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState("beginner");
  const [language, setLanguage] = useState("English");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askAI = async () => {
    if (!topic.trim()) return;

    try {
      setLoading(true);
      setAnswer("");

      const response = await axios.post(
        "http://127.0.0.1:8000/ask-ai",
        {
          topic,
          difficulty,
          explanation_type: "simple",
          language,
        }
      );

      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100 p-6">
      <div className="max-w-4xl mx-auto">

        <div className="bg-white rounded-2xl shadow-lg p-8">

          <h1 className="text-4xl font-bold mb-2">
            AI Study Assistant
          </h1>

          <p className="text-gray-500 mb-8">
            Learn faster with AI-powered explanations.
          </p>

          <div className="space-y-5">

            <div>
              <label className="block mb-2 font-medium">
                Topic
              </label>

              <input
                type="text"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
                placeholder="Example: Python Functions"
                className="w-full border rounded-lg px-4 py-3"
              />
            </div>

            <div className="grid md:grid-cols-2 gap-4">

              <div>
                <label className="block mb-2 font-medium">
                  Difficulty
                </label>

                <select
                  value={difficulty}
                  onChange={(e) => setDifficulty(e.target.value)}
                  className="w-full border rounded-lg px-4 py-3"
                >
                  <option value="beginner">Beginner</option>
                  <option value="intermediate">Intermediate</option>
                  <option value="advanced">Advanced</option>
                </select>
              </div>

              <div>
                <label className="block mb-2 font-medium">
                  Language
                </label>

                <select
                  value={language}
                  onChange={(e) => setLanguage(e.target.value)}
                  className="w-full border rounded-lg px-4 py-3"
                >
                  <option value="English">English</option>
                  <option value="Arabic">Arabic</option>
                  <option value="French">French</option>
                </select>
              </div>

            </div>

            <button
              onClick={askAI}
              disabled={loading}
              className="w-full rounded-lg py-3 font-semibold border"
            >
              {loading ? "Thinking..." : "Ask AI"}
            </button>

          </div>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-8 mt-6">

          <h2 className="text-2xl font-bold mb-4">
            Response
          </h2>
          {answer ? (
            <div className="whitespace-pre-wrap leading-7">
              {answer}
            </div>
          ) : (
            <p className="text-gray-500">
              Your AI explanation will appear here.
            </p>
          )}

        </div>
        <QuizGenerator />

      </div>
    </div>
  );
}

export default App;