import tkinter as tk
from tkscrollframe import ScrollFrame


root = tk.Tk()
root.geometry("400x300")
root['bg'] = 'red'

scrolled_frame = ScrollFrame(root, justify='right')

for i in range(10):
    # the widgets must be placed on scrolled_frame.viewPort
    tk.Button(scrolled_frame.viewPort, text=f"button {i}").pack(padx=8, pady=3)

scrolled_frame.pack(fill='both', expand=True)

root.mainloop()
