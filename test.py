import tkinter as tk

# Create a blank window
window = tk.Tk()
window.title("Stimulus")
window.geometry("800x600")
window.attributes("-topmost", True)
canvas = tk.Canvas(window, width=800, height=600, bg='black')
canvas.pack()
canvas.create_text(400, 300, text="Mini-Experiment\nRound 1 of 2", fill='white', width=600, font=('Arial', 30), anchor=tk.CENTER)
canvas.update()
window.after(2000)

canvas.delete("all")

# Create a label and entry field for the user to enter their name
tk.Label(window, text="Enter your first name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Create a label and entry field for the user to enter their first language
tk.Label(window, text="First language:").pack()
lang_entry = tk.Entry(window)
lang_entry.pack()

# Create a label and entry field for the user to enter their gender
tk.Label(window, text="Gender:").pack()
gender_entry = tk.Entry(window)
gender_entry.pack()

# Function to set the variables and exit the mainloop
def set_variables(event):
    global name, lang, gend
    name = name_entry.get()
    lang = lang_entry.get()
    gend = gender_entry.get()
    window.quit()

# Bind the <Return> event to the entry widgets
name_entry.bind("<Return>", set_variables)
lang_entry.bind("<Return>", set_variables)
gender_entry.bind("<Return>", set_variables)

# Start the mainloop
window.mainloop()

# Print the variables
print("Name:", name)
print("Language:", lang)
print("Gender:", gend)
