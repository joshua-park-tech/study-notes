import random
from appjar import gui

app = gui("Guide to wiping out Ganon from this Universe", "1000x550")
print("Guide to demolish Ganon")

def press():
    pass
def launch(win):
    app.showSubWindow(win)


if __name__ == "__main__":
    app.addFlashLabel("die", "You wanna kick Ganon out of Hyrule Castle with a tree branch and stuff?")
    #app.addImage("memes", "ezgif-2-e07e7cb62724.gif")

    # these go in the main window

    app.addButtons(["Thunderblight Ganon", "Windblight Ganon", "Waterblight Ganon", "Fireblight Ganon", "Calamity Ganon", "Dark Beast Ganon"], launch)

    # app.addImage("stasis zelda", "zelda-being-great-for-the-first-time-in-her-life.gif")
    # app.setImageSize("stasis zelda", 100, 100)
    # # app.addImage("bad zelda", "zelda-is-bad.gif")
    # # app.addImage("scared zelda", "zelda-is-scared.gif")
    # # app.addImage("frog zelda", "zelda-makes-link-eat-a-frog.gif")

    # this is a pop-up
    app.startSubWindow("Thunderblight Ganon", modal=True)
    app.addLabel("sed", "kill")
    app.addImage("gif", "tumblr_ou8k3q8gex1unzyd3o1_500.gif")
    app.addTextArea('t1')
    app.setTextArea("t1", "if you are good at parries, parry thunderblight and smack the shield before stunning him again. feel free to attack while stunned."
                          "if you are good at flurry rushes, continue flurry rushing"
                          "second phrase, if thunderblight chuchs metal pillars at you, magnesis them and attack them at thunderblight and resume attacking, parrying, flurry rushing after"
                    , end=True, callFunction=True)

    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("Windblight Ganon")
    app.addLabel("arr", "SubWindow Two")
    app.addTextArea('t2')
    app.setTextArea("t2", "get the point. with your strongest bow, shoot ganon with arrows, preferably on the eye with bomb arrows, and if you manage to make windblight get stunned and drop to the ground, spin attack with any powerful two-handed weapon.", end=True, callFunction=True)
    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("Waterblight Ganon")
    app.addLabel("yar", "SubWindow Two")
    app.addTextArea('t3')
    app.setTextArea("t3", "flurry rush or dodge ganon spears and shoot him on the eye. After stunned, hit repeatedly with weapon. Second phrase, stasis icicle cubes and smack the back at ganon to stun. Smack again. Shoot on eye if necessary. Repeat until dead.", end=True, callFunction=True)
    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("Fireblight Ganon")
    app.addLabel("bsg", "SubWindow Two")
    app.addTextArea('t4')
    app.setTextArea("t4", "Similar to Waterblight, flurry rush and stun with ice arrows. Afterwards, in phrase 2, when Ganon goes over and sucks in air, chuck a big boy remote bomb to stun. Smack with weapon. Repeat until dead.", end=True, callFunction=True)
    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("Calamity Ganon")
    app.addLabel("qwert", "SubWindow Two")
    app.addTextArea('t5')
    app.setTextArea("t5", "Finale!, Big boi will use every single attack the previous ganons used. Time to test your skill. Flurry rushing works like crazy. The second phrase. Ganon starts to turn orange and shoots lasers. Use urbosa's fury to stun and attack or stick to furry rushing and parrying.", end=True, callFunction=True)
    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("Dark Beast Ganon")
    app.addLabel("sdf", "SubWindow Two")
    app.addTextArea('t6')
    app.setTextArea("t6", "Big fat cheese. Don't forget to take a picture with Dark Beast. Get the bow of light. Savour it, it'll be the only time you will be allowed to use it. Shoot glowing areas. Use stop motion archery in midair to shoot the last arrow into the core! DONE", end=True, callFunction=True)
    app.stopSubWindow()

    app.setLabelBg("die", "red")
    # app.addButton("Thunderblight Ganon3", press)
    # app.addButton("Windblight Ganon3", press)
    # app.addButton("Waterblight Ganon3", press)
    # app.addButton("Firebllight Ganon3", press)
    # app.addButton("Calamity Ganon3", press)
    # app.addButton("Dark Beast Ganon3", press)

    list_names = ["zelda-being-great-for-the-first-time-in-her-life.gif", "zelda-is-bad.gif", "zelda-is-scared.gif", "m.gif"]
    ran_name = random.choice(list_names)
    app.addImage( "abc",ran_name)

    # app.addImage("stasis zelda", "zelda-being-great-for-the-first-time-in-her-life.gif")
    app.setImageSize("abc", 400, 500)

    app.go()