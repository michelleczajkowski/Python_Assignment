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
window.geometry("800x600")
window.configure(bg="black")

# define a function that will be called when the user clicks the "Save" button
def save_data():
    global name, lang, gend
    name = name_field.get()
    lang = lang_field.get()
    gend = gend_field.get()
    window.destroy()  # close the window after the name and language have been saved

# create a label and text entry field for the user's name
name_label = tk.Label(window, text="Welcome to the dutch job names mini-experiment\nFirst we need some information.\nPlease enter:\nYour first name (first four letters):", fg="white", bg="black", font=("Arial", 16))
name_field = tk.Entry(window, font=("Arial", 16))

# create a label and text entry field for the language choice
lang_label = tk.Label(window, text="Mother Language (d for Dutch or e for English):", fg="white", bg="black", font=("Arial", 16))
lang_field = tk.Entry(window, font=("Arial", 16))

# create a label and text entry field for the gender choice
gend_label = tk.Label(window, text="Gender (m or f):", fg="white", bg="black", font=("Arial", 16))
gend_field = tk.Entry(window, font=("Arial", 16))

# create a button to save the user's name and language choice
save_button = tk.Button(window, text="Click to Continue", command=save_data, fg="white", bg="black", font=("Arial", 16))

# pack the name label, text entry field, language label, text entry field, gender label, text entry field, and save button into the window
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
window.geometry("800x600")
window.attributes("-topmost", True)
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
#window.after(2000)
keyboard.wait('enter')
canvas.delete("all")
canvas.update()
canvas.create_text(400, 300, text="Decide as fast as you can!\nReady?\nHit ENTER to continue", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
#window.after(2000)
keyboard.wait('enter')

# Set up the stimulus
stimulus = pd.read_csv("stimulus.csv")
# Create an empty DataFrame to store the results
results_df = pd.DataFrame(columns=['type', 'trial', 'word', 'value_col', 'key', 'duration'])

image_path2 = "images/crosshairs.jpg" 

for i in range(2):

    # Select a random row from the data set
    row = stimulus.sample()
    # Select a random word from the 'word' column
    word = row.iloc[0, 0]
    # select the value from the other rows randomly 
    value_col = random.choice([1, 2, 3])
    image_path = f"images/{row.iloc[0, value_col]}"

    canvas.delete("all")
    
    
    canvas.update()
    canvas.create_text(400, 300, text=word, fill='white', font=('Arial', 30), anchor=tk.CENTER)
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
    window.focus_force()
    # Show the window
    window.mainloop()


    # Calculate the duration
    duration = end_time - start_time
    # Append a row of data to the DataFrame
    results_df = pd.concat([results_df, pd.DataFrame({'type': "image", 'trial': i+1, 'word': word, 'value_col': value_col, 'key': key, 'duration': duration}, index=[0])])




canvas.delete("all")
canvas.create_text(400, 300, text="Mini-experiment\nRound 2 of 2", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
window.after(2000)
canvas.delete("all")
canvas.update()
canvas.create_text(400, 300, text="You will hear a speaker,\nand then see a word.\nDo they match? Press 'y'.\nIf not, press 'n'.\nHit ENTER to start.", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
keyboard.wait('enter')
#window.after(2000)
canvas.delete("all")

canvas.create_text(400, 300, text="Decide as fast as you can.\nReady?\nHit ENTER to start.", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
#window.after(2000)
keyboard.wait('enter')

# Set up the stimulus
stimulus2 = pd.read_csv("stimulus2.csv")


for i in range(2):

    # Select a random row from the data set
    row = stimulus2.sample()
    # Select a random word from the 'word' column
    word = row.iloc[0, 0]
    # select the value from the other rows randomly 
    value_col = random.choice([1, 2, 3])
    sound_path = f"sounds/{row.iloc[0, value_col]}"



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
    results_df = pd.concat([results_df, pd.DataFrame({'type': "sound", 'trial': i+1, 'word': word, 'value_col': value_col, 'key': key, 'duration': duration}, index=[0])])


# get the current date and time
now = datetime.now()
date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

# construct the file name using the name, lang, gend, and current date and time
file_name = f"{name}_{lang}_{gend}_{date_time}.csv"

# save the results to a CSV file with the constructed file name
results_df.to_csv(file_name, index=False)