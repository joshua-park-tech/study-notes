import random
from appjar import gui
import json
from note import note_page


def confirm():
    j = app.getScale("scale")
    app.setTransparency(j)

def notebook():                    

    app.setTtkTheme("clam")
    app.startNotebook("Notebook")

    app.startNote("Math")

    #start of the notebook pages
    with app.pagedWindow("Math Page"):
        for pos in range(len(math_data)):
            with app.page():
                app.entry(str(pos)+"year", math_data[pos].year, label="year")
                app.entry(str(pos)+"month", math_data[pos].month, label="month")
                app.entry(str(pos)+"day", math_data[pos].day, label="day")
                app.addTextArea(str(pos) + "note")
                app.setTextArea(str(pos) + "note", math_data[pos].note, end=True, callFunction=True)
                app.addTextArea(str(pos) + "sidenote")
                app.setTextArea(str(pos) + "sidenote", math_data[pos].sidenote, end=True, callFunction=True)
                

    app.startNote("Science")
    app.addLabel("l2", "Science")
    app.stopNote()

    app.startNote("English")
    app.addLabel("l3", "English")
    app.stopNote()

    app.startNote("Geography")
    app.addLabel("l4", "Geography")
    app.stopNote()

    app.startNote("History")
    app.addLabel("l5", "History")
    app.stopNote()

    app.stopNotebook()

def login_check():
    pw = app.getEntry("Password")
    ppw = app.getEntry("Username")
    if pw == "1234" and ppw == "people":
        app.removeAllWidgets()
        notebook()
    else:
        print("Forgot password or ID?")

def login_page():
    app.addLabel("MY NOTEBOOK")
    app.addEntry("Username")
    app.addSecretEntry("Password")

    app.addButton("login", login_check)

if __name__ == '__main__':

    #TODO handling data needed

    math1 = note_page(2021,10,3,"the quadratic formula is very important", "check the book no1", None)
    math2 = note_page(2021, 10, 2, "ayuayayayayay", "yeert", None)
    math_data = [math1, math2]

    with gui("Updating Labels", useTtk=True) as app:
        app.setSize(600, 420)
        list_names = ["thiiiiiiiiiiiiiiiiiiiiiiiis is a gif.gif"]
        ran_name = random.choice(list_names)
        app.addImage("abc", ran_name)
        login_page()