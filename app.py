import tkinter as tk
from tkinter import filedialog

global_file_path = ""  # Global variable to store the file path

def exit_app():
    window.destroy()

def search_path():
    global global_file_path  # Indicates that we will use the global variable
    global_file_path = filedialog.askopenfilename(initialdir="/", title="Select path")
    print(global_file_path)  # Just for demonstration, prints the path in the console
    # Here you can do what you need with the file path

window = tk.Tk()
window.title("TEST LCAI MODELS")
window.geometry("800x800")  # Sets the size of the window

button_exit = tk.Button(window, text="Exit", command=exit_app)
button_exit.place(x=750, y=750)  # Position of the button

button_search = tk.Button(window, text="Search", command=search_path)
button_search.place(x=50, y=50)  # Adjust the position as needed

window.mainloop()