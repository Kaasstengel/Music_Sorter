import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        self.menubar = tk.Menu(root)
        root.config(menu=self.menubar)

        self.subMenu = tk.Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Open", command=self.browse_file)
        self.subMenu.add_command(label="Exit", command=root.destroy)

    def create_widgets(self):
        self.browse_file_click = tk.Button()
        self.browse_file_click["text"] = "Click me to browse files!"
        self.browse_file_click.pack(side="top")
        self.browse_file_click["command"] = self.browse_file

    def browse_file(self):
        global filenames
        filenames = filedialog.askopenfilenames(parent=root, title='choose a file')
        print(root.tk.splitlist(filenames))


root = tk.Tk()
app = Application(master=root)

statusbar = ttk.Label(root, text="Please choose the files you want sorted")
statusbar.pack(side="bottom", fill="x")



app.mainloop()
