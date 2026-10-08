// Vite fills import.meta.env from the root .env (see envDir in vite.config.ts).
// Only VITE_-prefixed variables are visible here.
const API_URL = import.meta.env.VITE_API_URL

function App() {
  console.log(`This is the API URL: ${API_URL}`)

  return (
    <>
      <form></form>
    </>
  )
}

export default App
