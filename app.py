"""
This script runs the inside_trip application using a development server.
"""

from os import environ
from inside_trip import app
from inside_trip import db

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000

    app.run(HOST, PORT, debug=True)
