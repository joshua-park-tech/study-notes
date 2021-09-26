from appjar import gui

def launch(win):
    app.showSubWindow(win)


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

def login_check():
    pw = app.getEntry("Password")
    if pw == "QWERTY":
        # this is a pop-up
        app.startSubWindow("Notes", modal=True)
        app.addLabel("sub1", "SubWindow One")
        app.setTtkTheme("clam")

        app.startNotebook("Notebook")
        app.startNote("Note 1")
        app.addLabel("l1", "Note 1")
        app.stopNote()
        app.startNote("Note 2")
        app.addLabel("l2", "Note 2")
        app.stopNote()
        app.startNote("Note 3")
        app.addLabel("l3", "Note 3")
        app.stopNote()
        app.stopNotebook()
        app.stopSubWindow()

    else:
        print("FORGOT PASSWORD? OR HACKER!")


if __name__ == '__main__':
    app = gui("Notebook", useTtk=True)

    app.addSecretEntry("Password")

    app.addButton("login", login_check)



    app.go()
