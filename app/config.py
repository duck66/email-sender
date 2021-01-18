# Database related config
DB_NAME = "emailsender"
DB_USER = "emailsender"
DB_PASS = "password"
DB_HOST = "localhost"
DB_PORT = "5438"

SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Celery Configuration
RESULT_BACKEND = "redis://localhost:6379"
CELERY_BROKER_URL = "redis://localhost:6379"
