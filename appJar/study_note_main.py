import random
import time
from appjar import gui
from note import note_page
import json


def confirm():
    j = app.getScale("scale")
    app.setTransparency(j)

def new_page_math():
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

    new_page = note_page(str(time.time()), "Year", "Month", "Date", "Your Description here", "Your Side Note here", "noimg.png", "math")
    new_page.adding_notes_txt()

    app.removeAllWidgets()
    notebook()

def change_image():
    print("change image")


def save_notebook():
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
            temp_page = note_page(conv[0], conv[1], conv[2], conv[3], conv[4], conv[5], conv[6], conv[7])

            if conv[7] == "math\n":
                math_data.append(temp_page)

            if conv[7] == "science\n":
                science_data.append(temp_page)
    # app.setStretch("both")
    # app.setSticky("nesw")

    app.setTtkTheme("clam")
    app.startNotebook("Notebook")

    app.startNote("Math")

    app.setFg("green")

    #start of the notebook pages
    with app.pagedWindow("Math"):
        app.setBg("blue")
        for pos in range(len(math_data)):
            with app.page():

                app.setStretch("both")
                app.setSticky("nesw")
                app.addImageButton(str(pos) + "math_sidenote",change_image, math_data[pos].images)
                app.entry(str(pos)+"math_year", math_data[pos].year, label="year")
                app.entry(str(pos)+"math_month", math_data[pos].month, label="month")
                app.entry(str(pos)+"math_day", math_data[pos].day, label="day")
                app.addTextArea(str(pos) + "math_note")
                app.setTextArea(str(pos) + "math_note", math_data[pos].note, end=True, callFunction=True)
                app.addTextArea(str(pos) + "math_sidenote")
                app.setTextArea(str(pos) + "math_sidenote", math_data[pos].sidenote, end=True, callFunction=True)
                app.addButton(str(pos) + "create page", new_page_math)
                app.addButton(str(pos) + "save page", save_notebook)


    app.startNote("Science")
    app.setBg("red")

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
    app.setFg("blue")

    with app.pagedWindow("English"):
        for pos in range(len(science_data)):
            with app.page():

                app.setStretch("both")
                app.setSticky("nesw")
                app.addImage(str(pos) + "English_sidenote", science_data[pos].images, compound=None)
                app.entry(str(pos)+"English_year", science_data[pos].year, label="year")
                app.entry(str(pos)+"English_month", science_data[pos].month, label="month")
                app.entry(str(pos)+"English_day", science_data[pos].day, label="day")
                app.addTextArea(str(pos) + "English_note")
                app.setTextArea(str(pos) + "English_note", science_data[pos].note, end=True, callFunction=True)
                app.addTextArea(str(pos) + "English_sidenote")
                app.setTextArea(str(pos) + "English_sidenote", science_data[pos].sidenote, end=True, callFunction=True)

    app.startNote("Geography")
    app.setFg("blue")

    with app.pagedWindow("Geography"):
        for pos in range(len(science_data)):
            with app.page():

                app.setStretch("both")
                app.setSticky("nesw")
                app.addImage(str(pos) + "Geography_sidenote", science_data[pos].images, compound=None)
                app.entry(str(pos)+"Geography_year", science_data[pos].year, label="year")
                app.entry(str(pos)+"Geography_month", science_data[pos].month, label="month")
                app.entry(str(pos)+"Geography_day", science_data[pos].day, label="day")
                app.addTextArea(str(pos) + "Geography_note")
                app.setTextArea(str(pos) + "Geography_note", science_data[pos].note, end=True, callFunction=True)
                app.addTextArea(str(pos) + "Geography_sidenote")
                app.setTextArea(str(pos) + "Geography_sidenote", science_data[pos].sidenote, end=True, callFunction=True)

    app.startNote("History")
    app.setFg("blue")


    with app.pagedWindow("History"):
        for pos in range(len(science_data)):
            with app.page():

                app.setStretch("both")
                app.setSticky("nesw")
                app.addImage(str(pos) + "History_sidenote", science_data[pos].images, compound=None)
                app.entry(str(pos)+"History_year", science_data[pos].year, label="year")
                app.entry(str(pos)+"History_month", science_data[pos].month, label="month")
                app.entry(str(pos)+"History_day", science_data[pos].day, label="day")
                app.addTextArea(str(pos) + "History_note")
                app.setTextArea(str(pos) + "History_note", science_data[pos].note, end=True, callFunction=True)
                app.addTextArea(str(pos) + "History_sidenote")
                app.setTextArea(str(pos) + "History_sidenote", science_data[pos].sidenote, end=True, callFunction=True)
    app.stopNotebook()

# def save_notebook_math():
#     app.getEntry(str(pos) + "math_note")

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

    with gui("Updating Labels", useTtk=True) as app:
        app.setSize(800, 500)
        list_names = ["thiiiiiiiiiiiiiiiiiiiiiiiis is a gif.gif"]
        ran_name = random.choice(list_names)
        app.addImage("abc", ran_name)
        login_page()