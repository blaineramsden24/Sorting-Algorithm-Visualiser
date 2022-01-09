import tkinter as tk
from tkinter import ttk
import random
from colours import *

# This Creates the main window
root = tk.Tk()
root.title("Sorting Algorithm Visualiser")
root.maxsize(1000, 700)
root.config(bg=BLACK)

# Algorithm Selector
algo_name = tk.StringVar()
algo_list = ['Bubble Sort', 'Merge Sort']

# The array of data to be sorted
array = []


# This will draw the array onto the canvas
def drawArray(array, colourArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(array) + 1)
    offset = 4
    spacing = 2
    normalised_data = [i / max(array) for i in array]

    for i, height in enumerate(normalised_data):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colourArray[i])

    root.update_idletasks()


# This will generate the random array
def generateArray():
    global array

    array = []
    for i in range(0, 100):
        random_value = random.randint(1, 100)
        array.append(random_value)

    drawArray(array, [WHITE for x in range(len(array))])


# This will sort the array using the selected sorting algorithm
def sort():
    print("Sorting")


# User interface
frame = tk.Frame(root, width=900, height=300, bg=BLACK)
frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown for selecting algorithm
label1 = tk.Label(frame, text="Algorithm: ", fg=WHITE, bg=BLACK)
label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
algo_drop = tk.ttk.Combobox(frame, textvariable=algo_name, values=algo_list)
algo_drop.grid(row=0, column=1, padx=5, pady=5)
algo_drop.current(0)

# button to run sorting
button1 = tk.Button(frame, text="Sort", command=sort, bg=LIGHT_GRAY)
button1.grid(row=2, column=1, padx=5, pady=5)

# button to generate array
button2 = tk.Button(frame, text="Generate Array", command=generateArray, bg=LIGHT_GRAY)
button2.grid(row=2, column=0, padx=5, pady=5)

canvas = tk.Canvas(root, width=800, height=400, bg=BLACK)
canvas.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
