import tkinter as tk

class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg="#7be5b2")
        self.controller = controller

        self.title = tk.Label(
            self,
            text='Choose level !',
            font=("Arial", 20),
            bg ="#7be5b2", fg="black"
        )
        self.title.place(relx =0.5, rely=0.03, anchor="center")

        self.level_1_button = tk.Button(
            self,
            text="level 1",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: self.choose_lvl(1),
            width=7,
            height=2
        )
        self.level_1_button.place(relx=0.3, rely=0.5, anchor="center")

        self.level_2_button = tk.Button(
            self,
            text="level 2",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: self.choose_lvl(2),
            width=7,
            height=2
        )
        self.level_2_button.place(relx=0.4, rely=0.5, anchor="center")

        self.level_3_button = tk.Button(
            self,
            text="level 3",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: self.choose_lvl(3),
            width=7,
            height=2
        )
        self.level_3_button.place(relx=0.5, rely=0.5, anchor="center")

        self.level_4_button = tk.Button(
            self,
            text="level 4",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: self.choose_lvl(4),
            width=7,
            height=2
        )
        self.level_4_button.place(relx=0.6, rely=0.5, anchor="center")

        self.level_5_button = tk.Button(
            self,
            text="level 5",
            font=("Arial", 16),
            bg="#129757",
            command = lambda : self.choose_lvl(5),
            width=7,
            height=2
        )
        self.level_5_button.place(relx=0.7, rely=0.5, anchor="center")

        self.level_6_button = tk.Button(
            self,
            text="level 6",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: self.choose_lvl(6),
            width=7,
            height=2
        )
        self.level_6_button.place(relx=0.3, rely=0.6, anchor="center")

        self.level_7_button = tk.Button(
            self,
            text="level 7",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: self.choose_lvl(7),
            width=7,
            height=2
        )
        self.level_7_button.place(relx=0.4, rely=0.6, anchor="center")

        self.level_8_button = tk.Button(
            self,
            text="level 8",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: self.choose_lvl(8),
            width=7,
            height=2
        )
        self.level_8_button.place(relx=0.5, rely=0.6, anchor="center")

        self.level_9_button = tk.Button(
            self,
            text="level 9",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: self.choose_lvl(9),
            width=7,
            height=2
        )
        self.level_9_button.place(relx=0.6, rely=0.6, anchor="center")

        self.level_10_button = tk.Button(
            self,
            text="level 10",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: self.choose_lvl(10),
            width=7,
            height=2
        )
        self.level_10_button.place(relx=0.7, rely=0.6, anchor="center")

        self.start_button = tk.Button(
            self,
            text="Main menu",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: controller.show_frame(list(controller.frames.keys())[0]))
        self.start_button.place(relx=0.9, rely=0.9, anchor="center")

    def choose_lvl(self,lvl):
        self.controller.logic.refresh(lvl),
        self.controller.show_frame(list(self.controller.frames.keys())[1])