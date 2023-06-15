import tkinter as tk
from tkinter import ttk
from windows.shell import Shell
class Wordpress:
    def __init__(self, root):
        self.root = root
        self.treeview = None
        self.install_button = None
        self.update_button = None

    def create_overlay_window(self):
        self.overlay = tk.Toplevel(self.root)
        self.overlay.title("WordPress")
        self.overlay.geometry("600x400")

        self.install_button = ttk.Button(self.overlay, text='Install Selected', command=self.install_selected)
        self.install_button.pack()
    def install_selected(self):
        Shell(["whoami","whoami"])
