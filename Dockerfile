FROM python:3.12
WORKDIR /usr/local/app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5500
ENV FLASK_APP=app.py
CMD [ "python", "app.py"]

