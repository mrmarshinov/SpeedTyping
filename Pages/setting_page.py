import tkinter as tk

from main import settings
from settings import save_settings,load_settings

class SettingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg="#7be5b2")
        self.controller = controller
        self.settings = settings.copy()
        self.language_var = tk.StringVar(value=f"Language: {self.settings['language']}")
        self.diff_var = tk.StringVar(value=f"Difficulty: {self.settings['difficulty']}")
        self.windows_var = tk.StringVar(value=f"Windows size: {self.settings['windows_size']}")

        controller.window_index = 0
        WINDOWS_OPTION = ["1280x720", "1366x768","1440x900","1600x900","1920x1080"]
        LANGUAGE_OPTION = ["English","Russian","Czech"]
        DIFFICULTY_OPTION =["Easy","Medium","Hard"]

        self.language_button = tk.Button(
            self,
            textvariable=self.language_var,
            font=("Arial", 16),
            bg="#129757",
            command = lambda:self.choose_option("language",LANGUAGE_OPTION, self.language_var,"Language:"),
            width=20,
            height=2,

        )
        self.language_button.place(relx=0.5, rely=0.4, anchor="center")

        self.diff_button = tk.Button(
            self,
            textvariable=self.diff_var,
            font=("Arial", 16),
            bg="#129757",
            command=lambda:self.choose_option("difficulty",DIFFICULTY_OPTION,self.diff_var,"Difficulty: "),
            width=20,
            height=2
        )
        self.diff_button.place(relx=0.5, rely=0.5, anchor="center")

        self.size_button = tk.Button(
            self,
            textvariable=self.windows_var,
            font=("Arial", 16),
            bg="#129757",
            command=lambda:self.choose_option("windows_size",WINDOWS_OPTION, self.windows_var,"Windows size: "),
            width=20,
            height=2
        )
        self.size_button.place(relx=0.5, rely=0.6, anchor="center")

        self.save_button = tk.Button(
            self,
            text="Save",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: (save_settings(self.settings),
                               controller.geometry(self.settings["windows_size"]),
                               self.controller.language.set(self.settings["language"]),
                               setattr(controller.logic, "image_path",f"images/{self.controller.language.get().lower()}_keyboard.jpg")
                               ),
            width=20,
            height=2
        )
        self.save_button.place(relx=0.5, rely=0.7, anchor="center")

        self.start_button = tk.Button(
            self,
            text="Back to Main menu",
            font=("Arial", 16),
            bg="#129757",
            command = self.back_to_main,
            width=20,
            height=2
        )
        self.start_button.place(relx=0.5, rely=0.8, anchor="center")


    def choose_option(self, setting_name: str, option: list,var_text: tk.StringVar, label: str):
        current_value = self.settings[setting_name]
        index = option.index(current_value)
        index =(index +1) % len(option)
        self.settings[setting_name] = option[index]
        var_text.set(label + self.settings[setting_name])

    def back_to_main(self):
        self.settings = load_settings()
        self.controller.show_frame(list(self.controller.frames.keys())[0])
        self.language_var.set(value=f"Language: {self.settings['language']}")
        self.diff_var.set(value=f"Difficulty: {self.settings['difficulty']}")
        self.windows_var.set(value=f"Windows size: {self.settings['windows_size']}")