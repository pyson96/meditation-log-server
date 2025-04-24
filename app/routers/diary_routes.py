from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import MeditationDiary, User
from app.schemas import MeditationDiaryCreate
from datetime import date
from app.auth import get_current_user  # JWT-based auth
router = APIRouter()

@router.post("/diaries", response_model=dict)
def create_diary(
    entry: MeditationDiaryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ← JWT-based auth
):
    diary = MeditationDiary(user_id=current_user.id, **entry.dict())
    db.add(diary)
    db.commit()
    db.refresh(diary)
    return {"message": "Diary saved", "id": diary.id}

@router.get("/diaries/{entry_date}")
def get_diary_by_date(
    entry_date: date,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    diary = (
        db.query(MeditationDiary)
        .filter(
            MeditationDiary.user_id == current_user.id,
            MeditationDiary.date == entry_date
        )
        .first()
    )

    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found for that date")

    return {
        "id": diary.id,
        "date": diary.date,
        "subtitles": [getattr(diary, f"subtitle_{i}") for i in range(1, 11)],
        "contents": [getattr(diary, f"content_{i}") for i in range(1, 11)],
    }