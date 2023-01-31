"""
John Doe's Flask API.
"""

from flask import Flask, Request, send_from_directory, render_template
from werkzeug.exceptions import NotFound, Forbidden
import os
import configparser

def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

config = parse_config(['credentials.ini', 'default.ini'])
port = config['SERVER']['PORT']

app = Flask(__name__)

@app.route("/")
def home():
    return "CS 322 Flask test by Calvin Stewart"

@app.errorhandler(404)
def page_not_found(a):
    return send_from_directory("./pages/", "404.html"), 404

@app.errorhandler(403)
def filename_forbidden(a):
    return send_from_directory("./pages/", "403.html"), 403

@app.route("/<path:filename>")
def printhtml(filename):
    if '..' in filename or '~' in filename:
        raise Forbidden()

    if not(os.path.exists(f'./pages/{filename}')):
        raise NotFound()

    return send_from_directory("./pages/", filename)

if __name__ == "__main__":
    app.run(port=port, debug=True, host='0.0.0.0')
