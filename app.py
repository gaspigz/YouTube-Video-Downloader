from tkinter import *
from pytube import YouTube
from os import path
from pathlib import Path

root = Tk()
root.geometry('500x450')
root.resizable(0,0)
root.title("YTVD @gaspigz") #Titulo de la ventana

Label(root,text = 'YT Video Downloader', font ='arial 20 bold').pack() #Label es texto que el usuario no puede cambiar

link = StringVar()
Label(root, text = "Link del video: ", font = 'arial 15 bold').place(x= 170 , y = 60)
#dire = StringVar()
#Label(root, text = "Direccion de descarga: ", font = 'arial 15 bold').place(x= 170 , y = 120)

#link_enter = Entry(root, width = 70,textvariable = dire).place(x = 32, y = 150)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.filter(res="720p").first().download('C:/Users/Gaspi/Downloads')
    lbl1 = Label(root, text = 'DESCARGADO', fg="DarkOrange3", font = 'arial 15').place(x= 170 , y = 240)
    lbl2 = Label(root, text = url.title, font = 'arial 15').place_configure(x=170, y=290)



Button(root,text = 'DESCARGAR', font = 'arial 15 bold' ,bg = 'gold3', padx = 2, command = Downloader).place(x=170 ,y = 190)

root.mainloop()

