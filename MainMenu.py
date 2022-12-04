from tkinter import * 
from PIL import ImageTk, Image
root = Tk()
#IMAGES
fbimage=Image.open('C:/Users/brand/Desktop/Practicas/Ongit/menuapp/Fb.png')
fb=fbimage.resize((50,50))
fb=ImageTk.PhotoImage(fb)
instaimg=Image.open('C:/Users/brand/Desktop/Practicas/Ongit/menuapp/Insta.png')
ins=instaimg.resize((50,50))
ins=ImageTk.PhotoImage(ins)
snapimage=Image.open('C:/Users/brand/Desktop/Practicas/Ongit/menuapp/snapchat.png')
sn=snapimage.resize((50,50))
sn=ImageTk.PhotoImage(sn)
twimage=Image.open('C:/Users/brand/Desktop/Practicas/Ongit/menuapp/twitter.png')
tw=twimage.resize((50,50))
tw=ImageTk.PhotoImage(tw)


botimg = Image.open("C:/Users/brand/Desktop/Practicas/Ongit/menuapp/bottom.jpg")
bot = botimg.resize((800,500))
bot = ImageTk.PhotoImage(bot)



root.geometry("800x800")
bottomlbl = Frame(root, bg='white', height=800, width=800)
uplbl = Label(bottomlbl, bg= '#FCFCFC')

lb = Label(uplbl, height=250, width=200, image=fb, bg='#D1D1D1').grid(row=1, column=0)
lb2 = Label(uplbl, height=250, width=200, image=ins, bg='#D1D1D1').grid(row=1, column=1)
lb3 = Label(uplbl, height=250, width=200, image=sn, bg='#D1D1D1').grid(row=1, column=2)
lb4 = Label(uplbl, height=250, width=200, image=tw, bg='#D1D1D1').grid(row=1, column=3)
uplbl.pack(fill = BOTH,)

botlbl = Label(bottomlbl, image=bot, anchor=CENTER).pack(fill=X)




bottomlbl.pack()
root.mainloop()