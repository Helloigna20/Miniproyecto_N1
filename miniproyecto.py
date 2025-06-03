import tkinter as tk

#Config. de ventana
ventana = tk.Tk()
ventana.geometry("600x600")
ventana.config(bg="NavajoWhite2")
ventana.attributes("-alpha",0.95)
ventana.title("Proyecto")
ventana.iconbitmap("Assets\Carrito.ico")

menu_barra = tk.Menu(ventana)



submenu = tk.Menu(menu_barra, tearoff=0)
submenu.add_command(label="Carrito")
submenu.add_command(label="Ventas")
submenu.add_separator()

Opciones_menu = tk.Menu(submenu, tearoff=0)
Opciones_menu.add_command(label="Apariencia")
Opciones_menu.add_command(label="Contacto")

submenu.add_cascade(label="Opciones", menu=Opciones_menu)


menu_barra.add_cascade(label="Principal", menu=submenu)

ventana.config(menu=menu_barra)

ventana.mainloop()