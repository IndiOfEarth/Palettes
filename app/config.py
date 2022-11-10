class Config():
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    ENV = "production"
    MAX_CONTENT_LENGTH = 5000 * 5000  # max file size 5 mb
    UPLOAD_EXTENSIONS = '.jpg', '.png', '.gif'

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
