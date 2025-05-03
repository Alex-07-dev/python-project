
from sqlalchemy import Column, Integer, String
from database.db import Base

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String)
