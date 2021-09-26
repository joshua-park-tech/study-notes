from appjar import gui

def confirm():
    j = app.getScale("scale")
    app.setTransparency(j)

def notebook():
    app.setSize(600, 400)
    # app.setFont(21)
    # app.addLabelScale("scale")
    # app.setScale("scale", 50)
    # app.addButton("scale confirm life", confirm)
    # app.go()
    #app.hide("")

    app.setTtkTheme("clam")
    app.startNotebook("Notebook")

    app.startNote("Math")

    #start of the notebook pages
    app.startPagedWindow("Math Page")

    #these pages need to be duplicated by itself.
    app.startPage()
    app.addTextArea("t1")
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
    if pw == "1234":
        app.removeAllWidgets()
        notebook()
    else:
        print("FORGOT PASSWORD? OR HACKER")


if __name__ == '__main__':
    app = gui("Notebook", useTtk=True)

    app.addSecretEntry("Password")

    app.addButton("login", login_check)
    app.go()
