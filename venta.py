import tkinter as tk

def abrir_ventana_venta():
    ventana_venta = tk.Toplevel()
    ventana_venta.title("Venta - Organización de Elementos")
    ventana_venta.geometry("1024x900") 

  
    menu_barra = tk.Menu(ventana_venta)
    ventana_venta.config(menu=menu_barra) 
    menu_inicio = tk.Menu(menu_barra, tearoff=0)
    menu_barra.add_cascade(label="Inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Volver a Inicio", command=ventana_venta.destroy)
    
    ventana_venta.grid_rowconfigure(0, weight=1) 
    ventana_venta.grid_columnconfigure(0, weight=2) 
    ventana_venta.grid_columnconfigure(1, weight=1) 

    
    frame_izquierda = tk.Frame(ventana_venta, bd=2, relief="groove") 
    frame_izquierda.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) # Se expande en todas direcciones en su celda

    frame_derecha = tk.Frame(ventana_venta, bd=2, relief="groove") 
    frame_derecha.grid(row=0, column=1, sticky="nsew", padx=10, pady=10) 

    frame_derecha.grid_rowconfigure(0, weight=3) 
    frame_derecha.grid_rowconfigure(1, weight=0, minsize=3) 
    frame_derecha.grid_rowconfigure(2, weight=1) 
    frame_derecha.grid_columnconfigure(0, weight=1) 

    frame_derecha_arriba = tk.Frame(frame_derecha, bd=2, relief="solid")
    frame_derecha_arriba.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    separator_frame = tk.Frame(frame_derecha, height=3, bg="gray", bd=0) 
    separator_frame.grid(row=1, column=0, sticky="ew", padx=5) 

    frame_derecha_abajo = tk.Frame(frame_derecha, bd=2, relief="solid")
    frame_derecha_abajo.grid(row=2, column=0, sticky="nsew", padx=5, pady=5) 
