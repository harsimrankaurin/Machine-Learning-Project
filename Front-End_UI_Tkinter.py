import tkinter as tk
# from tkinter import Canvas, Entry, Grid, INSERT, END
import pandas as pd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
# import numpy as np

# take the data


window = tk.Tk()

#setting tkinter window size
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Restaurant Recommender")

#Read CSV File 
df = pd.read_csv('abt_count.csv')

#Fetching top 20 user_id
lst = df['user_id'].head(20)
total_rows = len(lst)
total_columns = len(lst[0])

#Left Frame
frame1 = tk.Frame(master=window, width=400, bg="#135D75")
frame1.pack(fill="both", side=tk.LEFT)

#Main Heading label1
label1 = tk.Label(master=frame1, text="Select your USER ID:")
label1.place(x=30,y=50)
label1.config(font='Helvetica 18')
label1.config(bg="#135D75",fg="white")

#Header after the label1
horizontal =tk.Frame(master=frame1, bg='white', height=1,width=300)
horizontal.place(x=30, y=90)

#Table Grid Frame
framegrid = tk.Frame(master=frame1, width=400, height=900, bg="#135D75", borderwidth=0)
for x, i in zip(lst,range(total_rows)):
    for y in range(1):
        #Start count from 1
        i = i+1

        #Text to display in each label
        txt = (str(i) + " : " +  x)

        #Setting padding and position of the grid
        framegrid.grid(row=i, column=y, padx=5, pady=5)

        #Passing each user_id in each label
        labelgrid = tk.Label(master=framegrid, text=txt, bg="#135D75",fg="white")
        labelgrid.config(font='Helvetica 14')
        labelgrid.pack(pady=1,side="top", anchor="w")
        
#Placing table grid
framegrid.place(x=30, y=130)       

#Right Frame
frame2 = tk.Frame(master=window, bg="#F0F0F0")
frame2.place(relx=0.5, rely=0.5,anchor="center")
frame2.pack(expand = True,fill="both", side=tk.LEFT)

image = Image.open("img.png")
resize_image = image.resize((1000, 400))
img = ImageTk.PhotoImage(resize_image)

#Header after the label1
frame2_child =tk.Frame(master=frame2, bg='#F0F0F0', height=200, width=200)
frame2_child.place(relx=0.5, rely=0.3,anchor="center")

def download_clicked():
    showinfo(
        title='Information',
        message='Submit button clicked!'
    )

#Main Heading label1
label1 = tk.Label(
    master=frame2_child, 
    text="Get your recommendation",
    bg="#F0F0F0",
    fg="#135D75"
)
label1.place(relx=0.4, rely=0.3,anchor="center")
label1.config(font='Helvetica 18')
label1.pack(pady=20,side="top", anchor="w")

submit_btn = tk.Button(
    frame2_child,
    text='Submit',
    height=1,
    width=15,
    bg="#135D75",
    fg="white",
    command=download_clicked
)

submit_btn.place(y=200)   

submit_btn.config(font='Helvetica 14')

submit_btn.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

img1 = tk.Label(frame2, image = img)
img1.place(x=100,y=50)
img1.pack(side="bottom")


#Setting the window resizing to false
window.resizable(False, False)

#Recurrsive loop to keep running the application
window.mainloop()
