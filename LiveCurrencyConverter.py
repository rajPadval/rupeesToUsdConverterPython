from tkinter import *
import requests
root = Tk()
root.geometry("1200x400+50+50")
root.title("Motivational Quote Generator")
f = ("Arial", 40, "bold")


def getData():
    url = "https://api.exchangerate-api.com/v4/latest/usd"
    res = requests.get(url)
    data = res.json()
    msg = data["rates"]["INR"]
    enterdNum = User.get()
    converted = float(enterdNum)/msg
    ans.configure(text=f"The Amount is ${round(converted,2)}")


label = Label(root, font=f, text="Enter amount in ₹")
label.pack(pady=20)
User = Entry(root, font=f)
User.pack()
btn = Button(root, text="Generate", font=f, command=getData)
btn.pack(pady=30)
ans = Label(root, font=f,)
ans.pack(pady=10)

root.mainloop()
