# Copilot Instructions for This Repository

## Build, Test, and Lint Commands

- **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
- **Start the server:**
  ```bash
  ./start-server.sh
  # or
  FLASK_APP=server.py FLASK_RUN_PORT=3000 flask run
  ```
- **Run a single test:**
  *No test suite detected. Add instructions here if/when tests are added.*
- **Linting:**
  *No linting configuration detected. Add instructions here if/when linting is added.*

## High-Level Architecture

- This is a simple Flask backend server (see `server.py`).
- CORS is enabled for requests from `http://localhost:1234` (likely a frontend dev server).
- The main endpoint is:
  - `POST /hello`: Expects JSON `{ "name": "your name" }` and responds with `{ "message": "Hello <name>" }`.
- All backend logic currently resides in `server.py`.

## Key Conventions

- Only allows CORS requests from `http://localhost:1234`.
- Expects POST data as JSON with a `name` field for `/hello`.
- Returns errors as JSON with an `error` key and HTTP 400 for missing fields.

---

*No other AI assistant config files or conventions detected. Update this file if you add tests, linting, or additional conventions.*
