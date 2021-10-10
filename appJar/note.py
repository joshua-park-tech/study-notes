import json
import os

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
               "images":self.images,
               "subject": self.subject,
               }

        DATA_FILENAME = "note_pages.json"
        if os.stat("note_pages.json").st_size == 0:
            json_object = json.dumps(page)
            # file_name = str(self.subject) + "_note.json"
            with open("note_pages.json","w") as outfile:
                outfile.write(json_object)
            # with open(DATA_FILENAME, mode='w', encoding='utf-8') as f:
            #     json.dump([], f)
        else:
            pass
            # with open(DATA_FILENAME, mode='r', encoding='utf-8') as feedsjson:
            #     feeds = json.load(feedsjson)
            #
            # with open(DATA_FILENAME, mode='w', encoding='utf-8') as feedsjson:
            #     entry = page
            #     feeds.append(entry)
            #     json.dump(feeds, feedsjson)