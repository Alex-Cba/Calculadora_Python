#Haciendo una calculadora
#Lambda sirve para que sea funcion anonimas, es decir que no guarda lo que coloco en las variables de forma automatica, porque python cuando le doy un valor a una variable python lo va aguardar

from tkinter import *

raiz=Tk()
raiz.title("Calculadora by Alex")
miFrame=Frame(raiz)
miFrame.pack()

indice=0

#-------------------------------------Pantalla----------------------

#numeroPantalla=StringVar() #<-pasa todo como cadena de caracteres no sirve para el eval

pantalla=Entry(miFrame)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #Le digo al widgeth de la pantalla que se expanda en 4 por que la calculadora en su primera fila tiene 4 columnas
pantalla.config(background="black", fg="#03f943", justify="left")

#----------------------Codigo de botones----------------------

def numeropulsado(num): #Esto va a servir para que cuando la persona pulse el boton le llegue de esa pulsacion el parametro a la def, entonces no tengo que hacer 50 def para cada boton, sino que le paso el numero desde el boton, entonces con al funcion get lo va sumando, pero da un error que se soluciona con lambda
    global indice

    pantalla.insert(indice,num)
    indice+=1

def borrado():
    pantalla.delete(0, END)
    indice=0

def operacion():

    ecuacion= pantalla.get()
    resultado= eval(ecuacion)

    pantalla.delete(0,END)
    pantalla.insert(0, resultado)

    indice = 0


#------------------------Fila de numero primera---------------------

botonAC=Button(miFrame, text="AC", width=3, command=lambda:borrado())
botonAC.grid(row=2, column=1)
botonizqparen=Button(miFrame, text="(", width=3, command=lambda:numeropulsado("("))
botonizqparen.grid(row=2, column=2)
botonderparen=Button(miFrame, text=")", width=3, command=lambda:numeropulsado(")"))
botonderparen.grid(row=2, column=3)
botondiv=Button(miFrame, text="/", width=3, command=lambda:numeropulsado("/"))
botondiv.grid(row=2, column=4)

#------------------------Fila de numero segunda---------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeropulsado(7))
boton7.grid(row=3, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeropulsado(8))
boton8.grid(row=3, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeropulsado(9))
boton9.grid(row=3, column=3)
botonmul=Button(miFrame, text="*", width=3, command=lambda:numeropulsado("*"))
botonmul.grid(row=3, column=4)

#------------------------Fila de numero tercera---------------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeropulsado(4))
boton4.grid(row=4, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeropulsado(5))
boton5.grid(row=4, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeropulsado(6))
boton6.grid(row=4, column=3)
botonrestar=Button(miFrame, text="-", width=3, command=lambda:numeropulsado("-"))
botonrestar.grid(row=4, column=4)

#------------------------Fila de numero cuarta---------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeropulsado(1))
boton1.grid(row=5, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeropulsado(2))
boton2.grid(row=5, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeropulsado(3))
boton3.grid(row=5, column=3)
botonsuma=Button(miFrame, text="+", width=3, command=lambda:numeropulsado("+"))
botonsuma.grid(row=5, column=4)

#------------------------Fila de numero quinta---------------------

boton0=Button(miFrame, text="0", width=8, command=lambda:numeropulsado(0))
boton0.grid(row=6, column=1, columnspan=2)
botoncoma=Button(miFrame, text=",", width=3, command=lambda:numeropulsado(","))
botoncoma.grid(row=6, column=3)
botonigual=Button(miFrame, text="=", width=3, command=lambda:operacion())
botonigual.grid(row=6, column=4)


raiz.mainloop()