from subscenery.scrapper import SubSceneScrapper
from tkinter import Tk, filedialog, Label, Listbox, ACTIVE
from tkinter import ttk
import os

win = Tk()


class Application(Tk):
    def __init__(self):
        ttk.Button(win, text='Choose a media file', command=self.choose_location_btn).grid(column=0, row=0)
        self.label = Label(win, text='')
        self.listbox = Listbox(win)
        self.listbox.grid(column=0, row=2)
        self.add_subtitle_btn = ttk.Button(win, text='Add Subtitle', command=self.add_subtitle)
        self.add_subtitle_btn.grid(column=0, row=3)

    def choose_location_btn(self):
        self.path, name = os.path.split(filedialog.askopenfile(title="Choose a media file").name)
        self.scrapper = SubSceneScrapper(name, is_filename=True)
        self.subtitles = self.scrapper.get_subtitles()
        for language in self.subtitles.keys():
            self.listbox.insert(1, language)

    def add_subtitle(self):
        language = self.listbox.get(ACTIVE)
        best_match = self.scrapper.get_best_match_subtitle(language)
        self.scrapper.download_subtitle_to_path(best_match, self.path + os.sep)


app = Application()
win.title('SubDown')
win.resizable(0, 0)
win.lift()
win.attributes('-topmost', True)
win.after_idle(win.attributes, '-topmost', False)
win.mainloop()
