#from PIL import Image,ImageTk
#import tkinter.font as font
import tkinter as tk
#import tkinter
root = tk.Tk()
# root.title("Hello")
# root.geometry("500x200")
# course = Label(root, text="Begining to advance..", bg="red", fg="white")
# enroll = Label(root, text="enroll", bd=5)
# java = Label(root, text="Begining to advance..", bg="red", fg="white")

#############Positioning

# python = Label(root, text="enroll", bd=5)
# course.grid(row=0, column=0)
# enroll.grid(row=0,column=1)
# java.grid(row=1, column=0)
# python.grid(row=1 , column=1)
# enroll.pack()
# course.pack()

######## get data

# lbl = Label(root, text="name")
# data = Entry(root)
# lbl.grid(row=0, column=0)
# data.grid(row=0, column=1)

######### Image

# img = Image.open("rose.jpg.jpg") # PIL
# img.show() # PIL
# picture = ImageTk.Photo # PIL
# python = Label(root,image=picture)
# python.pack()

##### fonts

## tuple()
#lbl = Label(root, text="python", font=("Halvetica"))
#lbl.pack()
#
###  Using Object font
#font = font.Font(family="serif", size= 18, weight="Bold")
#lbl = Label(root, text="Programming", font= font)
#lbl.pack()
root.mainloop()