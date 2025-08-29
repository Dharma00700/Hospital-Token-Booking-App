
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Doctor mapping based on room
DOCTOR_MAP = {
    1: "Dr. Ramesh (Pediatrician)",
    2: "Dr. Priya (General Physician)",
    3: "Dr. Arun (Orthopedic)",
    4: "Dr. Meena (Cardiologist)",
    5: "Dr. Kiran (Senior Specialist)"
}

def assign_room(age: int) -> int:
    if 1 <= age <= 20:
        return 1
    elif 21 <= age <= 40:
        return 2
    elif 41 <= age <= 60:
        return 3
    elif 61 <= age <= 80:
        return 4
    elif 81 <= age <= 100:
        return 5
    else:
        return 0

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name", "").strip()
    age_raw = request.form.get("age", "").strip()

    if not name or not age_raw.isdigit():
        return redirect(url_for("home"))

    age = int(age_raw)
    room = assign_room(age)
    if room == 0:
        return render_template("token.html", name=name, age=age, room="N/A", doctor="N/A", invalid=True)

    doctor = DOCTOR_MAP[room]
    return render_template("token.html", name=name, age=age, room=room, doctor=doctor, invalid=False)

if __name__ == "__main__":
    # Use host='0.0.0.0' so it works on local networks too; remove if not needed.
    app.run(host="0.0.0.0", port=5000, debug=True)
