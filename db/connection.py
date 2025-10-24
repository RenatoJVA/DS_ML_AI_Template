import os 
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME", "mydatabase")

engine = create_engine(f'sqlite:///{DB_NAME}.db', echo=False)