import tkinter as tk
import time

# Create a window
window = tk.Tk()
window.geometry("800x800")

# Load the image
image = tk.PhotoImage(file="kapper_man.jpg")

# Define a function to show the hello message and the image
def show_hello_and_image():
    # Create a label with the hello message
    hello_label = tk.Label(window, text="Hello", font=("Arial", 24))
    hello_label.pack()
    
    # Wait for 1 second
    window.after(1000)
    
    # Remove the hello label and create a label with the image
    hello_label.destroy()
    image_label = tk.Label(window, image=image)
    image_label.pack()
    
    # Wait for 1 second
    window.after(1000)
    
    # Remove the image label
    image_label.destroy()

# Define a function to show a blank screen and wait for the user's response
def show_blank_screen():
    # Create a label with a blank message
    blank_label = tk.Label(window, text="", font=("Arial", 24))
    blank_label.pack()
    
    # Wait for the user's response
    answer = ""
    while answer not in ["y", "n"]:
        window.update()
        answer = window.event_generate("<<GetAnswer>>")
        time.sleep(0.1)
    
    # Remove the blank label
    blank_label.destroy()
    
    # Return the user's response
    return answer

# Define a function to repeat the hello, image, and blank screen sequence
def repeat_sequence():
    # Loop 20 times
    for i in range(20):
        show_hello_and_image()
        answer = show_blank_screen()
        print("Answer:", answer)

#
