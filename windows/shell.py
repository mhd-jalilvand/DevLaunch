import subprocess
import tkinter as tk
from tkinter import scrolledtext, Label, Entry, Button

class Shell:
    def __init__(self, commands, use_sudo=False):
        self.commands = commands if isinstance(commands, list) else [commands]
        self.use_sudo = use_sudo

        # Create the shell window
        self.shell_window = tk.Toplevel()
        self.shell_window.title("Shell Output")

        # Create the output text widget
        self.output_text = scrolledtext.ScrolledText(self.shell_window, width=80, height=20)
        self.output_text.pack()

        # Create the password label and entry if sudo is enabled
        self.password_label = None
        self.password_entry = None
        if self.use_sudo:
            self.password_label = Label(self.shell_window, text="Password:")
            self.password_label.pack()
            self.password_entry = Entry(self.shell_window, show="*")
            self.password_entry.pack()

        # Create the run button
        self.run_button = Button(self.shell_window, text="Run", command=self.run_command)
        self.run_button.pack()

    def run_command(self):
        self.run_button.configure(state=tk.DISABLED)
        # Get the password if sudo is enabled
        password = self.password_entry.get() if self.use_sudo else None

        # Execute each command in the list
        for i, command in enumerate(self.commands):
            is_last_item = (i == len(self.commands) - 1)
            self.output_text.insert(tk.END, "#" if self.use_sudo else "$" + command + "\n")

            # Prepare the command with sudo if needed
            if self.use_sudo and password:
                command = f"echo {password} | sudo -S {command}"

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True
            )
            # Read the output in real-time and display it in the text widget
            while True:
                output = process.stdout.readline().decode('utf-8')
                if output == '' and process.poll() is not None:
                    break
                self.output_text.insert(tk.END, output)
                self.output_text.see(tk.END)
                self.output_text.update_idletasks()

            # Wait for the process to finish and retrieve the return code
            return_code = process.wait()

            # Display the exit status in the text widget
            if(return_code !=0 or is_last_item):
                self.output_text.insert(tk.END, f"\n\nCommand exited with status {return_code}\n\n")
                self.output_text.see(tk.END)
            if(return_code != 0):
                break

        # Disable text widget editing
        self.output_text.configure(state=tk.DISABLED)
