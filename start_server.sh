#!/bin/bash

# Activate virtual environment and start the server

echo "Starting SmileItsSunnah Voice Agent Server..."

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# Start the server
python app.py
