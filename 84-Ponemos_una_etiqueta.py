import tkinter as tk

ventana = tk.Tk()

def accion():
    print("Presionaste el boton, chamo.")

tk.Button(ventana,text="Pulsame chamo",command=accion).pack(padx=10,pady=10)

etiqueta = tk.Label(text="¿Has pulsado el boton, chamo?")
etiqueta.pack(padx=10,pady=10)

ventana.mainloop() #no te salgas de tkinter