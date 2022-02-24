import tkinter as tk


class Window:
    """
    #Tkinter windows nesnesi olusturan class
    #Windows nesnesi root yani en temel nesnedir
    """
    #__init__ metodunda tkinter window olusturalim
    def __init__(self,title):
        self.window=tk.Tk()
        self.window.title(title)
        #self.window.configure(bg="#121212")
        #self.window.geometry("600x800")

    #window'u baslatmamiz ve tkinter windows baslamasi icin main loop vermemiz gerekir
    def start_window(self):
        self.window.mainloop

  # Ana Pencere

window=Window("Film Kütüphanesi")
    #penceremizi baslat
window.start_window()

