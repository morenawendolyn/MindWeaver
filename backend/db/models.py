




"""
Simple database models using SQLAlchemy for tracking tasks and history.
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class RefactorTask(Base):
    __tablename__ = "refactor_tasks"

    id = Column(Integer, primary_key=True)
    file_path = Column(String, nullable=False)
    status = Column(String, default="queued")
    score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

def get_engine(db_url="sqlite:///mindweaver.db"):
    return create_engine(db_url, echo=False, future=True)

def get_session(engine=None):
    if engine is None:
        engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
