from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    oauth_provider = Column(String)  # e.g. 'google', 'github'
    oauth_id = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
