class Config():
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    ENV = "production"

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
