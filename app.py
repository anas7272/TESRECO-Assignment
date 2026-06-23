from flask import Flask, render_template , request, jsonify , redirectd
import sqlite3

app = Flask(__name__)

#for index
@app.route("/")
def home():
    return render_template("index.html")

# for about
@app.route("/about")
def about():
    return render_template("about.html",
                           overview="TESRECO provides industry-oriented internship programs.",

        domains=[
            "AI/ML",
            "Data Science",
            "Python Development",
            "Web Development"
        ],

        mission="Bridge the gap between academics and industry.",

        vision="Create skilled professionals ready for real-world challenges."
    )

#create
@app.route("/register" , methods = ["GET", "POST"])
def register():

    if request.method =="GET":
        return "Registeration is working."
    
    data = request.get_json()

    conn = sqlite3.connect("database/interns.db")
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO Interns (name, email, domain)
                   VALUES(?, ?, ?)""",
                   (    
                    data["name"],
                    data["email"],
                    data["domain"]
                    ))


    conn.commit()
    conn.close()
    return {
        "message": "Intern Registered Sucessfyully"
    }


#Read
@app.route("/interns", methods=["GET"])
def get_interns():
    conn = sqlite3.connect("database/interns.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Interns"
    )
    records = cursor.fetchall()
    conn.close()
    return jsonify(records)

#update
@app.route("/intern/<int:id>", methods=["PUT"])
def update_interns():
    data = request.get_json()
    conn = sqlite3.connect("database/interns.db")

    cursor = conn.cursor()

    cursor.execute("""
                   UPDATE Interns
                   SET name=?,
                   email=?,
                   domain=?
                   WHERE id=?
                   """,
                   (
                       data["name"],
                       data["email"],
                       data["domain"],
                       id
                   ))
    conn.commit()
    conn.close()
    return {
        "message" : " Inters Updated Successful"
    }

#delete
@app.route("/interns/<int:id>", methods=["DELETE"])
def delete_intern(id):
    conn = sqlite3.connect("database/interns.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM Interns
        WHERE id=?
        """,
        (id,)
            )
    conn.commit()
    conn.close()
    return {
        "message" : f"Inter {id} Deleted"
    }



#Attandance

@app.route("/attendance" , methods=["POST"])
def attendance():
    data = request.get_json()
    conn = sqlite3.connect("database/attandance.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Attendance(
            intern_id,
            date,
            status
        )
        VALUES (?, ?, ?)
                """,
                (
                    data["interns_id"],
                    data["date"],
                    data["status"]
                )
    )
    conn.commit()
    conn.close()
    return {
        "message" : "Attandance recorded."
    }

#assignment

@app.route("/assignment" , methods=["POST"])
def assig_mentor():
    data = request.get_json()

    conn = sqlite3.connect("database/assignment.db")
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO Assignments(
                   intern_id,
                   mentor_id
                   )
                   VALUES (?, ?)
                   """,
                   (
                   data["intern_id"],
                   data["mentor_id"]))
    conn.commit()
    conn.close()
    return {
        "message" : "Mentor Assigned Successfully"
    }


#creating web page

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

@app.route("/view-intern")
def view_interns():

    conn = sqlite3.connect(
        "database/interns.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Interns"
    )

    interns = cursor.fetchall()

    conn.close()

    return render_template(
        "view_intern.html",
        interns=interns
    )

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_intern(id):

    conn = sqlite3.connect(
        "database/interns.db"
    )

    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]

        email = request.form["email"]

        domain = request.form["domain"]

        cursor.execute("""
        UPDATE Interns

        SET
        name=?,
        email=?,
        domain=?

        WHERE id=?
        """,
        (
            name,
            email,
            domain,
            id
        ))

        conn.commit()

        conn.close()

        return redirect(
            "/view-interns"
        )

    cursor.execute(
        "SELECT * FROM Interns WHERE id=?",
        (id,)
    )

    intern = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_intern.html",
        intern=intern
    )

@app.route("/delete/<int:id>")
def delete_intern_page(id):

    conn = sqlite3.connect(
        "database/interns.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Interns WHERE id=?",
        (id,)
    )

    conn.commit()

    conn.close()

    return redirect(
        "/view-intern"
    )


if __name__ == "__main__":
    app.run(debug=True)