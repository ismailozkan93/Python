#import
import tkinter as tk
from tkinter import Frame,Button

#Frame:container,baska widget'lari tutar

#ana pencere
window=tk.Tk()
window.title("Tkinter Temelleri--Label--Entry")
window.geometry("600x400")

#Frame Widget
frame=Frame(window)

#frame icini doldur
btnLeft=Button(master=frame,text="Frame Butonu lEFT",bg="black",fg="white")
btnLeft.pack(side=tk.LEFT)

btnRight=Button(master=frame,text="Frame Butonu RIGHT",bg="black",fg="white")
btnRight.pack(side=tk.RIGHT)


#yerlestir
frame.pack()


#mainloop
window.mainloop()