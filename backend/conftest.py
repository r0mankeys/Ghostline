import os

# pytest doesn't load .env, and main.py refuses to start without WEB_URL.
# conftest.py runs before the test files import main, so set it here.
os.environ.setdefault("WEB_URL", "http://localhost:3001")
