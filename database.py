from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os 
#carregar as variaveis de ambiante
load_dotenv()

DATABASE_URL =os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

Base =declarative_base()

sesion = sessionmaker(bind=engine)


def get_db():
    db =sesion()
    try:
        yield db
    finally:
        db.close()
        