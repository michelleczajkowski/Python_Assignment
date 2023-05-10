import pandas as pd
import random
import tkinter as tk
from PIL import ImageTk, Image
import time
import keyboard 

########## GET THE WORD AND PICS FROM THE STIMULUS SET

# Read the CSV file into a dataframe
stimulus = pd.read_csv('stimulus.csv')

# Select a random word from the 'word' column
word = random.choice(stimulus['word'].tolist())
image_name = stimulus.loc[stimulus['word'] == word, 'correct'].iloc[0]
image_path = f"images/{image_name}"  # assuming images are in the 'images' subdirectory
print(word)
print(image_name)
print(image_path)

##########

print("Press 'g' key to start timer")

# wait for 'g' key press
keyboard.wait('g')
print("g pressed. press 's' to stop")
start_time = time.time() * 1000  # convert to milliseconds

# wait for 's' key press to stop the timer
keyboard.wait('s')

end_time = time.time() * 1000  # convert to milliseconds
duration = end_time - start_time

print(f"Elapsed time: {duration:.2f} milliseconds")
