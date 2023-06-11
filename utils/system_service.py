import subprocess
from config import active_icon, stopped_icon, active_color, stopped_color


class SystemService:
    def __init__(self,servic_name):
        # Define the symbols for the icons
        self.active_icon = active_icon
        self.stopped_icon = stopped_icon
        self.active_color = active_color
        self.stopped_color = stopped_color
        self.service_name = servic_name
        # Initialize the service statuses
        self.status = None
        self.icon = None
        self.color = None

    def check_status(self):
        proc_params = ["systemctl", "is-active", self.service_name]
        self.status = subprocess.run(proc_params, capture_output=True, text=True).stdout.strip()
        self.icon = self.active_icon if self.status == "active" else self.stopped_icon
        self.color = self.active_color if self.status == "active" else self.stopped_color
    def get_text(self):
        return self.icon + self.service_name
