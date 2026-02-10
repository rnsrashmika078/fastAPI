from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///./blog.db"
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://USER:PASSWORD@HOST:5432/DBNAME"
TABLE_NAME = "blogs"
PASSWORD = "srilanka12327"
USERNAME = "postgres"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{USERNAME}:{PASSWORD}@localhost:5432/{TABLE_NAME}"
)

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
Base = declarative_base()
