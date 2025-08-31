import tkinter


class GameLogic:
    def __init__(self,controller):
        self.controller = controller
        self.sum_errors = 0
        self.current_count_errors = 0
        self.line_index = 0
        self.file_path = f"Levels/{self.controller.language.lower()}_{1}.txt"
        self.current_line_var = tkinter.StringVar(value=self.read_line(self.line_index))

    def len_control(self, typed, line=None):
        if line is None:
            line = self.current_line_var.get()

        if len(typed) >= len(line):
            self.sum_errors += self.current_count_errors
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
        with open(self.file_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i == index:
                    return line.strip()
        return ""

    def refresh(self,level):
        self.sum_errors = 0
        self.current_count_errors = 0
        self.line_index = 0
        self.file_path = f"Levels/{self.controller.language.lower()}_{level}.txt"
        self.current_line_var.set(self.read_line(self.line_index))