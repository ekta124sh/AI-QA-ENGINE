from sqlalchemy.orm import Session

from backend.auth.jwt import create_access_token
from backend.auth.security import hash_password, verify_password

from backend.database.auth_crud import (
    create_user,
    get_user_by_email,
)

from backend.schemas.user import UserCreate


class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        user: UserCreate,
    ):
        """
        Register a new user.
        """

        existing_user = get_user_by_email(
            db,
            user.email,
        )

        if existing_user:
            raise ValueError("Email already registered")

        return create_user(
            db=db,
            name=user.name,
            email=user.email,
            hashed_password=hash_password(user.password),
        )

    @staticmethod
    def login_user(
        db: Session,
        username: str,
        password: str,
    ):
        """
        Authenticate user and generate JWT token.

        Note:
        OAuth2PasswordRequestForm uses the field 'username'.
        In this project, the username is the user's email.
        """

        db_user = get_user_by_email(
            db,
            username,
        )

        if not db_user:
            return None

        if not verify_password(
            password,
            db_user.hashed_password,
        ):
            return None

        access_token = create_access_token(
            {
                "sub": db_user.email,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": db_user,
        }