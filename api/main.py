from flask import Flask
from flask_cors import CORS

from match import match


app = Flask(__name__)
CORS(app)

# define Flask API here

if __name__ == '__main__':
    app.run()
