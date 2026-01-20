from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, index=True)
    signup_date = Column(Date)
