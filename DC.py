from tkinter import *
import tkinter as tk
import tkinter.messagebox

# Pagina Principal
root = tk.Tk()
root.title('Proyecto ML Damas chinas - PUJ')
root.resizable(0, 0)

# Funciones del menu
# nuevo Juego
def iniciog():
    njug = entry.get()
    hide_all_f()
    gconf.pack(fill = "both", expand = 1 )

#cerrar otros frames
def hide_all_f():
    frame.pack_forget()
    gconf.pack_forget()

# BOTON ATRAS
def mainb():
    hide_all_f()
    frame.pack(fill = "both", expand = 1)

# Instrucciones
def inst():
     ("Instrucciones", "Blah Blash Blash ...")

# Menu del juego
pmenu = Menu(root)
root.config(menu = pmenu,bg = "#ffffff")
# setting geometry of tk window
root.geometry("600x600")

# crear los items del menu

inicio = Menu(pmenu)
pmenu.add_cascade(label = "Menu", menu = inicio)
inicio.add_command(label = "Nuevo Juego", command = iniciog)
inicio.add_command(label = "Acerda de")
inicio.add_command(label = "Salir", command = root.quit)


# crear menu frame de  welcome

frame = tk.Canvas(root, bg = '#ffffff', width = 600, height= 600)
frame.pack()

# imagen de inicio
img1 = PhotoImage(file = "/Users/junkal/Documents/Machine Learning /Proyecto Damas/ima.gif")
Label(frame, image = img1).pack()

label = tk.Label(frame, text = 'Ingrese su nombre', bg = '#ffffff', fg = 'black', padx = 10, pady = 10, font=("Calibri", 23), highlightthickness =0 )
label.pack()
entry = tk.Entry(frame, bg = '#ffffff', font=("Calibri", 23), highlightthickness =0, show = '*')
entry.pack()
njug = StringVar().set(entry.get())

button = tk.Button(frame, text= 'Continuar', font=("Calibri", 13), bg = "black", fg = "black", height = 1, command = iniciog)
button.pack()


#crear frame de config game

gconf= tk.Canvas(root, bg = '#ffffff',width = 600, height= 600, highlightthickness =0)
labmenu = Label(gconf,text = "MENU", fg = 'black',font=("Calibri", 23))
labmenu.pack()
labbien = Label(gconf, text = "Hola " + str(njug) + "Cómo estas").pack()
labinst = Button(gconf,text = "Instrucciones",fg = 'black', command = inst, highlightthickness =0)
labinst.pack()
labstart = Button(gconf,text = "Comenzar", fg = 'black', highlightthickness =0)
labstart.pack()
labatra = Button(gconf,text = "Atras", fg = 'black', command = mainb, highlightthickness =0)
labatra.pack()





root.mainloop()
