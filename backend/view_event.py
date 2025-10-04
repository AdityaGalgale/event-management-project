from db_config import connect

def view_events():
    db = connect()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT id, name, date, venue, seats FROM events")
    events = cursor.fetchall()

    db.close()
    return events
