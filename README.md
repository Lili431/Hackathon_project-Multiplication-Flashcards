# Hackathon_project-Multiplication-Flashcards
This is a small project I decided to do for the CS girlies hackathon. I decided to create a small multiplication flashcard web app for multiples of 1-12
My target audience is children who are starting to learn how to multiply. As a kid, I remember struggling with my multiplication tables
in third grade. Trying to remember all the multiples, how to solve them, and especially trying to be engaged in my studying of multiplication.
This web app is very simple and fun for anyone who would want to learn how to do simple multiplication using an interactive flip style flashcards.
To build this project, I used python, flask, HTML, CSS, and JavaScript.

Tools:
->Python: Backend
->HTML: Structure webpages
->Flask: Webserver
->CSS: Styling it to make it pretty
->JavaScript: flashcard logic, flipping and checking answers

Features:
->Enter a number from 1-12 to generate a flashcard deck
->Each Flashcard will show a multiplication problem
->kid friendly
->Users can type their answer and will recieve feedback based on their answer
->If an answer is wrong, a flip animation button will appear to show user the correct answer
->Goes through the deck one at a time
->home button to take you back to main page.

Project Structure:
Hackathon_project/
├-->app.py  #Flask app
├─->flashcards.py  #Generates multiplication card deck
├--> templates/
│   ├─-> index.html  #My home page
│   └──> next_page.html  #My flashcard page
├──->static/
│   ├──> index.css   #Home page styling
│   ├──> next_page.css  #Flashcard styling
│   └──> project_picture.jpg #Background image
└──> README.md    #Project documentation

Run project:
To run this project, you would have to download flask in your computer in the terminal using "pip3 install flask" if you are using python3.
Then you will run app.py after downloading flask. After running app.py, you will use this link "http://127.0.0.1:5000" in your designated
browser to go onto the webapp.

How the project works:
A user will enter a number from 1 to 12 on the home page. After that number is entered, flask will create a deck using the Flashcards.py logic.
Flashcards will apear one at a time as the user will enter an answer and Javascript will see if it's correct. If an answer in wrong, a button will apear that will let the user flip the card to see the right answer. The deck will continue until it is done.

Created by
Liliana Trejo

