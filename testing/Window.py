__author__ = 'Frank'

from Tkinter import *
import tkFont
import ImageTk
import random

window = Tk()
window.title("pyDuctor")
window.geometry('600x600+50+50')

#photoimage = ImageTk.PhotoImage(file="musicalnotesv3.png")
#photoimage.place(relx=0.0, rely=0.0)

helvetica = tkFont.Font(family='Helvetica', size=20)

vol_label = Label(window, text="Volume", font=helvetica, fg='orange')
vol_label.place(relx=0.2, rely=0.3, relheight=0.1, relwidth=0.2)

tempo_label = Label(window, text="Tempo", font=helvetica, fg='orange')
tempo_label.place(relx=0.6, rely=0.3, relheight=0.1, relwidth=0.2)

volume = 12
tempo = 12

canvas = Canvas(window)
canvas.place(relx=0.0, rely=0.4, relheight=0.6, relwidth=1)

canvas.update()
width = canvas.winfo_width()
height = canvas.winfo_height()

def drawCanvas():
    canvas.delete(ALL)
    volume = random.randint(1, 12);
    tempo = random.randint(1, 12);
    print volume
    print tempo
    vol_rectangle = canvas.create_rectangle(width*0.2, height*(1.0 - 0.08*volume), width*0.4, height+1, fill='orange', outline='orange')
    tempo_rectangle = canvas.create_rectangle(width*0.6, height*(1.0 - 0.08*tempo), width*0.8, height+1, fill='orange', outline='orange')
    canvas.after(200, drawCanvas)

drawCanvas()

window.mainloop()


