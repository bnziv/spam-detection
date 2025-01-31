import { useState } from 'react'
import './App.css'

const apiUrl = import.meta.env.VITE_API_URL

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [probability, setProbability] = useState({});
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    if (!text.trim()) return;

    setError('');

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch');
      }

      const data = await response.json();
      setResult(data.result);
      setProbability(data.probability);
    } catch (error) {
      console.error('Error:', error);
      setError('Something went wrong. Please try again.');
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen p-4 flex-col">
      <div className="w-full max-w-md bg-white shadow-md rounded-lg p-6">
        <h1 className={`text-2xl font-bold text-center
        ${result === 'spam' ? 'text-yellow-500' : result === 'ham' ? 'text-green-500' : result === 'phishing' ? 'text-red-500' : 'text-black'}`}>
          Spam Detection
        </h1>

        <textarea
          className="w-full h-32 p-3 mt-4 border border-gray-300 rounded-lg focus:ring focus:ring-blue-300 resize-none text-black"
          placeholder="Enter text here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        {error && <p className="text-red-500 text-sm mt-2">{error}</p>}

        <button
          className={`w-full mt-4 py-2 text-black font-semibold rounded-lg transition border border-gray-300
            ${text.trim() ? 'bg-white-500 border-blue-500 hover:bg-blue-500/75' : 
            'bg-gray-300 cursor-not-allowed'
          }`}
          onClick={handleSubmit}
          disabled={!text.trim()}
        >
          Submit
        </button>
      </div>
      {result && (
          <div className={`mt-4 p-3 text-center font-semibold text-white rounded-lg
          ${result === 'spam' ? 'bg-yellow-500' : result === 'ham' ? 'bg-green-500' : result === 'phishing' ? 'bg-red-500' : 'bg-gray-500'}`}>
            {result.toUpperCase()} {parseInt(probability[result] * 100)}%
            
            {/* Display other probabilities if the main one is less than 90% */}
            {probability[result] < 0.9 &&
            Object.entries(probability)
            .sort((a, b) => b[1] - a[1])
            .map(([label, prob]) => (
              label !== result &&
              <div key={label}>
                {label.toUpperCase()}: {parseInt(prob * 100)}%
              </div>
            ))
            }
          </div>
        )}
      </div>
  )
}

export default App