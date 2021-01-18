import os

# Database related config
DB_NAME = os.getenv("DB_NAME", "emailsender")
DB_USER = os.getenv("DB_USER", "emailsender")
DB_PASS = os.getenv("DB_PASS", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5438")

SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Celery related config
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
RESULT_BACKEND = "redis://localhost:{REDIS_PORT}"
CELERY_BROKER_URL = "redis://localhost:{REDIS_PORT}"

UTC_OFFSET = 7

# Mail related config
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_USE_TLS = False
MAIL_USE_SSL = True
