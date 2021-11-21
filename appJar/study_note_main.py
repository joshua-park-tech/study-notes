import random
import time
from appjar import gui
from note import note_page
import json

current_page = "stuff"
pos_math = -1
pos_science = 0
pos_history = 0

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

def save_notebook():
    global pos_math
    print(pos_math)
        # with open('note_page.txt', 'r') as input_file, open('new_file', 'w') as output_file:
        #     for line in input_file:
        #         print(line)
        #         conv = line.split(";.;")
        #         current_id = conv[0]
        #
        #         if current_id == math_data[pos].id in line:
        #             pass
        #
        #             # print(conv)
        #
        #             # adding the page
        #
        #             output_file.write('new line\n')
        #         else:
        #             output_file.write(line)
        #             pass


def notebook(btn):
    global pos_math
    global pos_history
    global pos_science

    if btn == "Next":
        print(pos_math)
        pos_math += 1

    elif btn == "Previous":
        pos_math -= 1

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

    if pos_math == 0:
        # app.disableButton("Previous")
        pass
    elif pos_math == len(math_data) - 1:
        app.disableButton("Next")
    else:
        app.enableButton("Previous")
        app.enableButton("Next")


    app.setStretch("both")
    app.setSticky("nesw")
    # app.addImageButton(str(pos_math) + "math_sidenote", change_image, math_data[pos_math].images)
    # app.entry(str(pos_math) + "math_year", math_data[pos_math].year)
    # app.entry(str(pos_math) + "math_month", math_data[pos_math].month)
    # app.entry(str(pos_math) + "math_day", math_data[pos_math].day)
    app.clearEntry("math_note", callFunction=False)
    app.clearEntry("math_sidenote", callFunction=False)
    app.setTextArea("math_note", math_data[pos_math].note, end=True, callFunction=True)
    app.setTextArea("math_sidenote", math_data[pos_math].sidenote, end=True, callFunction=True)
    # app.addButton("create page", new_page_math)
    # app.addButton("save page", save_notebook)


    # app.startNote("Science")
    #
    # with app.pagedWindow("Science"):
    #     for pos in range(len(science_data)):
    #         with app.page():
    #             app.setStretch("both")
    #             app.setSticky("nesw")
    #             app.addImage(str(pos) + "science_sidenote", science_data[pos].images, compound=None)
    #             app.entry(str(pos) + "science_year", science_data[pos].year, label="year")
    #             app.entry(str(pos) + "science_month", science_data[pos].month, label="month")
    #             app.entry(str(pos) + "science_day", science_data[pos].day, label="day")
    #             app.addTextArea(str(pos) + "science_note")
    #             app.setTextArea(str(pos) + "science_note", science_data[pos].note, end=True, callFunction=True)
    #             app.addTextArea(str(pos) + "science_sidenote")
    #             app.setTextArea(str(pos) + "science_sidenote", science_data[pos].sidenote, end=True, callFunction=True)
    #
    # app.startNote("English")
    # app.setFg("blue")
    #
    # with app.pagedWindow("English"):
    #     for pos in range(len(science_data)):
    #         with app.page():
    #             app.setStretch("both")
    #             app.setSticky("nesw")
    #             app.addImage(str(pos) + "English_sidenote", science_data[pos].images, compound=None)
    #             app.entry(str(pos) + "English_year", science_data[pos].year, label="year")
    #             app.entry(str(pos) + "English_month", science_data[pos].month, label="month")
    #             app.entry(str(pos) + "English_day", science_data[pos].day, label="day")
    #             app.addTextArea(str(pos) + "English_note")
    #             app.setTextArea(str(pos) + "English_note", science_data[pos].note, end=True, callFunction=True)
    #             app.addTextArea(str(pos) + "English_sidenote")
    #             app.setTextArea(str(pos) + "English_sidenote", science_data[pos].sidenote, end=True, callFunction=True)
    #
    # app.startNote("Geography")
    # app.setFg("blue")
    #
    # with app.pagedWindow("Geography"):
    #     for pos in range(len(science_data)):
    #         with app.page():
    #             app.setStretch("both")
    #             app.setSticky("nesw")
    #             app.addImage(str(pos) + "Geography_sidenote", science_data[pos].images, compound=None)
    #             app.entry(str(pos) + "Geography_year", science_data[pos].year, label="year")
    #             app.entry(str(pos) + "Geography_month", science_data[pos].month, label="month")
    #             app.entry(str(pos) + "Geography_day", science_data[pos].day, label="day")
    #             app.addTextArea(str(pos) + "Geography_note")
    #             app.setTextArea(str(pos) + "Geography_note", science_data[pos].note, end=True, callFunction=True)
    #             app.addTextArea(str(pos) + "Geography_sidenote")
    #             app.setTextArea(str(pos) + "Geography_sidenote", science_data[pos].sidenote, end=True,
    #                             callFunction=True)
    #
    # app.startNote("History")
    # app.setFg("blue")
    #
    # with app.pagedWindow("History"):
    #     for pos in range(len(science_data)):
    #         with app.page():
    #             app.setStretch("both")
    #             app.setSticky("nesw")
    #             app.addImage(str(pos) + "History_sidenote", science_data[pos].images, compound=None)
    #             app.entry(str(pos) + "History_year", science_data[pos].year, label="year")
    #             app.entry(str(pos) + "History_month", science_data[pos].month, label="month")
    #             app.entry(str(pos) + "History_day", science_data[pos].day, label="day")
    #             app.addTextArea(str(pos) + "History_note")
    #             app.setTextArea(str(pos) + "History_note", science_data[pos].note, end=True, callFunction=True)
    #             app.addTextArea(str(pos) + "History_sidenote")
    #             app.setTextArea(str(pos) + "History_sidenote", science_data[pos].sidenote, end=True, callFunction=True)
    # app.stopNotebook()


# def save_notebook_math():
#     app.getEntry(str(pos) + "math_note")

def login_check():
    pw = app.getEntry("Password")
    ppw = app.getEntry("Username")
    if pw == "1234" and ppw == "people":
        app.removeAllWidgets()
        next_prev_button()
        notebook("Next")
    else:
        print("Forgot password or ID?")


def login_page():
    app.addLabel("MY NOTEBOOK")
    app.addEntry("Username")
    app.addSecretEntry("Password")
    app.addButton("login", login_check)

def next_prev_button():
    app.removeAllWidgets()
    # app.addImageButton("math_sidenote")
    app.entry("math_year")
    app.entry("math_month")
    app.entry("math_day")
    app.addTextArea("math_note")
    # app.setTextArea("math_note")
    app.addTextArea("math_sidenote")
    # app.setTextArea("math_sidenote")
    app.buttons(["Previous", "Next"], notebook)
    app.buttons(["create page", "save page"], save_new)

def save_new(btn):
    if btn == "save page":
        save_notebook()

    elif btn == "create page":
        new_page_math()


if __name__ == '__main__':
    with gui("Updating Labels", useTtk=True, useSettings=True) as app:
        app.setSize(300, 800)
        list_names = ["thiiiiiiiiiiiiiiiiiiiiiiiis is a gif.gif"]
        ran_name = random.choice(list_names)
        app.addImage("abc", ran_name)
        login_page()
