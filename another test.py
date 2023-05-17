import tkinter as tk
from PIL import Image, ImageTk
import time
import random
import pandas as pd

df = pd.DataFrame({'word': [], 'image_path': [], 'key': [], 'duration': []})

# Set up the stimulus
stimulus = pd.read_csv("stimulus.csv")

window = tk.Tk()
window.title("Stimulus")
window.geometry("800x600")
window.attributes("-topmost", True)
canvas = tk.Canvas(window, width=800, height=600, bg='black')
canvas.pack()

# Counter variable to keep track of iterations
count = 0

while count < 20:
    # Select a random row from the data set
    row = stimulus.sample()
    # Select a random word from the 'word' column
    word = row.iloc[0, 0]
    # select the value from the other rows randomly 
    value_col = random.choice([1, 2, 3])
    image_path = f"images/{row.iloc[0, value_col]}"
    # Create a blank window
    
    window = tk.Tk()
    window.title("Stimulus")
    window.geometry("800x600")
    window.attributes("-topmost", True)
    canvas = tk.Canvas(window, width=800, height=600, bg='black')
    canvas.pack()
    canvas.create_text(400, 300, text=word, fill='white', font=('Arial', 100), anchor=tk.CENTER)
    canvas.update()
    window.after(1000)
    canvas.delete("all")
    canvas.update()
    window.after(1000)
    # Load the image using PIL
    image = Image.open(image_path)

    # Convert the image to a PhotoImage object
    tk_image = ImageTk.PhotoImage(image)

    # Create an image item on the canvas using the PhotoImage object
    canvas.create_image(400, 300, image=tk_image)

    # Pack the canvas so it appears in the window
    canvas.pack()
    start_time = time.time()
    # Function to close the window when a key is pressed
    def key_press(event):
        global key, end_time
        key = event.char
        end_time = time.time()
        canvas.delete("all")
        canvas.update()


    # Bind the key press event to the function
    window.bind("<Key>", key_press)

    # Show the window
    window.mainloop()

    # Calculate the reaction time
    duration = end_time - start_time
    df.loc[len(df)] = [word, image_path, key, duration]

    # Increment the counter
    count += 1

# Print the data frame after 20 iterations
print(df)
y