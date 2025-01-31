import { useState } from 'react'
import './App.css'

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  
  const handleSubmit = async () => {
    if (!text.trim()) return;

    setError('');

    try {
      const response = await fetch('http://127.0.0.1:5000/api/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch');
      }

      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.error('Error:', error);
      setError('Something went wrong. Please try again.');
    }
  };

  return (
    <>
      <div>
      </div>
      <h1 className={result}>Spam Detection</h1>
      <div className="card">
        <textarea
          onChange={(e) => setText(e.target.value)}
          value={text}
          className={result}
        />
        <button onClick={handleSubmit}>
          Submit
        </button>
        {result && <p>{result}</p>}
      </div>
    </>
  )
}

export default App
