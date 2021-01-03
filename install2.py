import tkinter as tk
# importing tkinter module 
from tkinter import * 
from tkinter.ttk import *
import os

root = Tk()
root.title("Titanium V0.7 Download")
root.geometry("600x380")
root.config(bg="#900C3F")

import tkinter as tk
#also maximize button remover
root.resizable(0,0)

root.iconbitmap('icon.ico')

def end():
    print("Successfully Installed~ !!")
    l2 = tk.Label(root, text="Successfully Installed~ !!", fg="white", bg="#900C3F")
    l2.pack()
    Button(root, text = 'Finish', command = root.destroy).place(relx = 0.1, rely = 0.9)
    

frame3 = tk.Frame(root, bg="#581845")
frame3.place(relwidth=4, relheight=1, relx=0.9, rely=0)

progress = Progressbar(root, orient = HORIZONTAL,
              length = 480, mode = 'determinate') 
  
# Function responsible for the updation 
# of the progress bar value 
def bar(): 
    import time 
    progress['value'] = 20
    root.update_idletasks() 
    time.sleep(1.7)

    os.system("")
    
    progress['value'] = 40
    root.update_idletasks() 
    time.sleep(1.7) 

    os.system("")

    progress['value'] = 50
    root.update_idletasks() 
    time.sleep(1.7)

    os.system("")
  
    progress['value'] = 60
    root.update_idletasks() 
    time.sleep(1.7)

    os.system("")
  
    progress['value'] = 80
    root.update_idletasks() 
    time.sleep(1.7)

    os.system("")


    progress['value'] = 100

    return end()


progress.place(relx = 0.1, rely = 0.8)


frame5 = tk.Frame(root, bg="#300A24")
frame5.place(relwidth=6, relheight=0.7, relx=0, rely=0.05)

frame5 = tk.Frame(root, bg="#67CA7A")
frame5.place(relwidth=0.1, relheight=0.03, relx=0, rely=0.1)

frame5 = tk.Frame(root, bg="#C22A10")
frame5.place(relwidth=0.03, relheight=0.03, relx=0.11, rely=0.1)

frame5 = tk.Frame(root, bg="#67CA7A")
frame5.place(relwidth=0.06, relheight=0.03, relx=0.16, rely=0.1)


lbl=tk.Label(root, bg="#67CA7A", height=1, fg="black", text=" ~ : $")
lbl.place(relx=0.24, rely=0.084)


Button(root, text = 'Install', command = bar).place(relx = 0.1, rely = 0.9)

Button(root, text = 'Cancel', command = root.destroy).place(relx = 0.25, rely = 0.9)







root.mainloop()