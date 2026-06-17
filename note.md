-- create enviroment using 
py -m venv .venv

-- activate enviroment using 
source ./.venv/bin/activate

-- then install Django
py -m pip install Django

-- update pip py to latest
py -m pip install -U pip

--to create project
django-admin startproject ..name of your project

-- to run server
py (manage.py dir) runserver