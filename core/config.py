"""
Archivo de configuración general
"""
import os

from dotenv import load_dotenv


class Settings:
    PROJECT_NAME:str = "Atenea API🔥"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "Ejemplo práctico de CRUD con API"

    load_dotenv()   # cargamos variables de entorno

    # DataBase
    DB_DRIVER: str = os.getenv('DB_DRIVER')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: int = os.getenv('DB_PORT')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_USER: str = os.getenv('DB_USER')
    DB_PASS: str = os.getenv('DB_PASS')
    # Auth
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    TOKEN_EXPIRE: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    ALGORITHM = "HS256"

    DATABASE_URL = f"Driver={DB_DRIVER};Server={DB_HOST};Database={DB_NAME};Trusted_Connection=yes;"


settings = Settings()
