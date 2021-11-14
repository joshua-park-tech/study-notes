import random
import time
from appjar import gui
from note import note_page
import json


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



data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4],
        ["Bart", "Simpson", "America", 14]]

pos = -1

def notebook(btn):
    global pos
    if btn == "Next": pos += 1
    elif btn == "Previous": pos -= 1

    if pos == 0:
        app.disableButton("Previous")
    elif pos == len(data)-1:
        app.disableButton("Next")
    else:
        app.enableButton("Previous")
        app.enableButton("Next")

    app.entry("First Name", data[pos][0])
    app.entry("Last Name", data[pos][1])
    app.entry("Country", data[pos][2])
    app.entry("Age", data[pos][3])



if __name__ == "__main__":
    with gui("Updating Labels") as app:
        app.entry("First Name", label=True)
        app.entry("Last Name", label=True)
        app.entry("Country", label=True)
        app.entry("Age", kind='numeric', label=True)
        app.buttons(["Previous", "Next"], notebook)
        notebook("Next")