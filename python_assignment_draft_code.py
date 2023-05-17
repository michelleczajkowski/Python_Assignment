import tkinter as tk
from PIL import Image, ImageTk
import time
import random
import keyboard
import pandas as pd
import time
import keyboard 
import os
from playsound import playsound

# Create a blank window
window = tk.Tk()
window.title("Stimulus")
window.geometry("800x600")
window.attributes("-topmost", True)
canvas = tk.Canvas(window, width=800, height=600, bg='black')
canvas.pack()
canvas.create_text(400, 300, text="Picture = Word? click Y or N", fill='white', width=600, font=('Arial', 20), anchor=tk.CENTER)
canvas.update()
window.after(2000)
canvas.delete("all")
canvas.create_text(400, 300, text="Click as fast as you can! Ready?", fill='white', width=600, font=('Arial', 20), anchor=tk.CENTER)
canvas.update()
window.after(2000)


# Set up the stimulus
stimulus = pd.read_csv("stimulus.csv")
# Create an empty DataFrame to store the results
results_df = pd.DataFrame(columns=['type', 'trial', 'word', 'value_col', 'key', 'duration'])

image_path2 = "images/crosshairs.jpg" 

for i in range(5):

    # Select a random row from the data set
    row = stimulus.sample()
    # Select a random word from the 'word' column
    word = row.iloc[0, 0]
    # select the value from the other rows randomly 
    value_col = random.choice([1, 2, 3])
    image_path = f"images/{row.iloc[0, value_col]}"



    canvas.delete("all")
    canvas.update()
    canvas.create_text(400, 300, text=word, fill='white', font=('Arial', 50), anchor=tk.CENTER)
    canvas.update()
    window.after(1000)
    canvas.delete("all")
    canvas.update()
    
    # Load the image using PIL
    image = Image.open(image_path2)
    # Convert the image to a PhotoImage object
    tk_image = ImageTk.PhotoImage(image)
    # Create an image item on the canvas using the PhotoImage object
    canvas.create_image(400, 300, image=tk_image)
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
        window.quit()

    # Bind the key press event to the function
    window.bind("<Key>", key_press)

    # Show the window
    window.mainloop()



    # Calculate the duration
    duration = end_time - start_time
    # Append a row of data to the DataFrame
    results_df = pd.concat([results_df, pd.DataFrame({'type': "image", 'trial': i+1, 'word': word, 'value_col': value_col, 'key': key, 'duration': duration}, index=[0])])




canvas.delete("all")
canvas.create_text(400, 300, text="Round 2 - last round", fill='white', width=600, font=('Arial', 20), anchor=tk.CENTER)
canvas.update()
window.after(2000)
canvas.delete("all")
canvas.update()
canvas.create_text(400, 300, text="Picture = Audio? click Y or N", fill='white', width=600, font=('Arial', 20), anchor=tk.CENTER)
canvas.update()
window.after(2000)
canvas.delete("all")
canvas.create_text(400, 300, text="Click as fast as you can! Ready?", fill='white', width=600, font=('Arial', 20), anchor=tk.CENTER)
canvas.update()
window.after(2000)


# Set up the stimulus
stimulus2 = pd.read_csv("stimulus2.csv")
# Create an empty DataFrame to store the results
results_df = pd.DataFrame(columns=['type', 'trial', 'word', 'value_col', 'key', 'duration'])

image_path2 = "images/crosshairs.jpg" 

for i in range(5):

    # Select a random row from the data set
    row = stimulus2.sample()
    # Select a random word from the 'word' column
    word = row.iloc[0, 0]
    # select the value from the other rows randomly 
    value_col = random.choice([1, 2, 3])
    sound_path = f"sounds/{row.iloc[0, value_col]}"



    canvas.delete("all")
    canvas.update()
    canvas.create_text(400, 300, text=word, fill='white', font=('Arial', 50), anchor=tk.CENTER)
    canvas.update()
    window.after(1000)
    canvas.delete("all")
    canvas.update()
    
    # Load the image using PIL
    image = Image.open(image_path2)
    # Convert the image to a PhotoImage object
    tk_image = ImageTk.PhotoImage(image)
    # Create an image item on the canvas using the PhotoImage object
    canvas.create_image(400, 300, image=tk_image)
    canvas.update()
    window.after(1000)
    canvas.delete("all")
    canvas.update()
    
    start_time = time.time() 
    
    playsound(sound_path)


    
    # Function to close the window when a key is pressed
    def key_press(event):
        global key, end_time
        key = event.char
        end_time = time.time()
        window.quit()

    # Bind the key press event to the function
    window.bind("<Key>", key_press)

    # Show the window
    window.mainloop()



    # Calculate the duration
    duration = end_time - start_time
    # Append a row of data to the DataFrame
    results_df = pd.concat([results_df, pd.DataFrame({'type': "sound", 'trial': i+1, 'word': word, 'value_col': value_col, 'key': key, 'duration': duration}, index=[0])])

# Print the DataFrame
print(results_df)