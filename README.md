# tkscrollframe
tkinter frame widget with auto scroll.

## How to install
`pip install tkscrollframe`


## How to use
```
import tkinter as tk
from tkscrollframe import ScrollFrame

root = tk.Tk()
sf = ScrollFrame(root)

frame = sf.viewPort # is important

# add some widget to frame sf
for i in range(20):
    tk.Label(frame, text=f"text in line {i}").pack() 

sf.pack()
root.mainloop()
```

## options
if you need scrollbar placed to right `sf= ScrollFrame(root, justify='right')`
