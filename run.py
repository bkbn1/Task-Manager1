from taskmanager import app

# starting if this file is run directly using python run.py
if __name__ == "__main__":
    app.run()
from config import load_config
app.config.from_object(load_config())

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')  # Load configuration from config.py

db = SQLAlchemy(app)

# Make sure to import models if you have any, for example:
# from your_project_folder.models import YourModel
print(app.config['SQLALCHEMY_DATABASE_URI'])

if __name__ == '__main__':
    app.run(debug=True)
