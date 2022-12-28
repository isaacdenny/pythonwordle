# pythonwordle
wordle spin-off in python

# Project Summary
Users can compete in a daily wordle-like online game and track their leaderboard status. Users can log in and then play the game. After playing, each user will have analytics based on their performance that they and other players can see. 

# Technologies
- FastAPI
- PostgreSQL
- SQLalchemy
- Alembic
- 

# Local Development
1. Clone this repo and `cd` into the repo directory
2. Check your python version: `python -V`. if less than 3.11, use pyenv to install and switch to 3.11+
3. Make sure [Poetry](https://python-poetry.org/docs/1.2/basic-usage/) is installed.
4. Install dependencies: `poetry install`
5. Run the server: `poetry run uvicorn main:app --reload`
6. Access swagger docs at: http://127.0.0.1:8000/docs

# Schema

# Design API

# Planning TODOs
- [] List all requirements
- [] Create Schema
- [] Design API
- [] Create Mockups
- [] Choose Technologies
