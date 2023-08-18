"""
Archivo de configuración general
"""

class Settings:
    PROJECT_NAME:str = "Atenea API🔥"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "Ejemplo práctico de CRUD con API"

    DB_DRIVER = "{SQL Server}"
    DB_HOST = "OFICINAROBERTOP\SQLEXPRESS"
    DB_PORT = "1433"
    DB_NAME = "dbPruebas"
    DB_USER = "sa"
    DB_PASS = "atenea"

    # DATABASE_URL = "Driver={SQL Server};Server=OFICINAROBERTOP\SQLEXPRESS;Database=dbPruebas;Trusted_Connection=yes;"
    DATABASE_URL = f"Driver={DB_DRIVER};Server=DB_HOST;Database=DB_NAME;Trusted_Connection=yes;"


settings = Settings()
