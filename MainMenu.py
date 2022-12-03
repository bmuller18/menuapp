from tkinter import * 
from PIL import ImageTk, Image
root = Tk()
root.overrideredirect(1)
#IMAGES
fbimage=Image.open('C:/Users/brand/Desktop/Practicas/Ongit/menuapp/faceicon.png')
fb=fbimage.resize((50,50))
fb=ImageTk.PhotoImage(fb)


botimg = Image.open("C:/Users/brand/Desktop/Practicas/Ongit/menuapp/bottom.jpg")
bot = botimg.resize((800,500))
bot = ImageTk.PhotoImage(bot)



root.geometry("800x800")
bottomlbl = Frame(root, bg='white', height=800, width=800)
uplbl = Label(bottomlbl, bg= '#FCFCFC')

lb = Label(uplbl, height=250, width=200, image=fb, bg='#D1D1D1').grid(row=1, column=0)
uplbl.pack(fill = BOTH,)

botlbl = Label(bottomlbl, image=bot, anchor=CENTER).pack(fill=X)



close = Button(root, text = "Close Window", command = lambda: root.destroy())
close.pack(fill = BOTH, expand = True)
bottomlbl.pack()
root.mainloop()