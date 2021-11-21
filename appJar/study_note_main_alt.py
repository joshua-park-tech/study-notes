import random
import time
from appjar import gui
from note import note_page
import json

def new_page_math():
    new_page = note_page(str(time.time()), "Year", "Month", "Date", "Your Description here", "Your Side Note here",
                         "noimg.png", "math")
    new_page.adding_notes_txt()

    app.removeAllWidgets()
    notebook()


def change_image():
    print("change image")


math_data = []


def loading_pages():
    global math_data
    global science_data
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
    elif pos == len(math_data)-1:
        app.disableButton("Next")
    else:
        app.enableButton("Previous")
        app.enableButton("Next")

    app.entry("Year", math_data[pos].year)
    app.entry("Month", math_data[pos].month)
    app.entry("Day", math_data[pos].day)
    app.addTextArea("Note", math_data[pos].note)





if __name__ == "__main__":
    with gui("Updating Labels") as app:
        app.entry("Year", label=True)
        app.entry("Month", label=True)
        app.entry("Day", label=True)
        app.addTextArea("Note")
        app.buttons(["Previous", "Next"], notebook)
        app.addButton("create page", new_page_math)
        app.addButton("save page", save_notebook)
        notebook("Next")