@echo off

REM Install requirements
pip install -r requirements.txt

REM Apply database migrations
py manage.py migrate

REM Run the Django server
start "" py manage.py runserver

REM Open the Django server in the explorer
start http://localhost:8000
