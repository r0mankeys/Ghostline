import react from '@vitejs/plugin-react'
import { defineConfig, loadEnv } from 'vite'


export default defineConfig(({ mode }) => {
  // Load env file based on `mode` in the current working directory.
  // Set the third parameter to '' to load all env regardless of the
  // `VITE_` prefix.
  const env = loadEnv(mode, "../.", '')
  return {
    plugins: [react()],
    server: {
      port: env.WEB_PORT ? Number(env.WEB_PORT) : 5173,
    },
  }
})
