from pydantic import BaseModel
from typing import Optional
from datetime import date

class GoogleIdToken(BaseModel):
    id_token: str


class MeditationDiaryCreate(BaseModel):
    date: date
    subtitle_1: Optional[str] = None
    content_1: Optional[str] = None
    subtitle_2: Optional[str] = None
    content_2: Optional[str] = None
    subtitle_3: Optional[str] = None
    content_3: Optional[str] = None
    subtitle_4: Optional[str] = None
    content_4: Optional[str] = None
    subtitle_5: Optional[str] = None
    content_5: Optional[str] = None
    subtitle_6: Optional[str] = None
    content_6: Optional[str] = None
    subtitle_7: Optional[str] = None
    content_7: Optional[str] = None
    subtitle_8: Optional[str] = None
    content_8: Optional[str] = None
    subtitle_9: Optional[str] = None
    content_9: Optional[str] = None
    subtitle_10: Optional[str] = None
    content_10: Optional[str] = None