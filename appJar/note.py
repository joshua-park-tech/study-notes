import json
import os
import time

class note_page:
    def __init__(self, id ,year, month, day, note, sidenote, images, subject):
        self.id = id
        self.year = year
        self.month = month
        self.day = day
        self.note = note
        self.sidenote = sidenote
        self.images = images
        self.subject = subject

    def adding_notes_txt(self):
        page = str(self.id) + ";.;" + str(self.year) + ";.;" + str(self.month) + ";.;" + str(self.day) + ";.;" + str(self.note) + ";.;" + str(self.sidenote) + ";.;" + str(self.images) + ";.;" + str(self.subject)

        file_object = open('note_page.txt', 'a')
        file_object.write('\n')
        file_object.write(str(page) + '\n')
        file_object.close()

    def saving_notes(self,added_note, added_sidenote, added_images):
        self.note = added_note
        self.sidenote = added_sidenote
        self.image = added_images



