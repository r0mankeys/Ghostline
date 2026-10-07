# Run the backend python API
backrun:
  cd backend && uv run --env-file ../.env main.py

# Run the web server
frontrun:
  cd frontend && bun run dev

