from playsound import playsound
import os
folder_name = "sounds"
file_name = "boer_man.mp3"
sound_path = os.path.join(folder_name, file_name)

playsound(sound_path)