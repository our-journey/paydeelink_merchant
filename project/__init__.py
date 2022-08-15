'''
Cheat Sheet:

> create user usera with password 'passworda';
> \du
> alter user usera with superuser;
> alter user usera with createdb;
> alter user usera with createrole;
> \c postgres usera
> \l
> create database databasea;
> \c databasea usera;
>

Fix:
# python -m pip install --upgrade pip
# python -m pip install --no-use-pep517 flask-bcrypt
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisfirstflaskapp2'

from project import routes