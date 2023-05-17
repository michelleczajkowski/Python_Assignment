import tkinter as tk

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
name_label = tk.Label(window, text="Your first name (first four letters):", fg="white", bg="black", font=("Arial", 16))
name_field = tk.Entry(window, font=("Arial", 16))

# create a label and text entry field for the language choice
lang_label = tk.Label(window, text="Mother Language (d for Dutch or e for English):", fg="white", bg="black", font=("Arial", 16))
lang_field = tk.Entry(window, font=("Arial", 16))

# create a label and text entry field for the gender choice
gend_label = tk.Label(window, text="Gender (m or f):", fg="white", bg="black", font=("Arial", 16))
gend_field = tk.Entry(window, font=("Arial", 16))

# create a button to save the user's name and language choice
save_button = tk.Button(window, text="Save", command=save_data, fg="white", bg="black", font=("Arial", 16))

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

# the name, lang, and gend variables will now contain the user's entered data
print("Hello,", name)
print("Your selected language is", lang)
print("Your gender is", gend)

