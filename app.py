"""
This script runs the inside_trip application using a development server.
"""

from os import environ
from inside_trip import app
from inside_trip import db

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT, debug=True)
