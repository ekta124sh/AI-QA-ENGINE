from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.auth.dependencies import get_current_user
from backend.database.dependencies import get_db
from backend.models.user import User
from backend.schemas.user import (
    UserCreate,
    UserResponse,
    Token,
)
from backend.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


# -----------------------------
# Register
# -----------------------------
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    try:
        return AuthService.register_user(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# -----------------------------
# Login (OAuth2)
# -----------------------------
@router.post(
    "/login",
    response_model=Token,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    result = AuthService.login_user(
        db=db,
        username=form_data.username,
        password=form_data.password,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    return {
        "access_token": result["access_token"],
        "token_type": result["token_type"],
    }


# -----------------------------
# Current Logged-in User
# -----------------------------
@router.get(
    "/me",
    response_model=UserResponse,
)
def get_logged_in_user(
    current_user: User = Depends(get_current_user),
):
    return current_user