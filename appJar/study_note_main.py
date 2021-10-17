import random
import time
from appjar import gui
from note import note_page
import json

def confirm():
    j = app.getScale("scale")
    app.setTransparency(j)

def new_page_math():
    pass

def notebook():

    math_data = []
    science_data = []
    # reading from the txt file
    lines = []
    with open('note_page.txt') as f:
        lines = f.readlines()

    for line in lines:
        conv = line.split(";.;")

        if conv[0] == "\n":
            pass
        else:

            print(conv)
            temp_page = note_page(conv[0], conv[1], conv[2], conv[3], conv[4], conv[5], conv[6])

            if conv[6] == "math\n":
                math_data.append(temp_page)

            if conv[6] == "science\n":
                science_data.append(temp_page)

    # app.setStretch("both")
    # app.setSticky("nesw")

    app.setTtkTheme("clam")
    app.startNotebook("Notebook")

    app.startNote("Math")
    app.setFg("blue")

    #start of the notebook pages

    #TODO this is where you need to modify.
    with app.pagedWindow("Math"):
        for pos in range(len(math_data)):
            with app.page():

                app.setStretch("both")
                app.setSticky("nesw")
                app.addImage(str(pos) + "math_sidenote", math_data[pos].images, compound=None)
                app.entry(str(pos)+"math_year", math_data[pos].year, label="year")
                app.entry(str(pos)+"math_month", math_data[pos].month, label="month")
                app.entry(str(pos)+"math_day", math_data[pos].day, label="day")
                app.addTextArea(str(pos) + "math_note")
                app.setTextArea(str(pos) + "math_note", math_data[pos].note, end=True, callFunction=True)
                app.addTextArea(str(pos) + "math_sidenote")
                app.setTextArea(str(pos) + "math_sidenote", math_data[pos].sidenote, end=True, callFunction=True)
                app.addButton(str(pos) + "create page", new_page_math)


    app.startNote("Science")
    app.setFg("blue")

    with app.pagedWindow("Science"):
        for pos in range(len(science_data)):
            with app.page():

                app.setStretch("both")
                app.setSticky("nesw")
                app.addImage(str(pos) + "science_sidenote", science_data[pos].images, compound=None)
                app.entry(str(pos)+"science_year", science_data[pos].year, label="year")
                app.entry(str(pos)+"science_month", science_data[pos].month, label="month")
                app.entry(str(pos)+"science_day", science_data[pos].day, label="day")
                app.addTextArea(str(pos) + "science_note")
                app.setTextArea(str(pos) + "science_note", science_data[pos].note, end=True, callFunction=True)
                app.addTextArea(str(pos) + "science_sidenote")
                app.setTextArea(str(pos) + "science_sidenote", science_data[pos].sidenote, end=True, callFunction=True)

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

    #load data from the json file
    # with open('note_pages.json', 'r') as openfile:
        # Reading from json file
        # json_object = json.load(openfile)

        # Iterating through the json
        # list
        # for i in json_object['subject']:
        #     print(i)
    # seconds = time.time()
    # math1 = note_page(2021,10,3,"the quadratic formula is very important", "check the book no1", "math/qd.png", "math")
    # math1.adding_notes_txt()
    # math2 = note_page(2021, 10, 2, "ayuayayayayay", "yeert", None, "math")
    # math2.adding_notes_txt()

    #these are the data container




    with gui("Updating Labels", useTtk=True) as app:
        app.setSize(600, 800)
        list_names = ["thiiiiiiiiiiiiiiiiiiiiiiiis is a gif.gif"]
        ran_name = random.choice(list_names)
        app.addImage("abc", ran_name)
        login_page()