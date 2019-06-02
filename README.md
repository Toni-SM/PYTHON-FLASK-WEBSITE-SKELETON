# PYTHON FLASK WEBSITE SKELETON
## *Web site skeleton with autentication and accounts creation*

 * Running over Python [Flask](http://github.com) microframework
 * Database abstraction layer with [Flask-SQLAlchemy](http://github.com)
 * Automatic creation of the database and its tables (if not exist)
 * User session management with [Flask-Login](http://github.com)
 * Account management page for create and remove users
 * Visual design and implementation of login/logout 

## Instructions

### Project dependencies
Install the necessary dependencies from `Python Command Line` 

```bash
$ python -m pip install Flask Flask-SQLAlchemy Flask-Login
```

or from `pip3` tool
```bash
$ pip3 install Flask Flask-SQLAlchemy Flask-Login
```

### Start the development server
Start the development server and browse to http://localhost:80

```bash
$ python run.py
```

Optionally you can execute the file `run.bat` in Windows or `run.sh` in Linux respectively

**Note:** You can change the current port of the development server or another parameters in the file `config.py` (root folder)
