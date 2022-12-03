from tkinter import * 
from PIL import ImageTk, Image

root = Tk()

#IMAGES
fbimage = ImageTk.PhotoImage(Image.open("C:/Users/brand/Desktop/Proyectos/MenuFront/FrontPanel/faceicon.png"))
botimg = ImageTk.PhotoImage(Image.open("C:/Users/brand\Desktop/Proyectos/MenuFront\FrontPanel/bottom.jpg"))

root.geometry("800x800")
toplbl = Label(root, height=200, width=200, bg= 'white')
uplbl = Label(toplbl, bg= '#fffff1').pack()

lb = Label(uplbl, height=250, width=200, image=fbimage).pack(fill=X)

botlbl = Label(toplbl, image=botimg, anchor=CENTER).pack(fill=X)
toplbl.pack()
root.mainloop()