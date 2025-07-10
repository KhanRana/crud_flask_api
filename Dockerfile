# Dockerfile for a Flask application

# This Dockerfile sets up a lightweight Python 3.12 environment for a Flask API.
# 1. Uses the official Python 3.12 slim image as the base.
# 2. Sets the working directory to /usr/local/app.
# 3. Copies requirements.txt and installs dependencies without cache.
# 4. Exposes port 5500 for the Flask app.
# 5. Creates a non-root user 'flask_user' for security and sets it as the container user.
# 6. Copies the application code to the working directory with correct ownership.
# 7. Sets the FLASK_APP environment variable to app.py.
# 8. Specifies the default command to run the Flask app using Python.

FROM python:3.12-slim
WORKDIR /usr/local/app

# Install the dependencies
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5500

# add a user to run the container
RUN useradd flask_user
USER flask_user
COPY --chown=flask_user . /usr/local/app

ENV FLASK_APP=app.py
CMD [ "python3", "app.py"]

