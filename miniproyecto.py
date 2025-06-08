import tkinter as tk
from venta import abrir_ventana_venta


#Config. de ventana
ventana_inicio = tk.Tk()
ventana_inicio.geometry("600x600")
ventana_inicio.attributes("-alpha",0.95)
ventana_inicio.title("Proyecto")
ventana_inicio.iconbitmap("Assets/Carrito.ico")
Imagen = tk.PhotoImage(file="Assets/Fondo.png")
Fondo = tk.Label(ventana_inicio, image=Imagen)
Fondo.place(x=0, y=0, relwidth=1, relheight=1)

#Config. del menu
menu_barra = tk.Menu(ventana_inicio)

Inicio = tk.Menu(menu_barra, tearoff=0)
Inicio.add_command(label="Carrito", command=abrir_ventana_venta)
Inicio.add_command(label="Salir", command=ventana_inicio.destroy)

menu_barra.add_cascade(label="Inicio", menu=Inicio)

ventana_inicio.config(menu=menu_barra)


ventana_inicio.mainloop()