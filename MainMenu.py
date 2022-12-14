from tkinter import * 
import time
import webbrowser
from PIL import ImageTk, Image



root = Tk()
root.title("")
# Link social buttons to the network
def my_command(social):
    if social == "facebook":
        url = 'http://www.facebook.com'
        webbrowser.register(
            'chrome',
            None,
            webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe')
        )    
        webbrowser.get('chrome').open_new(url)
    elif social == "instagram":
        url = 'http://www.instagram.com'
        webbrowser.register(
            'chrome',
            None,
            webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe')
        )    
        webbrowser.get('chrome').open_new(url)
    elif social == "snapchat":
        url = 'http://www.snapchat.com'
        webbrowser.register(
            'chrome',
            None,
            webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe')
        )    
        webbrowser.get('chrome').open_new(url)
    elif social == "twitter":
        url = 'http://www.twitter.com'
        webbrowser.register(
            'chrome',
            None,
            webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe')
        )    
        webbrowser.get('chrome').open_new(url)
        

#IMAGES

fbimage=Image.open(r'C:\Users\brand\Desktop\Practicas\Ongit\menuapp\Resources/Fb.png')
fb=fbimage.resize((80,80))
fb=ImageTk.PhotoImage(fb)#FACEBOOK
instaimg=Image.open(r'C:\Users\brand\Desktop\Practicas\Ongit\menuapp\Resources/Insta.png')
ins=instaimg.resize((80,80))
ins=ImageTk.PhotoImage(ins)#INSTAGRAM
snapimage=Image.open(r'C:\Users\brand\Desktop\Practicas\Ongit\menuapp\Resources/snapchat.png')
sn=snapimage.resize((80,80))
sn=ImageTk.PhotoImage(sn)#SNAPCHCHAT
twimage=Image.open(r'C:\Users\brand\Desktop\Practicas\Ongit\menuapp\Resources/twitter.png')
tw=twimage.resize((80,80))
tw=ImageTk.PhotoImage(tw)#TWITTER


botimg = Image.open(r"C:\Users\brand\Desktop\Practicas\Ongit\menuapp\Resources/bottom.jpg")
bot = botimg.resize((800,300))
bot = ImageTk.PhotoImage(bot)


#Window configuration
root.geometry("800x500")
bottomlbl = Frame(root, bg='white', height=800, width=800)
uplbl = Frame(bottomlbl, bg= '#FFF')
timer = Label(uplbl)

#Clock
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    seconds = time.strftime("%S")


    timer.config(text=hour + ":" + minute  + ":" + seconds, bg='#fff', font=('verdana', 44, 'bold'))
    timer.after(1000, clock)
clock()

#Let us create a dummy button and pass the image
fbbutton= Button(uplbl, image=fb,command=lambda: my_command("facebook"), height=250, width=200, borderwidth=0, bg='#FFF')
fbbutton.grid(row=1, column=0)
insbutton = Button(uplbl, image=ins, command=lambda: my_command("instagram"), height=250, width=200, borderwidth=0, bg='#FFF')
insbutton.grid(row=1, column=1)
snbutton = Button(uplbl, image=sn, command=lambda: my_command("snapchat"), height=250, width=200, borderwidth=0, bg='#FFF')
snbutton.grid(row=1, column=2)
twbutton = Button(uplbl, image=tw, command=lambda: my_command("twitter"), height=250, width=200, borderwidth=0, bg='#FFF')
twbutton.grid(row=1, column=3)
timer.grid(row=0, column=0, columnspan=4)
uplbl.pack(fill = BOTH,)

#   Side bottom image
botlbl = Label(bottomlbl, image=bot, anchor=CENTER).pack(side=BOTTOM)
bottomlbl.pack()
root.mainloop()