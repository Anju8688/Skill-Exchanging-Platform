import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = "postgresql://neondb_owner:npg_QdAhrPF78Zyq@ep-divine-mode-a8lx3oy2-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 