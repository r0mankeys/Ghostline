set dotenv-load

host := 'localhost'
port := env("API_PORT", "8000")
default_address := host+":"+port

# Default recipe, health check
default: health

# Run the backend python API
backrun:
  cd backend && uv run main.py

# Run the web server
frontrun:
  cd frontend && bun run dev

# Check the backend has intiated correctly
health address=default_address:
  curl -fsS '{{address}}/health'

# Run all tests
test:
  cd backend && uv run pytest
