from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        occupation = request.form.get("occupation")
        date = request.form.get("date")
        print(first_name, last_name, email, occupation, date)
        return render_template("index.html", first_name=first_name,
                               last_name=last_name,
                               email=email, occupation=occupation, date=date)
    else:
        pass
    return render_template("index.html")


app.run(debug=True, port=5000)
