from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Proyecto ML Damas chinas - PUJ')
root.geometry('500x500')
root.resizable(0, 0)
# ocultar todos los frames
def half():
    fra1.pack_forget()
    fra3.pack_forget()
#iniciar frames de menu
def contin1 ():
    test = Label(fra3, text = "Hola " + ent1.get())
    half()
    test.pack()
    fra3.pack()
#iniciar instrucciones
def inst():
    fra1.pack_forget()
    fra3.pack_forget()
    fra2.pack(fill = BOTH, expand = 1)
    my_canvas = Canvas(fra2)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scroll = ttk.Scrollbar(fra2, orient=VERTICAL, command=my_canvas.yview)
    my_scroll.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scroll.set)
    my_canvas.bind('<configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))
    fra2a1 = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=fra2a1, anchor='nw')

    bot2 = Button(fra2a1, text="Iniciar partida")
    bot2.pack()
    bot3 = Button(fra2a1, text="Acerca de", command=contin1)
    bot3.pack()
    bot4 = Button(fra2a1, text="Instrucciones", command=contin1)
    bot4.pack()
    bot4 = Button(fra2a1, text="Salir", command=contin1)
    bot4.pack()


# frame de inicio
fra1 = Frame(root, width = 500, height = 500)
img1 = PhotoImage(file = "/Users/junkal/Documents/Machine Learning /Proyecto Damas/ima.gif")
Label(fra1, image = img1).pack(fill = X)
lab1 = Label(fra1, text = "Hola, Bienvenido al mejor jueo de damas chinas, ¿Cual es su nombre?  ")
lab1.pack(fill = X)
ent1 = Entry(fra1,bg = 'grey')
ent1.pack()
bot1 = Button(fra1, text = "continuar", command = contin1)
bot1.pack()
fra1.pack()
# menu del juego (instrucciones)
fra3 = Frame(root, width = 500, height = 500)
bot2 = Button(fra3, text="Iniciar partida")
bot2.pack()
bot3 = Button(fra3, text="Acerca de", command=contin1)
bot3.pack()
bot4 = Button(fra3, text="Instrucciones", command= inst)
bot4.pack()
bot4 = Button(fra3, text="Salir", command=contin1)
bot4.pack()
fra2 = Frame(root)

root.mainloop()