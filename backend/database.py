import sqlite3
from datetime import datetime

DB_NAME = "axiom_yield.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS calculations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                hos INTEGER,
                volatility INTEGER,
                comm_quality INTEGER,
                recovery_days INTEGER,
                yield_score INTEGER,
                stage INTEGER,
                carrier_name TEXT,
                mc_number TEXT
            )
        ''')
