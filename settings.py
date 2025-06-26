from os import environ
MONGO_URI=environ.get("MONGO_URI")
SECRET_KEY=environ.get("SECRET_KEY")
DATABASE_NAME=environ.get("DATABASE_NAME")
PORT=int(environ.get("PORT", 5500))
# Set Flask environment variables
FLASK_ENV=environ.get("FLASK_ENV", "development")
FLASK_APP=environ.get("FLASK_APP", "app.py")
if FLASK_ENV == "development":
    DEBUG = True
else:
    DEBUG = False

