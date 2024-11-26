import time
import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("base de datos de autoconocimiento creada")
    conn.close()
    
def createTable() :
    conn = sql.connect("autoconocimiento.db")    
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE reminders (
    reminder_id INTEGER PRIMARY KEY AUTOINCREMENT,
    planning_id INTEGER,
    reminder_type TEXT, -- 'start', 'milestone', 'budget_alert', 'end'
    reminder_date DATE,
    message TEXT,
    is_sent BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (planning_id) REFERENCES experience_planning(planning_id)
    );
    """)
    print("tabla creada")
    conn.commit()
    conn.close()
   
if __name__ == "__main__": 
    createDB()
    createTable()
     
