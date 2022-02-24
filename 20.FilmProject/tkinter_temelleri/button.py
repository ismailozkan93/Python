#import
import tkinter as tk

#ana pencere
window=tk.Tk()
window.title("Tkinter Temelleri")
window.geometry("800x400")


#Button
btn=tk.Button(master=window,text="Durdur",width=45,#text-unit
              height=5,bg="red",
              fg="white",command=window.destroy)

#btn yerlestir
btn.pack()




#
window.mainloop()
