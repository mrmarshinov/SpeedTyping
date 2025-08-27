import tkinter as tk

class SettingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg="#7be5b2")
        self.controller = controller
        level = [
            ("Easy","green"),
            ("Medium","yellow"),
            ("Hard","red")
            ]
        controller.window_index = 0
        window_sizes = [
            (0, "1280x720"),
            (1, "1366x768"),
            (2, "1440x900"),
            (3, "1600x900"),
            (4, "1920x1080")
        ]
        language = [
            (0, "English"),
            (1, "Čeština"),
            (2, "Русский")
            ]
        def choose_dif():
            controller.level =(controller.level + 1) % 3
            self.diff_button.config(background=level[controller.level][1],text= f"Difficulty is:{level[controller.level][0]}")

        def choose_size():
            controller.window_index = (controller.window_index + 1) % len(window_sizes)
            size = window_sizes[controller.window_index][1]
            self.size_button.config(text=f"Window size: {size}")
            controller.geometry(size)


        self.diff_button = tk.Button(
            self,
            text=f"Difficulty is:{level[controller.level][0]}",
            font=("Arial", 16),
            bg="green",
            command=choose_dif,
            width=20,
            height=2
        )
        self.diff_button.place(relx=0.5, rely=0.7, anchor="center")

        self.size_button = tk.Button(
            self,
            text=f"Window size: {window_sizes[controller.window_index][1]}",
            font=("Arial", 16),
            bg="#129757",
            command=choose_size,
            width=20,
            height=2
        )
        self.size_button.place(relx=0.5, rely=0.6, anchor="center")


        self.language = tk.Button(
            self,
            text="Back to Main menu",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: controller.show_frame(list(controller.frames.keys())[0]),
            width=20,
            height=2
        )
        self.start_button.place(relx=0.5, rely=0.8, anchor="center")


        self.start_button = tk.Button(
            self,
            text="Back to Main menu",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: controller.show_frame(list(controller.frames.keys())[0]),
            width=20,
            height=2
        )
        self.start_button.place(relx=0.5, rely=0.8, anchor="center")



