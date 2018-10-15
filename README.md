# Awwwards

#### By **Kevin Jared**

## Description
The application allow a user to post a project he/she has created and get it reviewed by his/her peers.

**A user can**
* View posted projects and their details.
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page.

## Live Link
https://awwardsone.herokuapp.com/

## Set Up and Installations

### Prerequisites
1. Python3.6
2. Postgres
3. Python virtualenvironment
### Clone the Repo

Run the following command on the terminal:
`https://github.com/KevinJared/Awwards.git`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source virtual/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE gallery;
```

```
### Run initial Migration
```bash
python3.6 manage.py makemigrations gallery
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

## Known bugs
No known bugs so far

## Technologies used
    - HTML
    - JavaScript
    - css
    - Python 3.6
    - Bootstrap 4
    - Heroku
    - Postgresql


### License
Copyright (c) **Kevin Jared**