import sqlite3

conn = sqlite3.connect("interns.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Interns(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    email TEXT UNIQUE,

    domain TEXT NOT NULL

)
""")

conn.commit()
conn.close()


#attendance db
conn = sqlite3.connect("attandance.db")

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Attendance(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    intern_id INTEGER,

    date TEXT,

    status TEXT

)
""")
conn.commit()
conn.close()

#assignment db
conn = sqlite3.connect("assignment.db")

cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS Assignments(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    intern_id INTEGER,

    mentor_id INTEGER

)
""")
conn.commit()
conn.close()
