------- MySQL --------

CREATE DATABASE IF NOT EXISTS event_system;

USE event_system;

CREATE TABLE IF NOT EXISTS events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    date DATE,
    venue VARCHAR(255),
    seats INT
);

CREATE TABLE IF NOT EXISTS registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    user_name VARCHAR(255),
    email VARCHAR(255),
    seats_booked INT,
    FOREIGN KEY (event_id) REFERENCES events(id)
);

------- install --------

pip install flask flask-cors mysql-connector-python


------- final --------

python app.py (run this flask file)
open link shown in cmd (ctrl + click on link)
