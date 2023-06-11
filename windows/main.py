import tkinter as tk
import sys
import os

# Add the project root directory to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from utils.system_service import SystemService

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        
        # Create the status bar
        self.status_bar = tk.Label(self.root, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        # Create individual labels for each service status
        self.system_services = {
            "nginx": {"label":tk.Label(self.status_bar, width=10), "service":SystemService("nginx")},
            "apache": {"label":tk.Label(self.status_bar, width=10), "service":SystemService("apache2")},
            "mysql": {"label":tk.Label(self.status_bar, width=10), "service":SystemService("mysql")}
        }

        # Pack the labels in the status bar
        for obj in self.system_services.values():
            obj["label"].pack(side=tk.LEFT)

        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.update_status()
        
        self.root.mainloop()
        
    def update_status(self):
        for obj in self.system_services.values():
            obj["service"].check_status()
            obj["label"].config(text= obj["service"].get_text(), fg=obj["service"].color)
        # Schedule the next update after a certain interval (in milliseconds)
        self.root.after(5000, self.update_status)
