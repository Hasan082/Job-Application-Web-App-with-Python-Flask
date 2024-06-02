from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

# Create Flask app
app = Flask(__name__)

# Configure Flask-SQLAlchemy
app.config["SECRET_KEY"] = "jobAplication"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "dr.has82@gmail.com"
app.config["MAIL_PASSWORD"] = "wxvpiyopaayrwlhs"
db = SQLAlchemy(app)

# Configure Flask-Mail
mail = Mail(app)


# Define database model
class formData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date)

# Define routes
@app.route("/", methods=["GET", "POST"])
def index():
    # Handle form submission
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

        # mail body
        msg_body = f"Thank you for expressing interest in the position, {first_name}. We appreciate your application and will review it carefully. Expect to hear from us soon regarding the next steps in the hiring process. Here is your data: \n\nFirst Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nOccupation: {occupation}\nDate: {date}. \nThank you!"

        # Arrange message for sending data to user
        msg = Message(
            subject="Job Application in the position",
            sender=app.config["MAIL_USERNAME"],
            recipients=[email],
            body=msg_body,
        )

        # Deliver email
        mail.send(msg)

        # Show success message to user 
        flash("Thank you for expressing interest in the position. We appreciate your application and will review it carefully. Expect to hear from us soon regarding the next steps in the hiring process.", "success")

        # redirect to same page auto resubmit
        return redirect(url_for("index"))

    return render_template("index.html")


# Run Flask app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)
