import sqlite3
from datetime import datetime
from pathlib import Path

# ==========================================================
# DATABASE CONFIGURATION
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "applications.db"

DB_PATH.parent.mkdir(exist_ok=True)


# ==========================================================
# CREATE DATABASE
# ==========================================================

def create_database():
    with sqlite3.connect(DB_PATH) as conn:

        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS applications (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                company TEXT,
                role TEXT,
                email TEXT,
                location TEXT,

                status TEXT,

                applied_at TEXT
            )
        """)

        conn.commit()


# ==========================================================
# CHECK DUPLICATE
# ==========================================================

def application_exists(email, role):
    with sqlite3.connect(DB_PATH) as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM applications
            WHERE email = ?
            AND role = ?
            LIMIT 1
            """,
            (email, role),
        )

        return cursor.fetchone() is not None


# ==========================================================
# SAVE APPLICATION
# ==========================================================

def save_application(job, status):

    email = job.get("email")
    role = job.get("role")

    # Prevent duplicate applications
    if application_exists(email, role):
        print("\n⚠️ Application already exists in the database.")
        return

    with sqlite3.connect(DB_PATH) as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO applications
            (
                company,
                role,
                email,
                location,
                status,
                applied_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                job.get("company"),
                role,
                email,
                job.get("location"),
                status,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ),
        )

        conn.commit()


# ==========================================================
# GET ALL APPLICATIONS
# ==========================================================

def get_all_applications():

    with sqlite3.connect(DB_PATH) as conn:

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                company,
                role,
                email,
                location,
                status,
                applied_at
            FROM applications
            ORDER BY applied_at DESC
        """)

        return cursor.fetchall()