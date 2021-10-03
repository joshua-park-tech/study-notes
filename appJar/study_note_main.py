import random
from appjar import gui


def confirm():
    j = app.getScale("scale")
    app.setTransparency(j)

def notebook():
    app.setTtkTheme("clam")
    app.startNotebook("Notebook")

    app.startNote("Math")

    #start of the notebook pages
    app.startPagedWindow("Math Page")

    #these pages need to be duplicated by itself.
    app.startPage()
    app.addScrolledTextArea("t1")
    app.addScrolledTextArea("t2")
    app.stopPage()

    app.startPage()
    app.addLabel("p2", "Label 2")
    app.stopPage()

    app.startPage()
    app.addLabel("p3", "Label 3")
    app.stopPage()

    app.startPage()
    app.addLabel("p4", "Label 4")
    app.stopPage()
    app.stopPagedWindow()

    app.stopNote()

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

    app = gui("Notebook", useTtk=True)
    app.setSize(600, 420)

    list_names = ["thiiiiiiiiiiiiiiiiiiiiiiiis is a gif.gif"]
    ran_name = random.choice(list_names)
    app.addImage("abc", ran_name)


    #app.setImageSize("abc", 400, 500)

    login_page()
    app.go()
