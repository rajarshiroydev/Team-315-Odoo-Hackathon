from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///synergysphere.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

    BASE_DIR = Path(__file__).resolve().parent.parent  # Points to 'backend' dir
    
    DB_PATH = BASE_DIR / "data" / "app.db"

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    
    # Email Configuration
    SMTP_USERNAME = os.environ.get('SMTP_USERNAME')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
    # Whether to actually send emails (can be set to False for testing)
    MAIL_ENABLED = os.environ.get('MAIL_ENABLED', 'True').lower() == 'true'
   