from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "jobAplication"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class formData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        occupation = request.form.get("occupation")
        date = request.form.get("date")
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        
        # Process form data
        form = formData(
            first_name=first_name,
            last_name=last_name,
            email=email,
            occupation=occupation,
            date=date_obj,
        )

        # Add form data to database
        db.session.add(form)
        db.session.commit()

        # Show success message to user 
        flash("Thank you for expressing interest in the position. We appreciate your application and will review it carefully. Expect to hear from us soon regarding the next steps in the hiring process.", "success")

        # redirect to same page auto resubmit
        return redirect(url_for("index"))

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)
