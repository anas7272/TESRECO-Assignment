from app import app
from flask import Flask, render_template , request, jsonify 

@app.route("/add-intern", methods=["GET", "POST"])
def add_intern():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        domain = request.form["domain"]

        conn = sqlite3.connect(
            "database/interns.db"
        )

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Interns(
            name,
            email,
            domain
        )
        VALUES (?, ?, ?)
        """,
        (
            name,
            email,
            domain
        ))

        conn.commit()
        conn.close()

        return redirect("/view-interns")

    return render_template(
        "add_intern.html"
    )