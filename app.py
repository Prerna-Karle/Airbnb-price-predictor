from flask import Flask, render_template, request
from model import predict_price

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = {
            "bedrooms": int(request.form["bedrooms"]),
            "bathrooms": int(request.form["bathrooms"]),
            "accommodates": int(request.form["accommodates"]),
            "amenities": int(request.form["amenities"]),
        }

        result = predict_price(data)
        return render_template("index.html", result=result)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)