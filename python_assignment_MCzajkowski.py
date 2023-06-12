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
from datetime import datetime

# create a new window
window = tk.Tk()

# set the size and background color of the window
window.attributes("-fullscreen", True)
window.configure(bg='black')
window.configure(bg="black")

# when the user clicks the "Save" button
def save_data():
    global name, lang, gend
    name = name_field.get()
    lang = lang_field.get()
    gend = gend_field.get()
    window.destroy()  

# user's name
name_label = tk.Label(window, text="Welcome to the Dutch job names mini-experiment\nFirst we need some information.\nPlease enter:\nYour first name (first four letters):", fg="white", bg="black", font=("Arial", 16))
name_field = tk.Entry(window, font=("Arial", 16))

# language choice
lang_label = tk.Label(window, text="Mother Language (d for Dutch or e for English):", fg="white", bg="black", font=("Arial", 16))
lang_field = tk.Entry(window, font=("Arial", 16))

# gender choice
gend_label = tk.Label(window, text="Gender (m or f or nb):", fg="white", bg="black", font=("Arial", 16))
gend_field = tk.Entry(window, font=("Arial", 16))

# create a button to save 
save_button = tk.Button(window, text="Click to Continue", command=save_data, fg="white", bg="black", font=("Arial", 16))

# pack 
name_label.pack()
name_field.pack()
lang_label.pack()
lang_field.pack()
gend_label.pack()
gend_field.pack()
save_button.pack()

# start the event loop
window.mainloop()

# Create a blank window
window = tk.Tk()
window.title("Stimulus")
window.attributes("-fullscreen", True)
window.configure(bg='black')
window.grab_set()

canvas = tk.Canvas(window, width=800, height=600, bg='black')
canvas.pack()

window.focus_force()
canvas.create_text(400, 300, text="Mini-Experiment\nRound 1 of 2", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
window.after(2000)
canvas.delete("all")
canvas.update()
canvas.create_text(400, 300, text="You will see a word.\nThen you will see a picture.\nDo they match? press 'y'\nIf not, press 'n'.\nHit ENTER to continue", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
keyboard.wait('enter')
canvas.delete("all")
canvas.update()
canvas.create_text(400, 300, text="Decide as fast as you can!\nReady?\nHit ENTER to continue", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
keyboard.wait('enter')

# Set up 
stimulus = pd.read_csv("stimulus.csv")
# Create an empty DataFrame
results_df = pd.DataFrame(columns=['type', 'trial', 'word', 'value_col', 'key', 'gendered', 'rightornot', 'duration'])

image_path2 = "images/crosshairs.jpg" 

for i in range(20):

    # Select a random row 
    row = stimulus.sample()
    # Select a random word 
    word = row.iloc[0, 0]
    # select the value from the other rows randomly 
    value_col = random.choice([1, 2, 3])
    image_path = f"images/{row.iloc[0, value_col]}"

    # for later when storing results
    gendered = row.iloc[0,4]
    if gendered == 'y':
        gendered = 1
    if gendered == 'n':
        gendered = 0

    canvas.delete("all")
    canvas.update()
    canvas.create_text(400, 300, text=word, fill='white', font=('Arial', 30), anchor=tk.CENTER)
    canvas.update()
    window.after(1000)
    canvas.delete("all")
    canvas.update()
    
    # Load the image 
    image = Image.open(image_path2)
    tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(400, 300, image=tk_image)
    canvas.update()
    window.after(1000)

    # Load the image 
    image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(400, 300, image=tk_image)
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
    window.focus_force()

    window.mainloop()

    # Calculate the duration
    duration = end_time - start_time
   
    # Append a row of data to the DataFrame
    results_df = pd.concat([results_df, pd.DataFrame({'type': "image", 'trial': i+1, 'word': word, 'value_col': value_col, 'key': key, 'gendered': gendered, 'duration': duration}, index=[0])])

# start of new loop for audio trials
canvas.delete("all")
canvas.create_text(400, 300, text="Mini-experiment\nRound 2 of 2", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
window.after(2000)
canvas.delete("all")
canvas.update()
canvas.create_text(400, 300, text="You will hear a speaker,\nand then see a word.\nDo they match? Press 'y'.\nIf not, press 'n'.\nHit ENTER to start.", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
keyboard.wait('enter')
canvas.delete("all")
canvas.create_text(400, 300, text="Decide as fast as you can.\nReady?\nHit ENTER to start.", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
keyboard.wait('enter')

# Set up 
stimulus2 = pd.read_csv("stimulus2.csv")


for i in range(20):

    # Select a random row 
    row = stimulus2.sample()
    # Select a random word 
    word = row.iloc[0, 0]
    # select the value from the other rows randomly 
    value_col = random.choice([1, 2, 3])
    sound_path = f"sounds/{row.iloc[0, value_col]}"

    # for later when recording results
    gendered = row.iloc[0,4]
    if gendered == 'y':
        gendered = 1
    if gendered == 'n':
        gendered = 0

    canvas.delete("all")
    canvas.update()
    playsound(sound_path, block=True)
    window.after(2000)
    canvas.create_text(400, 300, text=word, fill='white', font=('Arial', 50), anchor=tk.CENTER)
    canvas.update()
 
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
    results_df = pd.concat([results_df, pd.DataFrame({'type': "sound", 'trial': i+1, 'word': word, 'value_col': value_col, 'key': key, 'gendered': gendered, 'duration': duration}, index=[0])])

# get the current date and time
now = datetime.now()
date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

# construct the file name using the name, lang, gend, and current date and time
file_name = f"{date_time}_{lang}_{gend}_{name}.csv"

# save the results to a CSV file with the constructed file name
results_df.to_csv(file_name, index=False)
canvas.delete("all")
canvas.create_text(400, 300, text="Thank you for participating!\nYour results have been saved.\nHave a great day :D", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
window.after(2000)
