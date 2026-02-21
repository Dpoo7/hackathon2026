from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import os
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()

# DATABASE PATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CONNECT DB
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    mobile TEXT,
    dob TEXT,
    profession TEXT,
    email TEXT,
    password TEXT
)
""")
conn.commit()

# MODEL
class User(BaseModel):
    name: str
    mobile: str
    dob: str
    profession: str
    email: str
    password: str

# REGISTER API
@app.post("/register")
def register(user: User):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users (name, mobile, dob, profession, email, password)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (user.name, user.mobile, user.dob, user.profession, user.email, user.password))

    conn.commit()
    conn.close()

    return {"message": "User registered successfully"}