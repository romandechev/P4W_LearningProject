import sqlite3 as sql


# Login method
def check_login(email, password):
    con = sql.connect(".database/database.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM USERS WHERE email == ? AND password == ?",
        (email, password),
    )
    result = cur.fetchone()
    con.close()
    if result is None:
        return False
    else:
        return True
