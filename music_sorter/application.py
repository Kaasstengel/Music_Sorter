import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.test = tk.Button(self)
        self.test["text"] = "testy testy"
        self.test["command"] = self.console_warning
        self.test.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def console_warning(self):
        print("weeeooooweeeoooo")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
