# Carer API - Technical Testing Task

## Scenario
There is an API which returns based on a date whether it is a working day for the carer or not.   
For Example: The Carer works Monday to Friday. So a date which falls on a Saturday would return that it is not a working day.

## Task 1
We are going to push this API to production for the first time. In order to ensure we have delivered quality, reliable and stable software what approach should we take?
1. Add a TEST-APPROACH.md explaining your test approach for this task, including different levels & types of test

## Task 2
1. Fix the failing test
1. Add a test for a negative scenario
1. Refactor anything you would improve

## Tips
1. Make sure to comment and add details of your thought process and any assumptions you have made
1. Don't spend too long on it (2 hours max)

## Setup

Resource used to create project [Flask Docs](https://flask.palletsprojects.com/tutorial/)   
python version (`3.10.0`)   
pip version (`21.2.3`)

### Run API
1. `python3 -m venv venv` or Windows `py -3 -m venv venv`
1. `. venv/bin/activate` or Windows `venv\Scripts\activate`
1. `pip install -e .`
1. `export FLASK_APP=flaskr` or Windows `set FLASK_APP=flaskr`
1. `export FLASK_ENV=development` or Windows `set FLASK_ENV=development`
1. `flask run`

### Run tests

1. `python3 -m venv venv` or Windows `py -3 -m venv venv`
1. `. venv/bin/activate` or Windows `venv\Scripts\activate`
1. `pip install '.[test]'`
1. `pytest`

## On Completion
- Fork and push your changes, then notify the hiring manager   
or
- Clone then zip it up and email to hiring manager    
(please do not create a pull request or push to main)
