FROM python:3.12-slim
WORKDIR /usr/local/app

# Install the dependencies
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5500

# add a user to run the container
RUN useradd app
USER app
COPY --chown=app:app . /usr/local/app

ENV FLASK_APP=app.py
CMD [ "python3", "app.py"]

