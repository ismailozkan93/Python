#import
import tkinter as tk
from tkinter import Label,Entry

#Label-->Metin yazar
#Entry-->Tek satir metin girisi

#ana pencere
window=tk.Tk()
window.title("Tkinter Temelleri--Label--Entry")
window.geometry("600x400")

#Label Widget
lblAd=Label(master=window,text="Adi")
lblSoyad=Label(master=window,text="Soyadi")

#Entry Widget
entAd=Entry(window)
entSoyad=Entry(window)

#yerlestir
lblAd.grid(row=0)
entAd.grid(row=0,column=1)

lblSoyad.grid(row=1)
entSoyad.grid(row=1,column=1)

#mainloop
window.mainloop()

