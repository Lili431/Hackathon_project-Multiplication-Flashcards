from flask import Flask, render_template, request
from flashcards import multiples_card

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    multiple = request.args.get("max_factor", type=int)#Get number user typed in index.html
    if not multiple: #If user typed nothing or invalid, default to 1
        multiple = 1
    deck = multiples_card(multiple)#create deck using the correct number
    return render_template("next_page.html", multiple=multiple, deck=deck)

if __name__ == "__main__":
    app.run(debug=True)
