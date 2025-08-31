import tkinter as tk

from Pages import *
from logic import GameLogic
from settings import load_settings

settings = load_settings()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.windows_size = settings["windows_size"]
        self.difficulty = settings["difficulty"]
        self.language = settings["language"]
        self.configure(bg="#7be5b2")
        self.title("SpeedTyping")
        self.geometry(self.windows_size)
        self.resizable(width=False, height=False)

        container = tk.Frame(self,bg="#7be5b2")
        container.pack(fill="both",expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.logic = GameLogic(self)

        for F in (MainPage, LevelPage, GamePage, SettingPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(MainPage)

    def show_frame(self,page_class):
        frame = self.frames[page_class]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
