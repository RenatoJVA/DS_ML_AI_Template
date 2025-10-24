from db.connection import get_db_connection, engine
from db.models import Base

if __name__ == "__main__":
    # Initialize the database by creating all tables defined in the models
    engine = get_db_connection()
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")