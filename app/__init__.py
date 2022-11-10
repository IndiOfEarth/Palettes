from flask import Flask

app = Flask(__name__)

# Setting FLASK_ENV and Config
# USE: set FLASK_ENV=development or production BEFORE "flask run"
if app.config["ENV"] == "production":
    app.config.from_object("app.config.ProductionConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("app.config.DevelopmentConfig")


from app import routes