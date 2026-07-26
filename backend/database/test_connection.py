from sqlalchemy import text

from backend.database.connection import engine

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("✅ Database Connected Successfully!")

except Exception as e:
    print(e)