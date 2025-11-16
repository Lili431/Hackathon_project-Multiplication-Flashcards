from flask import Flask, render_template, request
from flashcards import multiples_card

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    multiple = request.args.get("multiple", type=int, default=1)# Get selected multiple
    deck = multiples_card(multiple)# Create flashcard deck in Python
    return render_template("next_page.html", multiple=multiple, deck=deck) # Send deck + the chosen number to HTML

if __name__ == "__main__":
    app.run(debug=True)
