import sqlite3
from pathlib import Path
from datetime import datetime
import json


def init_db():
    # Path to database file (project root)
    db_path = Path(__file__).resolve().parent.parent / "history.db"

    
    conn = sqlite3.connect(db_path)

    
    cursor = conn.cursor()

    # Create table if it doesn't already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            score REAL,
            missing_skills TEXT,
            job_title TEXT
        )
    """)

    # Save changes and close connection
    conn.commit()
    conn.close()

def save_analysis(score, missing_skills, job_title=None):
    db_path = Path(__file__).resolve().parent.parent / "history.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    missing_skills_json = json.dumps(missing_skills)

    cursor.execute("""
        INSERT INTO analysis_history (timestamp, score, missing_skills, job_title)
        VALUES (?, ?, ?, ?)
    """, (timestamp, score, missing_skills_json, job_title))

    conn.commit()
    conn.close()

def get_history(limit=10):
    db_path = Path(__file__).resolve().parent.parent / "history.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, timestamp, score, missing_skills, job_title
        FROM analysis_history
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows


