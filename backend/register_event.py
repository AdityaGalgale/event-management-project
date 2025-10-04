from db_config import connect

def register_event(event_id, user_name, email, seats_booked):
    db = connect()
    cursor = db.cursor()

    # checking available seats
    cursor.execute("SELECT seats FROM events WHERE id=%s", (event_id,))
    result = cursor.fetchone()

    if not result:
        db.close()
        return {"success": False, "error": "Event not found."}

    if result and result[0] >= seats_booked:
        cursor.execute(
            "INSERT INTO registrations (event_id, user_name, email, seats_booked) VALUES (%s, %s, %s, %s)",
            (event_id, user_name, email, seats_booked)
        )
        reg_id = cursor.lastrowid

        cursor.execute("UPDATE events SET seats = seats - %s WHERE id=%s", (seats_booked, event_id))

        db.commit()
        db.close()
        return {"success": True, "reg_id": reg_id, "message": "Registration successful."}
    else:
        db.close()
        return {"success": False, "error": "Not enough seats available."}
