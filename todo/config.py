import os
dbpath = os.path.join(os.path.abspath(os.curdir), "todo.db")
SECRET_KEY = "secert"
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(dbpath)
SQLALCHEMY_TRACK_MODIFICATIONS = True