#import
import tkinter as tk


#ana pencere
window=tk.Tk()
window.title("Tkinter Temelleri-CheckButton")
window.geometry("600x400")

#Checkbutton Widget
chkBtn=tk.Checkbutton(master=window,text="True")
chkBtn1=tk.Checkbutton(master=window,text="False",bg="blue")
#yerlestir
chkBtn.grid(row=0,column=0)
chkBtn1.grid(row=1,column=0)






#mainloop
window.mainloop()