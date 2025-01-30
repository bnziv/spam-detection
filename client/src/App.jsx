import { useState } from 'react'
import './App.css'

function App() {
  const [text, setText] = useState('')
  const [result, setResult] = useState('')
  
  const submit = (text) => {
    if (!text) {
      return
    }
    fetch('http://127.0.0.1:5000/api/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text })
    })
    .then(response => response.json())
    .then(response => setResult(response.result))
  }

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
        <button onClick={() => submit(text)}>
          Submit
        </button>
      </div>
    </>
  )
}

export default App
