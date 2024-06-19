import sqlite3

conn = sqlite3.connect('test.db')
print("Successfully connected")

conn.execute("""
CREATE TABLE TEACHERS(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL)
""")

print("Successfully created table Teachers")
conn.close()