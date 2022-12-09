import tkinter
from tkinter import filedialog as fd
import customtkinter
from classYT import yutube
import threading
import time

y = yutube()

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"

app = customtkinter.CTk()
app.geometry("500x550")
app.title("Youtube Video Downloader")
mytext = ""
label_text = ""


# ------------------- some methods of backend here ------------------ 
def download_call_back():
    print("Button click", combobox_1.get())
    link = link_entry.get()
    print("link", link)
    global label_text

    if link == "":
        label_1.configure(text="No link inserted")
        time.sleep(2)
        label_1.configure(text="")
        return
        
    else:
    
        if combobox_1.get() == "Highest Quality" and checkbox_1.get() == 0:
            label_text = y.donwload_highest_resolution(link, mytext)

        elif checkbox_1.get() == 1:
            label_text = y.donwload_only_sound(link, mytext)
    
        elif checkbox_2.get() == 1 and checkbox_1.get() == 0:
            label_text = y.download_playlist(link, mytext)

        else:
            label_text = y.download_video(link, mytext, combobox_1.get())
            

        label_1.configure(text=label_text)

def browse_call_back():
    global mytext
    mytext = fd.askdirectory()
    print("Dir Selected", mytext)
    if mytext == "":
        path_label.configure(text ="Folder no selected")
    else:    
        path_label.configure(text = mytext)

def checkbox_call_back():
    print("Button click", checkbox_1.get())

def checkbox_call_back_2():
    print("Button click", checkbox_2.get())


# ------------------- ends methods of backend here ------------------ 


#frame base 
frame_1 = customtkinter.CTkFrame(master=app) 
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


link_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter Link Here")
link_entry.pack(pady=20, padx=10, fill="both")

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="")
label_1.pack(pady=10, padx=10)

quality_label = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Select Quality of Video")
quality_label.pack(pady=10, padx=10)
combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Highest Quality", "720p"])
combobox_1.pack(pady=10, padx=10)
#optionmenu_1.set("CTkComboBox")

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="Only Sound", command=checkbox_call_back)
checkbox_1.pack(pady=10, padx=10)

checkbox_2 = customtkinter.CTkCheckBox(master=frame_1, text="PlayList", command=checkbox_call_back_2)
checkbox_2.place(relx=0.575, rely=0.55, anchor=tkinter.E)

download_button = customtkinter.CTkButton(master=frame_1, command=download_call_back, text="Download")
download_button.place(relx=0.5, rely=0.85, anchor=tkinter.E)

browse_button = customtkinter.CTkButton(master=frame_1 ,command=browse_call_back, text="Select Folder")
browse_button.place(relx=0.7, rely=0.85, anchor=tkinter.CENTER)

path_label = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="")
path_label.pack(pady=40, padx=10)

if __name__ == '__main__':
    app.mainloop()