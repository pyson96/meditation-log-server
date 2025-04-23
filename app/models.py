from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
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

class MeditationDiary(Base):
    __tablename__ = "meditation_diary"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)

    # 10 subtitles and content fields
    subtitle_1 = Column(String)
    content_1 = Column(String)
    subtitle_2 = Column(String)
    content_2 = Column(String)
    subtitle_3 = Column(String)
    content_3 = Column(String)
    subtitle_4 = Column(String)
    content_4 = Column(String)
    subtitle_5 = Column(String)
    content_5 = Column(String)
    subtitle_6 = Column(String)
    content_6 = Column(String)
    subtitle_7 = Column(String)
    content_7 = Column(String)
    subtitle_8 = Column(String)
    content_8 = Column(String)
    subtitle_9 = Column(String)
    content_9 = Column(String)
    subtitle_10 = Column(String)
    content_10 = Column(String)