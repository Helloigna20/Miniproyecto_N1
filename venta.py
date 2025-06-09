import tkinter as tk
from tkinter import ttk # Importamos ttk para widgets más modernos y estilizados como Treeview

def abrir_ventana_venta(productos):
    ventana_venta = tk.Toplevel()
    ventana_venta.title("Venta - Organización de Elementos")
    ventana_venta.geometry("1024x900")
    ventana_venta.iconbitmap("Assets/Carrito.ico") # Aca también agregamos el icono.

    # Configuración del menú
    menu_barra = tk.Menu(ventana_venta)
    ventana_venta.config(menu=menu_barra)
    menu_inicio = tk.Menu(menu_barra, tearoff=0)
    menu_barra.add_cascade(label="Inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Volver a Inicio", command=ventana_venta.destroy)

    # Configuración de grid para la ventana principal
    ventana_venta.grid_rowconfigure(0, weight=1)
    ventana_venta.grid_columnconfigure(0, weight=2) # Columna izquierda más ancha para productos
    ventana_venta.grid_columnconfigure(1, weight=1) # Columna derecha para el carrito

    # Frames principales (izquierda y derecha)
    frame_izquierda = tk.Frame(ventana_venta, bd=2, relief="groove")
    frame_izquierda.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) # Se expande en todas direcciones en su celda

    frame_derecha = tk.Frame(ventana_venta, bd=2, relief="groove")
    frame_derecha.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Configuración de grid para el frame_derecha
    frame_derecha.grid_rowconfigure(0, weight=3) # Para el carrito
    frame_derecha.grid_rowconfigure(1, weight=0, minsize=5) # Separador (ajustado ligeramente para un mejor tamaño)
    frame_derecha.grid_rowconfigure(2, weight=1) # Para el resumen
    frame_derecha.grid_columnconfigure(0, weight=1)

    # Sub-frames dentro de frame_derecha
    frame_derecha_arriba = tk.Frame(frame_derecha, bd=2, relief="solid")
    frame_derecha_arriba.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    separator_frame = tk.Frame(frame_derecha, height=5, bg="gray", bd=0) # Altura del separador
    separator_frame.grid(row=1, column=0, sticky="ew", padx=5)

    frame_derecha_abajo = tk.Frame(frame_derecha, bd=2, relief="solid")
    frame_derecha_abajo.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    # --- Contenido para frame_izquierda (Productos Disponibles) ---
    frame_izquierda.grid_rowconfigure(0, weight=0) # Título no se expande
    frame_izquierda.grid_rowconfigure(1, weight=1) # Treeview de productos se expande
    frame_izquierda.grid_columnconfigure(0, weight=1)
    frame_izquierda.grid_columnconfigure(1, weight=0) # La columna del scrollbar no se expande, solo toma el ancho necesario

    tk.Label(frame_izquierda, text="Productos Disponibles", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=10, columnspan=2)

    # Usamos un Treeview para mostrar los productos de manera tabular
    # Se ajusta al tamaño de la celda donde está contenido
    productos_tree = ttk.Treeview(frame_izquierda, columns=("ProductoNombre", "Precio", "Stock"), show="headings", height=10)
    productos_tree.grid(row=1, column=0, sticky="nsew", padx=(10,0), pady=10 )

    # Define el encabezado de la columna principal
    productos_tree.heading("#0", text="Producto")
    productos_tree.column("#0", width=250, anchor="w", stretch=tk.YES)

    # Definir encabezados de columnas
    productos_tree.heading("ProductoNombre", text="Producto")
    productos_tree.heading("Precio", text="Precio")
    productos_tree.heading("Stock", text="Stock")

    # Configurar el ancho de las columnas 
    productos_tree.column("ProductoNombre", width=250, anchor="w", stretch=tk.YES)
    productos_tree.column("Precio", width=100, anchor="center")
    productos_tree.column("Stock", width=80, anchor="center")


    # Barra de desplazamiento para el Treeview
    scrollbar = ttk.Scrollbar(frame_izquierda, orient="vertical", command=productos_tree.yview)
    scrollbar.grid(row=1, column=1, sticky="ns", padx=(0,10)) # Colocado al lado derecho del Treeview
    productos_tree.configure(yscrollcommand=scrollbar.set)

    # Rellenar el Treeview con los productos del diccionario
    if productos:
        for nombre, detalles in productos.items():
            precio = detalles.get("precio", "N/A")
            stock = detalles.get("stock", "N/A")

            productos_tree.insert("", "end", values=(nombre, f"${precio:.2f}", stock))
    else:
        # Si no hay productos, puedes insertar un mensaje o deshabilitar el Treeview
        productos_tree.insert("", "end", values=("No hay productos para mostrar", "", ""))

    # Contenido para frame_derecha_arriba (El Carrito Actual) 
    frame_derecha_arriba.grid_rowconfigure(0, weight=0)
    frame_derecha_arriba.grid_rowconfigure(1, weight=1)
    frame_derecha_arriba.grid_columnconfigure(0, weight=1)

    tk.Label(frame_derecha_arriba, text="Tu Carrito", font=("Arial", 14, "bold")).grid(row=0, column=0, pady=5)

    # Placeholder para el carrito real (podría ser otro Treeview o un Listbox)
    carrito_listbox = tk.Listbox(frame_derecha_arriba)
    carrito_listbox.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    carrito_listbox.insert(tk.END, "El carrito estará aquí...") # Mensaje inicial

    # Contenido para frame_derecha_abajo (Resumen de Compra)
    frame_derecha_abajo.grid_rowconfigure(0, weight=0)
    frame_derecha_abajo.grid_rowconfigure(1, weight=1) # Placeholder para el total
    frame_derecha_abajo.grid_columnconfigure(0, weight=1)

    tk.Label(frame_derecha_abajo, text="Resumen de Compra", font=("Arial", 14, "bold")).grid(row=0, column=0, pady=5)

    # Placeholder para el total y botones de acción
    total_label = tk.Label(frame_derecha_abajo, text="Total: $0.00", font=("Arial", 12))
    total_label.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    tk.Button(frame_derecha_abajo, text="Realizar Compra").grid(row=2, column=0, pady=5)
    tk.Button(frame_derecha_abajo, text="Vaciar Carrito").grid(row=3, column=0, pady=5)