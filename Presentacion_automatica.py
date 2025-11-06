import tkinter as tk

def mostrar_datos():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    pasatiempo = entrada_pasatiempo.get()
    mensaje = f"Hola {nombre}, con {edad}, es un gran momento para aprender Python. Ademas {pasatiempo}, suena excelente como pasatiempo"
    etiqueta_resultado.config(text=mensaje)

#Ventana principal
ventana = tk.Tk()
ventana.title("Bienvenido Usuario")

#Etiquetas y campos de entrada

tk.Label(ventana, text="Nombre completo: ").pack()
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack()

tk.Label(ventana, text="Edad: ").pack()
entrada_edad = tk.Entry(ventana, width=30)
entrada_edad.pack()

tk.Label(ventana, text="Escribe tu pasatiempo: ").pack()
entrada_pasatiempo = tk.Entry(ventana, width=30)
entrada_pasatiempo.pack()

#Boton para mostrar datos
boton_mostrar = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_datos)
boton_mostrar.pack()

#Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
