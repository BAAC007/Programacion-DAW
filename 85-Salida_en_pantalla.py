import tkinter as tk

ventana = tk.Tk()

def accion():
    etiqueta.config(text="Pues si que has pulsado el boton, chamo")

acciona = accion()

def sobreaccion():
    if acciona == 5:
        etiqueta.config(text="Deja la vaina, chamo")

tk.Button(ventana,text="Pulsame chamo",command=accion).pack(padx=10,pady=10)

etiqueta = tk.Label(text="¿Has pulsado el boton, chamo?")
etiqueta.pack(padx=10,pady=10)

ventana.mainloop() #no te salgas de tkinter