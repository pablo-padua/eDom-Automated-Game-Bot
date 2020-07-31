import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
from main import eDomBot, username, password, cronometro, energy, no_energy, zero, logging


root = tk.Tk()

canvas = tk.Canvas(root, height="400", width="500")
canvas.pack()

img = ImageTk.PhotoImage(Image.open('back.png'))
back_img = tk.Label(root, image=img)
back_img.place(relwidth=1,relheight=1)

frame=tk.Frame(root, bg="light green")
frame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.5)

label1 = tk.Label(frame, text="Login:" , bg="light green" ,font=('Century',12))
label1.place(relx=0.39, rely=0.03, relwidth=0.25, relheight=0.1)

entry1 = tk.Entry(frame)
entry1.place(relx=0.27, rely=0.17, relwidth=0.5, relheight=0.1)

label2 = tk.Label(frame, text="Password:" , bg="light green" ,font=('Century',12))
label2.place(relx=0.37, rely=0.32, relwidth=0.3, relheight=0.1)

entry2 = tk.Entry(frame)
entry2.place(relx=0.27, rely=0.45, relwidth=0.5, relheight=0.1)

def execute():
    username = entry1.get()
    password= entry2.get()
    bot=eDomBot(username,password)
    while True:
        bot.moving_on(cronometro, energy, no_energy)
        bot.my_productions(zero)
        for x in range(1, 300):
            logging.warning("Loopin for the " + str(x) + "° time.")
            bot.moving_on(cronometro, energy, no_energy)

button = tk.Button(frame, text="Confirm", bg="gray", fg="white", font=('Century',12), command=execute)
button.place(relx=0.38,rely=0.65,relwidth=0.28,relheight=0.12)

label3 = tk.Label(root, text="SilverBot by PrivatePM" , bg="light green" ,font=('Century',12), borderwidth=10)
label3.place(relx=0.01, rely=0.94, relwidth=0.35, relheight=0.05)

label4 = tk.Label(root, text="PrivatePM#6916 on Discord" , bg="light green" ,font=('Century',12), borderwidth=10)
label4.place(relx=0.58, rely=0.94, relwidth=0.42, relheight=0.05)

root.mainloop()
