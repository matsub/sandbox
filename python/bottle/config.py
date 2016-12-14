class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    CDN_DOMAIN = 'cdn.peerboard.com'
    CDN_HTTPS = True

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    CDN_DOMAIN = 'localhost:8000'
    CDN_HTTPS = False

class TestingConfig(Config):
    TESTING = True
