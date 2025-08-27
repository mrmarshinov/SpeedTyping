import tkinter as tk

class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg="#7be5b2")
        self.controller = controller
        self.errors_var = tk.StringVar()
        self.errors_var.set(f"Count Errors: {self.controller.logic.current_count_errors}")

        self.title = tk.Label(
            self,
            text=controller.logic.current_line,
            font=("Arial", 20),
            bg="#7be5b2", fg="black"
        )
        self.title.place(relx=0.5, rely=0.6, anchor="center")

        self.error_counter = tk.Label(
            self,
            textvariable=self.errors_var,
            font=("Arial", 20),
            bg="#7be5b2", fg="black"
        )
        self.error_counter.place(relx=0.1, rely=0.9, anchor="center")

        self.start_button = tk.Button(
            self,
            text="Main menu",
            font=("Arial", 16),
            bg="#129757",
            command = lambda: controller.show_frame(list(controller.frames.keys())[0]))
        self.start_button.place(relx=0.9, rely=0.9, anchor="center")

        self.text = tk.Text(
            self,
            width=len(self.controller.logic.current_line),
            height=1,
            font=('Arial',18),
            bg="white",
            fg="black"
        )
        self.text.focus_set()
        self.text.place(relx=0.5, rely=0.7, anchor="center")
        self.text.bind("<KeyRelease>", self.on_key)


    def on_key(self,event):
        typed = self.text.get("1.0", "end-1c")
        self.text.tag_remove("wrong", "1.0", "end")
        errors = self.controller.logic.is_correct(typed)
        self.errors_var.set(f"Count Errors: {self.controller.logic.current_count_errors}")
        for start, end in errors:
            self.text.tag_add("wrong",f"1.{start}", f"1.{end}")
        self.text.tag_configure("wrong", background="#fb798d")

        if len(typed) >= len(self.controller.logic.current_line):
            self.text.delete("1.0","end")
            self.controller.logic.len_control(typed)
            self.title.config(text=self.controller.logic.current_line)
        else:
            self.controller.logic.len_control(typed)
            self.title.config(text=self.controller.logic.current_line)
