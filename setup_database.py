import sqlite3

# -------------------------------
# Wrap database creation in a function
# -------------------------------
def create_database():
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        gpa REAL
    )
    """)

    # -------------------------------
    
    # -------------------------------
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany("""
        INSERT INTO students (name, department, gpa)
        VALUES (?, ?, ?)
        """, [
            ("Ali", "CS", 3.5),
            ("Ahmed", "IT", 3.8),
            ("Sara", "CS", 3.9),
            ("Zara", "SE", 3.6)
        ])

    conn.commit()
    conn.close()

# -------------------------------

# -------------------------------
if __name__ == "__main__":
    create_database()
    print("Database created successfully!")

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
