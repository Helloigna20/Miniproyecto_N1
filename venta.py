import tkinter as tk
from tkinter import ttk # Importamos ttk para widgets más modernos y estilizados como Treeview
from tkinter import messagebox  # Para mostrar mensajes emergentes

def abrir_ventana_venta():

    productos= {
        "Pan blanco": {"precio": 1400.25, "stock": 10, "imagen": "./Assets/pan_blanco.png"},
        "Pan integral": {"precio": 2300, "stock": 6, "imagen": "./Assets/pan_integral.png"},
        "Fideos tallarín": {"precio": 1140, "stock": 20, "imagen": "./Assets/fideos_tallarin.png"},
        "Fideos codito": {"precio": 980.50, "stock": 15, "imagen": "./Assets/fideos_codito.png"},
        "Fideos tirabuzon": {"precio": 1200, "stock": 15, "imagen": "./Assets/fideos_tirabuzon.png"},
        "Arroz": {"precio": 1750, "stock": 20, "imagen": "./Assets/arroz.png"},
        "Leche entera": {"precio": 2500, "stock": 12, "imagen": "./Assets/leche_entera.png"},
        "Leche descremada": {"precio": 2750, "stock": 12, "imagen": "./Assets/leche_descremada.png"},
        "Queso cremoso (500 g)": {"precio": 5500, "stock": 10, "imagen": "./Assets/queso_cremoso.png"},
        "Yerba común": {"precio": 4500, "stock": 16, "imagen": "./Assets/yerba_comun.png"},
        "Yerba saborizada": {"precio": 2600, "stock": 14, "imagen": "./Assets/yerba_saborizada.png"},
        "Té": {"precio": 1000, "stock": 12, "imagen": "./Assets/te.png"},
        "Café instantaneo": {"precio": 6500, "stock": 8, "imagen": "./Assets/cafe_instantaneo.png"},
        "Azúcar": {"precio": 1200, "stock": 10, "imagen": "./Assets/azucar.png"},
        "Harina común": {"precio": 2300, "stock": 10, "imagen": "./Assets/harina_comun.png"},
        "Aceite de girasol": {"precio": 1300, "stock": 8, "imagen": "./Assets/aceite_girasol.png"},
        "Aceite de oliva": {"precio": 6500.30, "stock": 8, "imagen": "./Assets/aceite_oliva.png"},
        "Huevos blancos (doc)": {"precio": 4200, "stock": 8, "imagen": "./Assets/huevos.png"},
    }

    carrito = {}  #  Diccionario para almacenar productos en el carrito

    def actualizar_carrito():  # Función para actualizar el Listbox y total
        carrito_listbox.delete(0, tk.END)
        total = 0
        for nombre, cantidad in carrito.items():
            precio_unitario = productos[nombre]['precio']
            subtotal = precio_unitario * cantidad
            carrito_listbox.insert(tk.END, f"{nombre} x{cantidad} - ${subtotal:.2f}")
            total += subtotal
        total_label.config(text=f"Total: ${total:.2f}")

    def agregar_al_carrito(nombre):  # Función para agregar al carrito
        if int (productos[nombre]['stock']) > 0:
            carrito[nombre] = carrito.get(nombre, 0) + 1
            productos[nombre]['stock'] = int(productos[nombre]['stock']) - 1
            actualizar_carrito()
            actualizar_stock_labels()

    def quitar_del_carrito(nombre):  # Función para quitar del carrito
        if nombre in carrito and carrito[nombre] > 0:
            carrito[nombre] -= 1
            productos[nombre]['stock'] += 1
            if carrito[nombre] == 0:
                del carrito[nombre]
            actualizar_carrito()
            actualizar_stock_labels()

    def vaciar_carrito():  # Función para vaciar el carrito
        for nombre, cantidad in carrito.items():
            productos[nombre]['stock'] += cantidad
        carrito.clear()
        actualizar_carrito()
        actualizar_stock_labels()
        messagebox.showinfo("Carrito", "El carrito se ha vaciado con éxito")

    stock_labels = {}  # Almacena las referencias a los labels de stock
    
    def confirmar_compra():
        total_texto = total_label.cget("text") 

        try:
            # Quitamos el "Total: $" y si hubiera comas de miles
            total_str = total_texto.replace("Total: $", "").replace(",", "") 
            total_float = float(total_str)
        except ValueError:
            messagebox.showerror("Error", "No se pudo obtener el total de la compra.")
            return

        # Valida si el carrito está vacío
        if not carrito:
            messagebox.showwarning("Carrito Vacío", "No hay productos en el carrito para confirmar la compra.", parent=ventana_venta)
            return
        
        # Mostrar el cuadro de diálogo de confirmación
        confirmar = messagebox.askyesno("Confirmar Compra", f"El total de la compra es ${total_float:.2f}\n¿Desea confirmar la compra?", parent=ventana_venta)

        if confirmar:
            messagebox.showinfo("Compra Confirmada", "¡Compra realizada con éxito!", parent=ventana_venta)
            carrito.clear()
            actualizar_carrito()
            
        else:
            messagebox.showinfo("Compra Cancelada", "La compra ha sido cancelada.", parent=ventana_venta)


    def actualizar_stock_labels():  # Actualiza los labels de stock
        for nombre, label in stock_labels.items():
            label.config(text=f"Stock: {productos[nombre]['stock']}")

    ventana_venta = tk.Toplevel()
    ventana_venta.title("Venta - Organización de Elementos")
    ventana_venta.geometry("1200x600")
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

    # --- Contenido para frame_izquierda (Productos Disponibles) 
    frame_izquierda.grid_rowconfigure(0, weight=0) # Título no se expande
    frame_izquierda.grid_rowconfigure(1, weight=1) # Treeview de productos se expande
    frame_izquierda.grid_columnconfigure(0, weight=1)
    frame_izquierda.grid_columnconfigure(1, weight=0) # La columna del scrollbar no se expande, solo toma el ancho necesario

    tk.Label(frame_izquierda, text="Productos Disponibles", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=10, columnspan=2)

    #usamos frame para manejar las cards de los productos
    productos_frame = ttk.Frame(frame_izquierda)
    productos_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    productos_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)  # Hasta 4 por fila
    
    imagenes_ventas = {}

    fila = 0
    columna = 0

    for nombre, detalles in productos.items():
        ruta_imagen = detalles.get('imagen')


        if ruta_imagen:
            imagen = tk.PhotoImage(file=ruta_imagen).subsample(10, 10)
        else:
            print(f"No se puedo cargar la imagen {nombre} : {ruta_imagen}")
            imagen = tk.PhotoImage(file='./Assets/producto.png').subsample(10, 10)
    
        imagenes_ventas[nombre] = imagen
      
        card = tk.Frame(productos_frame, bd=2, relief="groove", padx=10, pady=10, bg="#ffffff")
        card.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
        
        img_label = tk.Label(card, image=imagenes_ventas[nombre], bg="#ffffff")
        img_label.pack()
        img_label.image = imagenes_ventas[nombre]

        tk.Label(card, text=nombre, font=("Arial", 12, "bold"), bg="#ffffff").pack()
        tk.Label(card, text=f"${detalles['precio']:.2f}", font=("Arial", 10), bg="#ffffff").pack()
        stock_label = tk.Label(card, text=f"Stock: {detalles['stock']}", font=("Arial", 10, "italic"), bg="#ffffff")
        stock_label.pack()
        stock_labels[nombre] = stock_label  # Almacenar la referencia
        
       
        # Frame para agrupar los botones + y -
        botones_frame = tk.Frame(card, bg="#e0f7fa")
        botones_frame.pack(pady=5)
        tk.Button(botones_frame, text="+", width=3, bg="#b2ebf2", command=lambda n=nombre: agregar_al_carrito(n)).pack(side="left", padx=2)
        tk.Button(botones_frame, text="-", width=3, bg="#ffcdd2", command=lambda n=nombre: quitar_del_carrito(n)).pack(side="left", padx=2)

        columna += 1
        if columna > 3:  # 4 columnas
            columna = 0
            fila += 1

    # Evita que la imagen desaparezca
    productos_frame.image = imagen

    # Contenido para frame_derecha_arriba (El Carrito Actual) 
    frame_derecha_arriba.grid_rowconfigure(0, weight=0)
    frame_derecha_arriba.grid_rowconfigure(1, weight=1)
    frame_derecha_arriba.grid_columnconfigure(0, weight=1)

    tk.Label(frame_derecha_arriba, text="Tu Carrito", font=("Arial", 14, "bold")).grid(row=0, column=0, pady=5)

    carrito_listbox = tk.Listbox(frame_derecha_arriba)
    carrito_listbox.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    # Contenido para frame_derecha_abajo (Resumen de Compra)
    frame_derecha_abajo.grid_rowconfigure(0, weight=0)
    frame_derecha_abajo.grid_rowconfigure(1, weight=1) # Placeholder para el total
    frame_derecha_abajo.grid_columnconfigure(0, weight=1)

    tk.Label(frame_derecha_abajo, text="Resumen de Compra", font=("Arial", 14, "bold")).grid(row=0, column=0, pady=5)

    total_label = tk.Label(frame_derecha_abajo, text="Total: $0.00", font=("Arial", 12))
    total_label.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    tk.Button(frame_derecha_abajo, text="Realizar Compra", command=confirmar_compra).grid(row=2, column=0, pady=5)
    tk.Button(frame_derecha_abajo, text="Vaciar Carrito", command=vaciar_carrito).grid(row=3, column=0, pady=5)
