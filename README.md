# Todo List App

The Todo List App is an application for creating and sharing todolists.

This repo contains:

* Resources for creating users, todo lists, todos, and todo list permissions.
* User tests for the above resources.


## Environment Setup

Clone the repository:

`git clone https://github.com/cfierro/todo.git`

Grab your fork:

'git remote add [yourname] https://github.com/[yourname]/todo.git'

Install dependencies using the bootstrap script:

`./scripts/bootstrap.sh`


## Directory Structure

* app/authentication - resources for user authentication
  * log in
  * log out
  * get logged in user info
* app/lib - shared libraries across multiple resources
  * /authenticaion - decorator for requiring a user to be logged in
  * /models - includes a base table mixin for all data tables
  * /response_uit - methods for building status responses
  * /status - classes for returning raised exceptions
* app/permissions - model and resources for list permissions
* app/todo_lists - model and resources for todo lists
* app/todos - model and resources for todos
* app/users - model and resources for users
* app/__init__.py - initialize python packages. Includes:
  * Import Flask libraries
  * Error handler
  * database creation
  * Model imports
  * Resources urls for APIs
* env - virtual environment
* scripts - bootstrap script fo installing dependencies
* unittest/resources - unittests for user, todo, todo_list, and auth resources
* .gitignore - files to ignore upon git commit
* config.py -
* README.md - this file!
* requirements.txt - required libraries
* run.py - runs the application.
* shell.py -


## Development

Run the following from the top level directory:

Activate your virutual environment.

`source env/bin/activate`

To run the app:

`python run.py`

To run unit tests:

`py.test unittest`

