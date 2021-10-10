import json
class note_page:
    def __init__(self, year, month, day, note, sidenote, images, subject):
        self.year = year
        self.month = month
        self.day = day
        self.note = note
        self.sidenote = sidenote
        self.images = images
        self.subject = subject

    def adding_notes_json(self):
        page = { "year":self.year,
               "month":self.month,
               "day":self.day,
               "note":self.note,
               "sidenote":self.sidenote,
               "images":self.images
               }

        json_object = json.dumps(page)
        file_name = str(self.subject) + "_note.json"
        with open(file_name, "w") as outfile:
            outfile.write(json_object)