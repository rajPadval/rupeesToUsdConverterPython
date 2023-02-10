from tkinter import *
import requests
root = Tk()
root.geometry("1200x400+50+50")
root.title("Motivational Quote Generator")
f = ("Arial",40,"bold")
def getData():
    url = "http://api.quotable.io/random"
    res = requests.get(url)
    data = res.json()
    msg = data["content"]
    label.configure(text=msg)

btn = Button(root,text="Generate",font=f,command=getData)
btn.pack(pady=30)
label = Label(root,font=f,wraplength=1000)
label.pack()
root.mainloop()