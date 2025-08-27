import tkinter as tk

from Pages import *
from logic import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.windows_index = 0
        self.windows_size = "1280x720"
        self['bg'] = "#7be5b2"
        self.title("SpeedTyping")
        self.geometry(self.windows_size)
        self.resizable(width=False, height=False)
        self.level = 0
        self.language = 0
        container = tk.Frame(self,bg="#7be5b2")
        container.pack(fill="both",expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.logic = GameLogic()

        for F in (MainPage, LoginPage, GamePage, SettingPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(SettingPage)

    def show_frame(self,page_class):
        frame = self.frames[page_class]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()