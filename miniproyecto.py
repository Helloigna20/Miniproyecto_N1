import tkinter as tk

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
Inicio.add_command(label="Venta")
Inicio.add_command(label="Salir", command=ventana_inicio.destroy)

Stock = tk.Menu(menu_barra, tearoff=0)


Ayuda = tk.Menu(menu_barra, tearoff=0)
Ayuda.add_command(label="Contacto")
Ayuda.add_command(label="Sobre nosotros")



menu_barra.add_cascade(label="Inicio", menu=Inicio)
menu_barra.add_cascade(label="Stock", menu=Stock)
menu_barra.add_cascade(label="Ayuda", menu=Ayuda)

ventana_inicio.config(menu=menu_barra)


ventana_inicio.mainloop()