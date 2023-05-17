import tkinter as tk
from PIL import Image, ImageTk
import time
import random

# Create a blank window
window = tk.Tk()
window.title("Random letters")
window.geometry("400x300")
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

# Set up the alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#LOOP
for i in range(5):
    # Select a random letter from the alphabet
    letter1 = random.choice(alphabet)

    # Display the letter on the canvas
    canvas.delete("all")
    canvas.create_text(200, 150, text=letter1, font=('Arial', 50), anchor=tk.CENTER)
    canvas.update()

    # Wait for 1 second
    time.sleep(1)

    # Wait for the user to press the same key that is displayed on the canvas
    def on_key_press(event):
        if event.char.upper() == letter1:
            window.quit()  # Exit the event loop
    window.bind("<Key>", on_key_press)
    window.mainloop()

    # Select another random letter from the alphabet
    letter2 = random.choice(alphabet)

    # Display the second letter on the canvas
    canvas.delete("all")
    canvas.create_text(200, 150, text=letter2, font=('Arial', 50), anchor=tk.CENTER)
    canvas.update()

    # Wait for 1 second
    time.sleep(1)

# Start the event loop of the window
window.mainloop()
