#import
import tkinter as tk
from tkinter import Text

#ana pencere
window=tk.Tk()
window.title("Tkinter Temelleri-Text")
window.geometry("600x400")


#Text widget
txt=Text(window,height=4,width=20,background="red")




#yerlestir
txt.pack()



#mainloop
window.mainloop()