import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
root = tk.Tk()
canvas = tk.Canvas(root, width = 600,height = 500, bg = "white", highlightbackground = 'white')
canvas.grid(columnspan = 3, rowspan = 3)


# Logo de inicio
img1 = Image.open("ima.gif")
img1 = img1.resize((800, 350), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)

def halc():
    canvas.grid_forget()
    canmen.grid_forget()
def halcinst():
    canins.pack_forget()
    lab3.pack_forget()
    bot5.pack_forget()
    lab4.pack_forget()
    bot6.pack_forget()
    lab5.pack_forget()
    bot7.pack_forget()

def menu ():
    usr = tk.StringVar()
    usr = ent1.get()
    x=usr
    if bool(usr):
        halc()
        lab2 = tk.Label(canmen,text= "Hola " + x +" bienvenido al mejor juego de damas chinas", bg= "white")
        canmen.grid(columnspan = 3, rowspan = 3)
        lab2.grid(row=0, columnspan=3)
        print ( usr)
    else:
        messagebox.showwarning(message= "Incluir un mobre de usiuario valido", title="nombre de usuiario")

# layout del inicio
img1_lab = tk.Label(canvas, image = img1, highlightbackground = 'white' ).grid(row = 0, column = 2)
lab1 = tk.Label(canvas, text = "Hola, Ingresa nombre de Usuario", highlightbackground = 'white', bg= "white")
lab1.grid(row= 1, columnspan = 3)
ent1 = tk.Entry(canvas,highlightbackground = 'white')
ent1.grid(row = 2, column = 2)
bot1 = tk.Button(canvas, text = "Continuar", command = menu, highlightbackground = 'white')
bot1.grid(row= 3, column = 2)

#layot de menu
canmen = tk.Canvas(root, width = 600,height = 500, bg = "white", highlightbackground = 'white')
bot2 = tk.Button(canmen, text= "Iniciar partida", highlightbackground = 'white')
bot2.grid(row= 1, column =1)
bot3 = tk.Button(canmen, text="Instrucciones", highlightbackground = 'white')
bot3.grid(row=1,column= 2)
bot4 =tk.Button(canmen, text="Salir del Juego", command = root.quit, highlightbackground = 'white')
bot4.grid(row=2,column= 1,columnspan=2)
"""""""""
#layout de instrucciones
canins = tk.Canvas(root, width = 600,height = 500, bg = "white", highlightbackground = 'white')

img2 = Image.open("reglas.png")
img2 = image.resize((300, 100), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)
lab3 = tk.Label(canins, image = img2, highlightbackground = 'white' )
bot5 =tk.Button(canins, text="Continuar", command = inst2, highlightbackground = 'white')

img3 = Image.open("estrategia.png")
img3 = image.resize((300, 100), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img3)
lab4 = tk.Label(canins, image = img3, highlightbackground = 'white' )

img4 = Image.open("Final.png")
img4 = image.resize((300, 100), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(img4)
lab5 = tk.Label(canins, image = img4, highlightbackground = 'white' )
"""""
root.mainloop()
