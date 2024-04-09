from flask import Flask, render_template
from mongo_tryout import Creature

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/creatures")
def creatures():
    all_creatures = Creature.objects()
    return render_template("creatures.html",
                           all_creatures=all_creatures)


if __name__ == "__main__":
    app.run(debug=True)
