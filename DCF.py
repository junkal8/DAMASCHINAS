import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
root = tk.Tk()
root.resizable(0, 0)
frain=tk.Frame(root, width = 700,height = 600)
frain.pack()
canvas = tk.Canvas(frain, width = 600,height = 500, bg = "white", highlightbackground = 'white')
canvas.pack()
frain2=tk.Frame(root, width = 700,height = 600)


# Logo de inicio
img1 = Image.open("ima.gif")
#img1 = img1.resize((800, 350), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)

def halc():
    frain.pack_forget()
    canmen.pack_forget()

def menu ():
    usr = tk.StringVar()
    usr = ent1.get()
    x=usr
    if bool(usr):
        halc()
        frain2.pack()
        lab2 = tk.Label(canmen,text= "Hola " + x +" bienvenido al mejor juego de damas chinas", bg= "white")
        canmen.pack()
        lab2.pack()
        bot2.pack()
        bot3.pack()
        bot4.pack()
        print ( usr)
    else:
        messagebox.showwarning(message= "Incluir nombre de usiuario valido", title="nombre de usuiario")



def create_circle(x, y, r, canvasName,Col): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=Col)
def create_line(x,y, canvasName):
    x0 = x
    y0 = y
    x1 = x + 1
    y1 = y + 1
    return canvasName.create_rectangle()

# Definir el espacio del tablero
# G = verde, R = rojo, Y = amarillo, B = Azul, P = morado, O= maranja
def tablero():
    tab = [[" "," "," "," "," "," "," "," "," "," "," "," ","G"," "," "," "," "," "," "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "," "," "," "," ","G"," ","G"," "," "," "," "," "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "," "," "," ","G"," ","G"," ","G"," "," "," "," "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "," "," ","G"," ","G"," ","G"," ","G"," "," "," "," "," "," "," "," "," "],
           ["B"," ","B"," ","B"," ","B"," ","E"," ","E"," ","E"," ","E"," ","E"," ","Y"," ","Y"," ","Y"," ","Y"],
           [" ","B"," ","B"," ","B"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","Y"," ","Y"," ","Y"," "],
           [" "," ","B"," ","B"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","Y"," ","Y"," "," "],
           [" "," "," ","B"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","Y"," "," "," "],
           [" "," "," "," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," "," "," "," "],
           [" "," "," ","P"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","O"," "," "," "],
           [" "," ","P"," ","P"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","O"," ","O"," "," "],
           [" ","P"," ","P"," ","P"," ","E"," ","E"," ","E"," ","E"," ","E"," ","E"," ","O"," ","O"," ","O"," "],
           ["P"," ","P"," ","P"," ","P"," ","E"," ","E"," ","E"," ","E"," ","E"," ","O"," ","O"," ","O"," ","O"],
           [" "," "," "," "," "," "," "," "," ","R"," ","R"," ","R"," ","R"," "," "," "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "," "," "," ","R"," ","R"," ","R"," "," "," "," "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "," "," "," "," ","R"," ","R"," "," "," "," "," "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "," "," "," "," "," ","R"," "," "," "," "," "," "," "," "," "," "," "," "]]
    for r in range(17):
        for c in range(25):
            if tab[r][c] == "G":
                create_circle(15+c*14, 15+r*20, 9, cantab,"green")
            if tab[r][c] == "B":
                create_circle(15+c*14, 15+r*20, 9, cantab, "blue")
            if tab[r][c] == "Y":
                create_circle(15+c*14, 15+r*20, 9, cantab, "yellow")
            if tab[r][c] =="P":
                create_circle(15+c*14, 15+r*20, 9, cantab,"purple")
            if tab[r][c] == "O":
                create_circle(15+c*14, 15+r*20, 9, cantab, "orange")
            if tab[r][c] =="R":
                create_circle(15+c*14, 15+r*20, 9, cantab,"red")
            if tab[r][c] =="E":
                create_circle(15+c*14, 15+r*20, 9, cantab,"gray")
            else:
                pass

def gamen():
    cantab.pack(ipadx=10, ipady=10)
    tablero()


# layout del inicio
img1_lab = tk.Label(canvas, image = img1, highlightbackground = 'white' ).grid(row = 0, column = 2)
lab1 = tk.Label(canvas, text = "Hola, Ingresa nombre de Usuario", highlightbackground = 'white', bg= "white")
lab1.grid(row= 1, columnspan = 3)
ent1 = tk.Entry(canvas,highlightbackground = 'white')
ent1.grid(row = 2, column = 2)
bot1 = tk.Button(canvas, text = "Continuar", command = menu, highlightbackground = 'white')
bot1.grid(row= 3, column = 2)

#layot de menu
canmen = tk.Canvas(frain2, width = 600,height = 500, bg = "white", highlightbackground = 'white')
bot2 = tk.Button(canmen, text= "Iniciar partida", highlightbackground = 'white',command = gamen)

bot3 = tk.Button(canmen, text="Instrucciones", highlightbackground = 'white')

bot4 =tk.Button(canmen, text="Salir del Juego", command = root.quit, highlightbackground = 'white')

#pantalla game
cantab = tk.Canvas(root, height=350, width=350)
def click(event):
    global CURRENT
    if cantab.find_withtag(CURRENT):

        print(CURRENT)
        cantab.itemconfig(CURRENT, fill="blue")
        #cantab.move(CURRENT, event.x,event.y)
        cantab.update_idletasks()
        cantab.after(200)
        cantab.itemconfig(CURRENT, fill="red")

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
cantab.bind("<Button-1>", click)
root.mainloop()
