#!/usr/bin/python3



import tkinter as tk

# importing tkinter module 

from tkinter import * 

from tkinter.ttk import *

import os





def cld(r, g, b,text):                                                          #

    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text) # 

text = 'Installing will be attempted here.'                                     #

colored_text = cld(255, 0, 0, text)                                             #

print(colored_text)







root = Tk()



root.iconbitmap('my2.ico')

root.title("Titanium V0.7 Download")

root.geometry("600x380")

root.config(bg="#900C3F")



import tkinter as tk

#also maximize button remover

root.resizable(0,0)





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

    os.system("clear")

    

    import time 

    progress['value'] = 15

    root.update_idletasks() 

    time.sleep(1.7)



    os.system("sudo apt install git")

    

    progress['value'] = 25

    root.update_idletasks() 

    time.sleep(1.7) 



    os.system("sudo apt install john")



    progress['value'] = 35

    root.update_idletasks() 

    time.sleep(1.7)



    os.system("sudo apt-get install cmatrix")

  

    progress['value'] = 45

    root.update_idletasks() 

    time.sleep(1.7)



    os.system("git clone https://github.com/amoiz3567/Titanium-By-amoiz-via-linux")

  

    progress['value'] = 55

    root.update_idletasks() 

    time.sleep(1.7)



    os.system("sudo cp /Titanium-By-amoiz-via-Windows/learn.py /usr/bin/tn")





    progress['value'] = 65

    root.update_idletasks() 

    time.sleep(1.7)

    

    os.system("")

    

    

    progress['value'] = 75

    root.update_idletasks() 

    time.sleep(1.7)

    

    

    print("[+] Please, Type as said below so you can setup the tool... ")

    cm22 = input("[~] please cd to [ cd Titanium-By-amoiz-via-linux ] : ")

    os.system("" +cm22)

    gg=(cld(199, 0, 57,"[ sudo cp titanium.py /usr/bin/tn ] : "))

    cm2 = input(cld(205, 174, 20,"[~] plz type= " +gg))

    os.system("" +cm2)

    

    progress['value'] = 85

    root.update_idletasks() 

    time.sleep(1.7)

    

    

    os.system("")

    

    progress['value'] = 95

    root.update_idletasks() 

    time.sleep(1.7)

    

    

    os.system("")

    

    progress['value'] = 100

    root.update_idletasks() 

    time.sleep(1.7)



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