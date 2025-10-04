from db_config import connect

def add_event(name, date, venue, seats):

    db = connect()
    cursor = db.cursor()

    sql = "INSERT INTO events (name, date, venue, seats) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, date, venue, seats))

    db.commit()
    db.close()

    return "Event added successfully!"
