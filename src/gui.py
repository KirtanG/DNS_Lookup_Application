#Importing required libraries.
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from urllib.parse import urlparse
import tkinter as tk
import socket 
from tkinter.filedialog import asksaveasfilename

__author__="Kirtan Goswami"

# Defining functions

def saveFile():
    """
        This function is used to save the content currently present in the TextBox(tkinter.Text) as simple text file. 
    """
    file = None
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None
        else:
            #Save as a new file
            f = open(file, "w")
            f.write(entry_2.get(1.0,tk. END))
            f.close()            

def get_Host_name_IP() -> str:
    """
        This function is used get the IP of the hostname from the textVar and return list of IP addresses and
        return  "Unable to get IP." if none is found.
    """
    hostName = textVar.get().strip()
    if hostName == '':
         return ''
    if not hostName.startswith(('http://', 'https://')):
        hostName = 'http://' +hostName
    parsed_url = urlparse(hostName)   
    domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path  
        
    try: 
            ip = socket.gethostbyname_ex(domain)[2]
            host_ip="\n".join(ip)
            return host_ip 
    except: 
            return "Unable to get IP." 

def textUpdate():
    """
        This function updates the state of the textBox and updates the text to the IP address.
    """
    entry_2["state"]="normal"
    entry_2.delete(1.0,tk.END)
    # text.insert('end', 'This is a Text widget demo.\n'+textVar.get()+ get_Host_name_IP()+"\n")
    if get_Host_name_IP() == '':
        entry_2.insert('end', "Please enter a valid URL!\n")
    else: 
        entry_2.insert('end', 'IP address/es are:\n'+ get_Host_name_IP()+"\n")
    entry_2["state"]="disabled"

def clearTextBox():
    """This functions clears both entries to Empty."""
    textVar.set(" ")
    entry_1.delete(0,tk.END)
    entry_2["state"]="normal"
    entry_2.delete(1.0,tk.END)
    entry_2["state"]="disabled"

def relative_to_assets(path: str) -> Path:
    return f"{Path(__file__).parent}\\assets\\{path}" 

#GUI logic

window = Tk()
window.title("DNS lookup")
window.geometry("507x715")
window.wm_iconbitmap(f"{Path(__file__).parent}\\assets\\dns.ico")
window.configure(bg = "#FFFFFF")

textVar = tk.StringVar()

canvas = Canvas(
    window,
    bg = "#E3E3E3",
    height = 715,
    width = 507,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    21.0,
    18.0,
    anchor="nw",
    text="Enter a URL:",
    fill="#000000",
    font=("Arial", 20)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    253.5,
    80.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font="timesnewroman 18",
    textvariable=textVar
)
entry_1.place(
    x=21.0,
    y=57.0,
    width=465.0,
    height=45.0
)

canvas.create_text(
    21.0,
    188.0,
    anchor="nw",
    text="Output:",
    fill="#000000",
    font=("Arial", 20)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    253.5,
    462.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0,
    font=("Open Sans",14)    
)
entry_2.place(
    x=21.0,
    y=227.0,
    width=465.0,
    height=468.0
)
entry_2['state'] = 'disabled'

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clearTextBox,
    relief="flat"
)
button_1.place(
    x=178.0,
    y=114.0,
    width=140.0,
    height=64.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=saveFile,
    relief="flat"
)
button_2.place(
    x=345.0,
    y=114.0,
    width=140.0,
    height=64.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=textUpdate,
    relief="flat"
)
button_3.place(
    x=21.0,
    y=114.0,
    width=140.0,
    height=64.0
)
window.resizable(False, False)
window.mainloop()
