from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:Kv%409063321@localhost:5432/customer_db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()