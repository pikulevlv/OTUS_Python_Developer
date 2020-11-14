import os
PG_HOST = os.environ["PG_HOST"]
if PG_HOST is None:
    PG_HOST = "0.0.0.0"
SQLALCHEMY_DATABASE_URI = f"postgres+psycopg2://user:password@{PG_HOST}:5432/mosdb"
