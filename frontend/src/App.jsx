import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("Loading backend...");

  useEffect(() => {
    fetch("/api/message")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Backend request failed");
        }

        return response.json();
      })
      .then((data) => {
        setMessage(data.message);
      })
      .catch(() => {
        setMessage("Unable to connect to backend");
      });
  }, []);

  return (
    <main>
      <h1>CI/CD Demo Application</h1>

      <h2>React Frontend</h2>

      <p>Backend Response:</p>

      <strong>{message}</strong>
    </main>
  );
}

export default App;
