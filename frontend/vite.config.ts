import react from '@vitejs/plugin-react'
import { defineConfig, loadEnv } from 'vite'

// The shared .env lives in the repo root, one level up from frontend/.
const envDir = '..'

export default defineConfig(({ mode }) => {
  // Config-time only (runs in Node when Vite starts): load every variable,
  // prefixed or not, so the config can read WEB_PORT. None of this reaches
  // the browser.
  const env = loadEnv(mode, envDir, '')

  return {
    plugins: [react()],
    // Where Vite reads .env for import.meta.env in browser code.
    // Only VITE_-prefixed variables are exposed there.
    envDir,
    server: {
      port: env.WEB_PORT ? Number(env.WEB_PORT) : 5173,
    },
  }
})
