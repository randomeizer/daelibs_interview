# The Project

This repository contains both the backend and frontend for the daelibs interview project.

This project uses an sqlite3 database which is included in the repo (so you don't have to run migrate).

## Backend Overview

The code is in two main parts:

1. The `daelibs_interview` project, which configures and runs the Django server.
2. The `main` app, which contains the traffic API.

Getting it running:

* Ensure Python 3.10 or higher
* Create Python virtualenv and install requirements from `requirements.txt`
* Start your local server

### 1. Ensure Python 3.10 or higher is installed

Latest version can be downloaded from:

<https://www.python.org/downloads/>

Ensure it is added to your path.

### 2. Create virtualenv and install dependencies

To create a virtualenv,

```python
python -m venv daelibs-interview
```

This will create a folder call 'daelibs-interview', then you will need to activate the environment.

On Windows, run:

```shell
daelibs-interview\Scripts\activate.bat
```

On Unix or MacOS, run:

```shell
source daelibs-interview/bin/activate
```

The virtual environment will be activated and you’ll see "daelibs-interview" next to the command prompt to designate that

Once done, you should cd to the dummy project root directory and run:

```shell
pip install -r requirements.txt
```

### 4. Testing

The `main` app contains a test suite that can be run using the Django test runner.

There is a script that sets up the test environment and runs the tests:

```shell
./run_tests.sh
```

You may need to make the script executable by running:

```shell
chmod +x run_tests.sh
```

If you prefer to run the tests via the Django test runner, you can do so by running:

```shell
export DJANGO_SETTINGS_MODULE=daelibs_interview.settings.test; python manage.py test
```

### 3. Start your local server

You should now be able to run the local server:

```shell
python manage.py runserver
```

### 4. Query the API

Once the server is running, you can query the API by visiting:

<http://localhost:8000/traffic/dayOfWeekAverageCount?start_date=2023-07-07&end_date=2023-07-14>

If you enter an invalid date, you will receive a 400 response with a message indicating the error. For example, if your end date is prior to the start date:

<http://localhost:8000/traffic/dayOfWeekAverageCount?start_date=2023-07-07&end_date=2023-07-06>

## Frontend Overview

The frontend is built with Vue 3. It is a single page that displays the ScoreList component. This component is a table that displays the scores of the users, based on the design from the Figma project. The scores are fetched from the backend, which is just hard-coded in this example.

### 1. Project setup

Install `Node` and `npm` if you haven't already. You can download them from:

<https://nodejs.org/en/download/>

Then, move into the frontend directory and install the dependencies:

```shell
cd daelibs-frontend
npm install
```

### 2. Compile and hot-reload for development

```shell
npm run serve
```

### 3. Access the frontend

Once the server is running, you can access the frontend at `http://localhost:8080/`.
