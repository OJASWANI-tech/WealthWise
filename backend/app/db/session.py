from sqlalchemy.orm import sessionmaker
from app.db.database import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 👇 YE FUNCTION MISSING THA
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
