import { useState } from "react";
import axios from "axios";

function App() {
  const [topic, setTopic] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askAI = async () => {
    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/ask-ai",
        {
          topic: topic,
          difficulty: "beginner",
          explanation_type: "simple",
          language: "English"
        }
      );

      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
      alert("Error calling backend");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>AI Study Assistant</h1>

      <input
        type="text"
        placeholder="Enter a topic"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        style={{
          width: "300px",
          padding: "10px"
        }}
      />

      <br />
      <br />

      <button onClick={askAI}>
        Ask AI
      </button>

      <br />
      <br />

      {loading && <p>Loading...</p>}

      {answer && (
        <div>
          <h3>Response</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;