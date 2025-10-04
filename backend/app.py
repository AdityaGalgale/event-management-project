from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from add_event import add_event
from view_event import view_events
from register_event import register_event
from cancel_registration import cancel_registration

app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../asset"
)
CORS(app)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Render HTML pages
@app.route("/add_event_page")
def add_event_page():
    return render_template("add_event.html")

@app.route("/view_event_page")
def view_event_page():
    return render_template("view_event.html")

@app.route("/register_event_page")
def register_event_page():
    return render_template("register_event.html")

@app.route("/cancel_registration_page")
def cancel_registration_page():
    return render_template("cancel_registration.html")

# Add event
@app.route("/add_event", methods=["POST"])
def add_event_api():
    data = request.get_json()
    name = data.get("name")
    date = data.get("date")
    venue = data.get("venue")
    seats = data.get("seats")
    
    msg = add_event(name, date, venue, seats)
    return jsonify({"message": msg})

# View event
@app.route("/view_events", methods=["GET"])
def view_events_api():
    events = view_events()
    return jsonify(events)

# Register
@app.route("/register_event", methods=["POST"])
def register_event_api():
    data = request.get_json()
    event_id = data.get("event_id")
    user_name = data.get("user_name")
    email = data.get("email")
    seats_booked = data.get("seats_booked")
   
    result = register_event(event_id, user_name, email, seats_booked)
    return jsonify(result)

# Cancel
@app.route("/cancel_registration", methods=["POST"])
def cancel_registration_api():
    data = request.get_json()
    reg_id = data.get("reg_id")
    msg = cancel_registration(reg_id)
    return jsonify({"message": msg})

if __name__ == "__main__":
    app.run(debug=True)
