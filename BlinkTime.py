import threading
import tkinter as tk


statue= True
mon_timer =  threading.Timer(20 * 60)
pausechoose = 20


def pausebloque(): #affichage bloquant l'utilisateur à faire quelque action
    pause_window = tk.Toplevel()
    pause_window.attributes('-fullscreen',True)
    pause_window.attributes('-topmost',True) #toujours audessus
    pause_window.config(bg="Black" \
    #Message
    label = tk.Label(pause_windows, text="Fais une pause pendant 20 seonces !", fg="white", bg="black", font=("Arial",30))
    label.pack(expand=True)
    pause_window.grab_set()
    pause_window.after(pausechoose , pause_window.destroy)

root = tk.Tk()


while statue == True:
    mon_timer.start()
    if mon_timer == 0:
        pausebloque()




