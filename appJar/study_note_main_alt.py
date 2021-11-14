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


def save_notebook():
    print(pos)
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

    # app.setTtkTheme("clam")
    # app.startNotebook("Notebook")
    # app.startNote("Math")


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

    app.addButton(str(pos) + "create page", new_page_math)
    app.addButton(str(pos) + "save page", save_notebook)



if __name__ == "__main__":
    with gui("Updating Labels") as app:
        app.entry("First Name", label=True)
        app.entry("Last Name", label=True)
        app.entry("Country", label=True)
        app.entry("Age", kind='numeric', label=True)
        app.buttons(["Previous", "Next"], notebook)
        notebook("Next")