from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    # Base
    app_title: str = 'QRKot'
    app_description: str = 'Благотворительный фонд поддержки котиков'
    database_url: str = 'sqlite+aiosqlite:///./cat_charity_fund.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    # Google API
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    # User
    jwt_lifetime = 3600
    password_min_length = 3

    class Config:
        env_file = '.env'


settings = Settings()
