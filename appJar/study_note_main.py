import random
import time
from appjar import gui
from note import note_page
import json

current_page = "stuff"
global pos

def confirm():
    j = app.getScale("scale")
    app.setTransparency(j)

def new_page_math():
    new_page = note_page(str(time.time()), "Year", "Month", "Date", "Your Description here", "Your Side Note here",
                         "noimg.png", "math")
    new_page.adding_notes_txt()

    app.removeAllWidgets()
    notebook()


def change_image():
    print("change image")

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

    def save_notebook():
        print(math_data[pos].id)
        with open('note_page.txt', 'r') as input_file, open('new_file', 'w') as output_file:
            for line in input_file:
                print(line)
                conv = line.split(";.;")
                current_id = conv[0]

                if current_id == math_data[pos].id in line:
                    pass

                    # print(conv)

                    # adding the page

                    output_file.write('new line\n')
                else:
                    output_file.write(line)
                    pass


    # start of the notebook pages
    with app.pagedWindow("Math"):

        for pos in range(len(math_data)):
            with app.page():

                # global current_page
                # current_page =

                app.setStretch("both")
                app.setSticky("nesw")
                app.addImageButton(str(pos) + "math_sidenote", change_image, math_data[pos].images)
                app.entry(str(pos) + "math_year", math_data[pos].year, label="year")
                app.entry(str(pos) + "math_month", math_data[pos].month, label="month")
                app.entry(str(pos) + "math_day", math_data[pos].day, label="day")
                app.addTextArea(str(pos) + "math_note")
                app.setTextArea(str(pos) + "math_note", math_data[pos].note, end=True, callFunction=True)
                app.addTextArea(str(pos) + "math_sidenote")
                app.setTextArea(str(pos) + "math_sidenote", math_data[pos].sidenote, end=True, callFunction=True)
                app.addButton(str(pos) + "create page", new_page_math)
                app.addButton(str(pos) + "save page", save_notebook)


    app.startNote("Science")

    with app.pagedWindow("Science"):
        for pos in range(len(science_data)):
            with app.page():
                app.setStretch("both")
                app.setSticky("nesw")
                app.addImage(str(pos) + "science_sidenote", science_data[pos].images, compound=None)
                app.entry(str(pos) + "science_year", science_data[pos].year, label="year")
                app.entry(str(pos) + "science_month", science_data[pos].month, label="month")
                app.entry(str(pos) + "science_day", science_data[pos].day, label="day")
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
                app.entry(str(pos) + "English_year", science_data[pos].year, label="year")
                app.entry(str(pos) + "English_month", science_data[pos].month, label="month")
                app.entry(str(pos) + "English_day", science_data[pos].day, label="day")
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
                app.entry(str(pos) + "Geography_year", science_data[pos].year, label="year")
                app.entry(str(pos) + "Geography_month", science_data[pos].month, label="month")
                app.entry(str(pos) + "Geography_day", science_data[pos].day, label="day")
                app.addTextArea(str(pos) + "Geography_note")
                app.setTextArea(str(pos) + "Geography_note", science_data[pos].note, end=True, callFunction=True)
                app.addTextArea(str(pos) + "Geography_sidenote")
                app.setTextArea(str(pos) + "Geography_sidenote", science_data[pos].sidenote, end=True,
                                callFunction=True)

    app.startNote("History")
    app.setFg("blue")

    with app.pagedWindow("History"):
        for pos in range(len(science_data)):
            with app.page():
                app.setStretch("both")
                app.setSticky("nesw")
                app.addImage(str(pos) + "History_sidenote", science_data[pos].images, compound=None)
                app.entry(str(pos) + "History_year", science_data[pos].year, label="year")
                app.entry(str(pos) + "History_month", science_data[pos].month, label="month")
                app.entry(str(pos) + "History_day", science_data[pos].day, label="day")
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
    with gui("Updating Labels", useTtk=True, useSettings=True) as app:
        app.setSize(300, 800)
        list_names = ["thiiiiiiiiiiiiiiiiiiiiiiiis is a gif.gif"]
        ran_name = random.choice(list_names)
        app.addImage("abc", ran_name)
        login_page()
