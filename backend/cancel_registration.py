from db_config import connect

def cancel_registration(reg_id):
    
    try:
        reg_id = int(reg_id)

        db = connect()
        cursor = db.cursor()

        cursor.execute("SELECT event_id, seats_booked FROM registrations WHERE id=%s", (reg_id,))
        result = cursor.fetchone()

        if not result[0]:
            db.close()
            return "Registration ID not found!"
        
        event_id, seats_booked = result

        cursor.execute("DELETE FROM registrations WHERE id=%s", (reg_id,))
        cursor.execute("UPDATE events SET seats = seats + %s WHERE id=%s", (seats_booked, event_id))
        
        db.commit()
        db.close()
        return "Registration cancelled successfully!"

    except Exception as e:
        print("Error:", e)
        if 'db' in locals():
            db.close()
        return "Something went wrong!"
