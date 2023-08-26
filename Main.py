import tkinter as tk
from AlgoritmoFlooding import *
from tkinter import simpledialog, messagebox


class AlgorithmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithms App")
        self.root.geometry("400x300")

        # Styling
        btn_style = {
            "padx": 20,
            "pady": 10,
            "bg": "#6200EE",
            "fg": "white",
            "borderwidth": 0,
            "activebackground": "#3700B3",
            "activeforeground": "white",
        }

        # Create buttons for the algorithms
        self.flooding_button = tk.Button(
            root, text="🌊 Flooding", command=self.start_flooding, **btn_style
        )
        self.flooding_button.pack(pady=20)

        self.algo2_button = tk.Button(
            root, text="🔒 Algorithm #2", command=self.start_algo2, **btn_style
        )
        self.algo2_button.pack(pady=20)

        self.algo3_button = tk.Button(
            root, text="🔍 Algorithm #3", command=self.start_algo3, **btn_style
        )
        self.algo3_button.pack(pady=20)

    def start_flooding(self):
        new_window = tk.Toplevel(self.root)
        FloodingApp(new_window)

    def start_algo2(self):
        # Placeholder for Algorithm #2
        messagebox.showinfo("Info", "🔒 Algorithm #2 not implemented yet!")

    def start_algo3(self):
        # Placeholder for Algorithm #3
        messagebox.showinfo("Info", "🔍 Algorithm #3 not implemented yet!")


# Running the Tkinter App
def run_main_app():
    root = tk.Tk()
    app = AlgorithmApp(root)
    root.mainloop()


run_main_app()
