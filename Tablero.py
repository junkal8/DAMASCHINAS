from tkinter import *
root = Tk()
cantab = Canvas(root, height =350, width=350)
cantab.pack(ipadx=10,ipady=10)

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

"""""""""
Funcion quecambia el color de los objetos cuando del usuario da clck
"""""""""
def click(event):
    if cantab.find_withtag(CURRENT):
        print(CURRENT)
        cantab.itemconfig(CURRENT, fill="blue")
        cantab.update_idletasks()
        cantab.after(200)
        cantab.itemconfig(CURRENT, fill="red")

tablero()

cantab.bind("<Button-1>", click)

root.mainloop()
