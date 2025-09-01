import tkinter as tk
import time

class GameLogic:
    def __init__(self,controller):
        self.controller = controller
        self.sum_errors = 0
        self.current_count_errors = 0
        self.line_index = 0
        self.text_path = f"Levels/{self.controller.language.get().lower()}_{1}.txt"
        self.image_path =f"Images/{self.controller.language.get().lower()}_keyboard.jpg"
        self.current_line_var = tk.StringVar(value=self.read_line(self.line_index))
        self.len_text = tk.IntVar(value=0)

    def len_control(self, typed, line=None):
        if line is None:
            line = self.current_line_var.get()

        if len(typed) >= len(line):
            self.sum_errors = self.current_count_errors
            self.current_count_errors = 0
            self.line_index += 1
            self.current_line_var.set(self.read_line(self.line_index))

    def is_correct(self, typed, line=None):
        errors = []
        self.current_count_errors = 0
        if line is None:
            line = self.current_line_var.get()
        for i, char in enumerate(typed):
            if i < len(line) and char != line[i]:
                errors.append((i,i+1))
        self.current_count_errors = self.sum_errors + len(errors)
        return errors

    def read_line(self, index):
        with open(self.text_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i == index:
                    return line.strip()
        return self.controller.show_frame(list(self.controller.frames.keys())[2])

    def refresh(self,level):
        self.sum_errors = 0
        self.current_count_errors = 0
        self.line_index = 0
        self.text_path = f"Levels/{self.controller.language.get().lower()}_{level}.txt"
        self.current_line_var.set(self.read_line(self.line_index))

    def timer(self,start):
        end = time.time()
        return start-end