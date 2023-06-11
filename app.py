import tkinter as tk
from utils.window_utils import set_window_size
from windows.main import MainWindow

# Create the main window
root = tk.Tk()

# Set the window size
set_window_size(root)

# Create an instance of the MainWindow
main_window = MainWindow(root)

# Run the main event loop
root.mainloop()
