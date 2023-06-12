import subprocess
import tkinter as tk
from tkinter import scrolledtext, Label, Entry, Button
from windows.shell import Shell
class Software:
    def __init__(self, title, install_command, version_command, update_command):
        self.title = title
        self.install_command = install_command
        self.version_command = version_command
        self.update_command = update_command

    def is_installed(self):
        try:
            subprocess.check_output(self.version_command, shell=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def get_version(self):
        try:
            output = subprocess.check_output(self.version_command, shell=True, encoding='utf-8')
            version = output.strip()
            return version
        except subprocess.CalledProcessError:
            return 'N/A'

    def install(self):
        Shell(self.install_command, True)

    def update(self):
        Shell(self.install_command, True)
