import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#7be5b2")
        self.controller = controller

        self.title = tk.Label(
            self,
            text='Welcome to SpeedTyping app!',
            font=("Arial", 20),
            bg ="#7be5b2", fg="black"
        )
        self.title.place(relx =0.5, rely=0.025, anchor="center")

        self.start_button = tk.Button(
            self,
            text="Start typing game",
            font=("Arial", 16),
            bg= "#129757",
            command=lambda: controller.show_frame(list(controller.frames.keys())[2]),
            width=20,
            height=2
        )
        self.start_button.place(relx =0.5, rely=0.35, anchor="center")

        self.start_button = tk.Button(
            self,
            text="Settings",
            font=("Arial", 16),
            bg= "#129757",
            command=lambda: controller.show_frame(list(controller.frames.keys())[3]),
            width=20,
            height=2
        )
        self.start_button.place(relx =0.5, rely=0.45, anchor="center")
