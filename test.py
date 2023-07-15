from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/portfolio'
db = SQLAlchemy(app)

# Define your models and perform database operations using 'db'

if __name__ == '__main__':
    app.run()
