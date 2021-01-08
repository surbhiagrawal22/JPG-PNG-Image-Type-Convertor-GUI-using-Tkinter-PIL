#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk 
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox


# In[ ]:


window = tk.Tk(screenName="Online Tool Converter")
frame=tk.Frame()

label = tk.Label(master=frame,
                 background="black", borderwidth=6,  font="arial", foreground="white",
                 relief="raised",  text="Online Tool Converter",
                 underline=True)


def select_image():
    global image1
    imagepath = filedialog.askopenfilename(defaultextension='.jpg')
    image1 = Image.open(imagepath)
  

def convert_image():
    global image1
    save_path = filedialog.asksaveasfilename(defaultextension='.png')
    image1.save(save_path)


button = tk.Button(master=frame,font=('helvetica', 12, 'bold'),
                   text="Select Image File to convert",
                   underline=True, command=select_image,  height=15, width=50, relief="raised", borderwidth=10,bg="white",fg="dark blue")

button1 = tk.Button(master=frame,
                    font=('helvetica', 12, 'bold'),
                    text="Save a File",
                    underline=True, command=convert_image, height=15, width=50, relief="raised", borderwidth=10,bg="white",fg="dark blue")

label.pack()
button.pack()
button1.pack()
frame.pack()
window.mainloop()


# In[ ]:





# In[ ]:




