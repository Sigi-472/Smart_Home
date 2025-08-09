from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

Base = declarative_base()

class Notiz(Base):
  __tablename__ = "notizen"

  id = Column(Integer, primary_key=True)
  Notiz = Column(String, nullable=False)
  Priority = Column(Integer, nullable=False)
  Datum = Column(Date, nullable=False)

def get_engine(db_path="Database.db"):
  db_url = f"sqlite:///{db_path}"
  engine = create_engine(db_url, echo=False)
  return engine

def create_db(engine):
    Base.metadata.create_all(engine)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()