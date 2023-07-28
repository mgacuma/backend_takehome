#!/bin/sh

export FLASK_APP=./app.py

export FLASK_DEBUG=1

pipenv run flask --debug run -p 5000 -h 0.0.0.0