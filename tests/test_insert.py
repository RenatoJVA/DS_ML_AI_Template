import pytest
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import User, Base

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

@pytest.fixture
def db_session():
    """Creates a new database session for a test."""
    session = Session()
    yield session
    session.rollback()
    session.close()

def test_insert_user(db_session):
    """Tests inserting a user into the database."""
    new_user = User(name="Test User", email="example@email.com", years=30)
    db_session.add(new_user)
    db_session.commit()

    retrieved_user = db_session.query(User).filter_by(email="example@email.com").first()
    assert retrieved_user is not None
    assert retrieved_user.name == "Test User"