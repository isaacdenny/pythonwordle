# pythonwordle
wordle spin-off in python

# Project Summary
Users can compete in a daily wordle-like online game and track their leaderboard status. Each user will have analytics based on their performance that they and other players can see. The game is called "Pass" where players must log in during the day to pass the bomb to another player. Before passing the bomb, the player must put together a word with the letters written on the bomb. If the player fails to log in during that day (if they have a bomb), or fails to put together a word with the letters provided, the bomb explodes.

# Technologies
- Python 3.11+
- Fast API
- Postgres
- SQLAlchemy
- Alembic
- Uvicorn

# Local Development
1. Clone this repo and `cd` into the repo directory
2. Check your python version: `python -V`. if less than 3.11, use pyenv to install and switch to 3.11+
3. Make sure [Poetry](https://python-poetry.org/docs/1.2/basic-usage/) is installed.
4. Install dependencies: `poetry install`
5. Run the server: `poetry run uvicorn main:app --reload`
6. Access swagger docs at: http://127.0.0.1:8000/docs

# Schema

## User

- username
- email
- created_at
- updated_at

## Challenge (Bomb)

- title
- answers
- provided_letters
- created_by
- created_at
- updated_at
- published_status

# Design API

# Planning TODOs
- [ ] List all requirements
- [ ] Create Schema
- [ ] Design API
- [ ] Create Mockups
- [ ] Choose Technologies
