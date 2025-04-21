from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from google.oauth2 import id_token as google_id_token
from google.auth.transport import requests
import os

from app.database import get_db
from app.models import User
from app.auth import create_access_token
from app.schemas import GoogleIdToken

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

router = APIRouter()

@router.post("/auth/google/id-token-login")
def login_with_google_id_token(payload: GoogleIdToken, db: Session = Depends(get_db)):
    try:
        # 🔐 Verify token and check audience (aud)
        id_info = google_id_token.verify_oauth2_token(
            payload.id_token,
            requests.Request(),
            GOOGLE_CLIENT_ID  # ✅ Required to match aud claim
        )
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid ID token")

    # 🔍 Additional checks
    if not id_info.get("email_verified"):
        raise HTTPException(status_code=403, detail="Email not verified")

    email = id_info["email"]
    name = id_info.get("name")
    google_user_id = id_info["sub"]

    # 🔁 Check or create user in DB
    user = db.query(User).filter(User.oauth_id == google_user_id).first()
    if not user:
        user = User(
            email=email,
            name=name,
            oauth_id=google_user_id,
            oauth_provider="google"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # 🪪 Create your own JWT
    jwt_token = create_access_token(data={"sub": user.email})
    return {"access_token": jwt_token, "token_type": "bearer"}
