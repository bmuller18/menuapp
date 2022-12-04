from tkinter import * 
from PIL import ImageTk, Image
import time



root = Tk()
root.title("")
# Link social buttons to the network
def my_command():
    print("fr")

#IMAGES
fbimage=Image.open('Resources/Fb.png')
fb=fbimage.resize((80,80))
fb=ImageTk.PhotoImage(fb)#FACEBOOK
instaimg=Image.open('Resources/Insta.png')
ins=instaimg.resize((80,80))
ins=ImageTk.PhotoImage(ins)#INSTAGRAM
snapimage=Image.open('Resources/snapchat.png')
sn=snapimage.resize((80,80))
sn=ImageTk.PhotoImage(sn)#SNAPCHCHAT
twimage=Image.open('Resources/twitter.png')
tw=twimage.resize((80,80))
tw=ImageTk.PhotoImage(tw)#TWITTER

botimg = Image.open("Resources/bottom.jpg")
bot = botimg.resize((800,300))
bot = ImageTk.PhotoImage(bot)



root.geometry("800x500")
bottomlbl = Frame(root, bg='white', height=800, width=800)
uplbl = Frame(bottomlbl, bg= '#FFF')
timer = Label(uplbl)

#Clock
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    seconds = time.strftime("%S")


    timer.config(text=hour + ":" + minute  + ":" + seconds, bg='#FCFCFC', font=('verdana', 44, 'bold'))
    timer.after(1000, clock)
clock()

#Let us create a dummy button and pass the image
fbbutton= Button(uplbl, image=fb,command= my_command, height=250, width=200, borderwidth=0, bg='#FFF')
fbbutton.grid(row=1, column=0)
insbutton = Button(uplbl, image=ins, command=my_command, height=250, width=200, borderwidth=0, bg='#FFF')
insbutton.grid(row=1, column=1)
snbutton = Button(uplbl, image=sn, command= my_command, height=250, width=200, borderwidth=0, bg='#FFF')
snbutton.grid(row=1, column=2)
twbutton = Button(uplbl, image=tw, command= my_command, height=250, width=200, borderwidth=0, bg='#FFF')
twbutton.grid(row=1, column=3)
timer.grid(row=0, column=0, columnspan=5)
uplbl.pack(fill = BOTH,)

#   Side bottom image
botlbl = Label(bottomlbl, image=bot, anchor=CENTER).pack(side=BOTTOM)
bottomlbl.pack()
root.mainloop()