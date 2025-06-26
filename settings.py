from os import environ
MONGO_URI=environ.get("MONGO_URI")
SECRET_KEY=environ.get("SECRET_KEY")
DATABASE_NAME=environ.get("DATABASE_NAME")
FLASK_DEBUG=environ.get("FLASK_DEBUG", "False").lower() in ("true", "1", "t")
FLASK_ENV=environ.get("FLASK_ENV", "development")
FLASK_APP=environ.get("FLASK_APP", "app.py")
FLASK_RUN_PORT=int(environ.get("FLASK_RUN_PORT", 5000))
DEBUG=FLASK_DEBUG
if FLASK_ENV == "development":
    DEBUG = True
else:
    DEBUG = False
    
