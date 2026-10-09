// Vite fills import.meta.env from the root .env (see envDir in vite.config.ts).
// Only VITE_-prefixed variables are visible here.
const API_URL = import.meta.env.VITE_API_URL
const file_types = [
  "image/jpeg",
  "image/png",
]
const ACCEPTABLE_FILE_TYPES = file_types.join(", ")

function App() {
  async function handleSubmit(e) {
    e.preventDefault()
    const form = e.target;
    const formData = new FormData(form);
    try {
      const response = await fetch(`${API_URL}/submissions`, {
        method: "POST",
        body: formData
      });
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
        const result = await response.json();
        console.log(result);
      } catch (error) {
        console.error(error.message);
      }
    }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input type="file" id="img_upload" name="file" accept={ACCEPTABLE_FILE_TYPES}></input>
        <button type="submit">Submit</button>
      </form>
    </>
  )
}

export default App
