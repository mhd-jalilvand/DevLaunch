import tkinter as tk
from tkinter import ttk
from utils.software import Software
from config import software_list
class Softwares:
    def __init__(self, root):
        self.root = root
        self.software_list =software_list
        self.treeview = None
        self.install_button = None
        self.update_button = None

    def create_overlay_window(self):
        overlay = tk.Toplevel(self.root)
        overlay.title("Software Status")
        overlay.geometry("600x400")

        self.treeview = ttk.Treeview(overlay, columns=('Checkbox', 'Title', 'Status', 'Version'), show='headings')
        self.treeview.heading('Checkbox', text='')
        self.treeview.heading('Title', text='Title')
        self.treeview.heading('Status', text='Status')
        self.treeview.heading('Version', text='Version')

        self.populate_treeview()
        self.treeview.pack(fill='both', expand=True)  # Maximize the treeview
        self.treeview.pack()

        self.install_button = ttk.Button(overlay, text='Install Selected', state='disabled', command=self.install_selected)
        self.install_button.pack()

        self.update_button = ttk.Button(overlay, text='Update Selected', state='disabled', command=self.update_selected)
        self.update_button.pack()

        self.treeview.bind('<<TreeviewSelect>>', self.on_checkbox_select)

    def populate_treeview(self):
        for software in self.software_list:
            installed = software.is_installed()
            version = software.get_version()

            status_text = 'Installed' if installed else 'Not Installed'

            # Insert a row into the treeview
            self.treeview.insert("", "end", values=('', software.title, status_text, version))

            # Set the icon based on the installed status
            icon = '✔️' if installed else '❌'
            self.treeview.set(self.treeview.get_children()[-1], 'Checkbox', icon)

    def get_selected_items(self):
        selected_items = []
        for item in self.treeview.selection():
            values = self.treeview.item(item, 'values')
            title = values[1]
            selected_items.append(title)
        return selected_items

    def update_selected(self):
        selected_items = self.get_selected_items()
        for software in self.software_list:
            if software.title in selected_items:
                software.update()
                version = software.get_version()
                item = self.get_item_by_title(software.title)
                self.treeview.set(item, 'Version', version)

    def install_selected(self):
        selected_items = self.get_selected_items()
        for software in self.software_list:
            if software.title in selected_items:
                software.install()
                item = self.get_item_by_title(software.title)
                self.treeview.set(item, 'Status', 'Installed')
                self.treeview.set(item, 'Checkbox', '✔️')

    def on_checkbox_select(self, event):
        selected_items = self.get_selected_items()

        if selected_items:
            self.install_button['state'] = 'normal'
            self.update_button['state'] = 'normal'
        else:
            self.install_button['state'] = 'disabled'
            self.update_button['state'] = 'disabled'

    def get_item_by_title(self, title):
        for item in self.treeview.get_children():
            if self.treeview.item(item, 'values')[1] == title:
                return item


