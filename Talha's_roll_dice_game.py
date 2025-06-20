from tkinter import *
import random

fun = Tk()
fun.geometry("700x450")
fun.title("Talha's Roll Dice")

label = Label(fun, text = "", font = ("times", 260))

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text = f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()
    
button = Button(fun, text = "Let's Roll...", width = 40, height = 5, font = 10, bg = "white", bd = 2, command = roll)
button.pack(padx = 10, pady = 10)

fun.mainloop()