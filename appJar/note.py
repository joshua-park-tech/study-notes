import json
import os

class note_page:
    def __init__(self, year, month, day, note, sidenote, images, subject):
        self.id = id
        self.year = year
        self.month = month
        self.day = day
        self.note = note
        self.sidenote = sidenote
        self.images = images
        self.subject = subject

    def adding_notes_txt(self):
        page = str(self.year) + ";.;" + str(self.month) + ";.;" + str(self.day) + ";.;" + str(self.note) + ";.;" + str(self.sidenote) + ";.;" + str(self.images) + ";.;" + str(self.subject)


        file_object = open('note_page.txt', 'a')
        file_object.write('\n')
        file_object.write(str(page) + '\n')
        file_object.close()

