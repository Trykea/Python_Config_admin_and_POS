from sqlalchemy import create_engine, text
from flask import Flask, render_template, request
from urllib.parse import quote_plus
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
user = 'root'
password = '@12345sql'
host = '127.0.0.1'
port = '3306'
database = 'st89_pos'

# URL-encode the password
encoded_password = quote_plus(password)

# Create the connection string
connection_string = f"mysql+mysqlconnector://{user}:{encoded_password}@{host}:{port}/{database}"

# Create the engine
engine = create_engine(connection_string)

import routes

if __name__ == '__main__':
    app.run()
