import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg="#7be5b2")
        self.controller = controller

        self.start_button = tk.Button(
            self,
            text="Main menu",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: controller.show_frame(list(controller.frames.keys())[0]))
        self.start_button.place(relx=0.5, rely=0.35, anchor="center")