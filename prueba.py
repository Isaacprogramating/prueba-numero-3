import json

# Definir los menús disponibles
menus = ["Comida Italiana", "Comida Japonesa", "BBQ"]

# Lista para almacenar los pedidos
pedidos = []

# Función para validar la entrada del usuario
def validar_entrada(prompt, tipo=str):
    while True:
        entrada = input(prompt)
        if tipo == int:
            try:
                return int(entrada)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif tipo == str:
            if entrada.strip():
                return entrada
            else:
                print("Por favor, ingrese un texto válido.")

# Función para registrar un pedido
def registrar_pedido():
    nombre = validar_entrada("Nombre y apellido del cliente: ")
    contacto = validar_entrada("Número de contacto: ")
    tipo_evento = validar_entrada("Tipo de evento: ")
    fecha = validar_entrada("Fecha del evento (DD/MM/AAAA): ")
    direccion = validar_entrada("Dirección del evento: ")
    
    print("Seleccione el menú:")
    for i, menu in enumerate(menus, 1):
        print(f"{i}. {menu}")
    
    menu_seleccionado = validar_entrada("Ingrese el número del menú seleccionado: ", int)
    if 1 <= menu_seleccionado <= len(menus):
        menu_seleccionado = menus[menu_seleccionado - 1]
    else:
        print("Selección inválida. Intente nuevamente.")
        return
    
    cantidad_comensales = validar_entrada("Cantidad de comensales: ", int)
    
    pedido = {
        "nombre": nombre,
        "contacto": contacto,
        "tipo_evento": tipo_evento,
        "fecha": fecha,
        "direccion": direccion,
        "menu": menu_seleccionado,
        "cantidad_comensales": cantidad_comensales
    }
    
    pedidos.append(pedido)
    print("Pedido registrado exitosamente.")

# Función para listar todos los pedidos
def listar_pedidos():
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    
    for i, pedido in enumerate(pedidos, 1):
        print(f"Pedido {i}:")
        for key, value in pedido.items():
            print(f"  {key.capitalize()}: {value}")
        print()

# Función para imprimir detalles de pedidos por menú y generar archivos
def imprimir_detalle_pedidos_por_menu():
    print("Seleccione el menú para generar el detalle de pedidos:")
    for i, menu in enumerate(menus, 1):
        print(f"{i}. {menu}")
    
    menu_seleccionado = validar_entrada("Ingrese el número del menú seleccionado: ", int)
    if 1 <= menu_seleccionado <= len(menus):
        menu_seleccionado = menus[menu_seleccionado - 1]
    else:
        print("Selección inválida. Intente nuevamente.")
        return
    
    pedidos_filtrados = [pedido for pedido in pedidos if pedido["menu"] == menu_seleccionado]
    
    if not pedidos_filtrados:
        print(f"No hay pedidos registrados para el menú {menu_seleccionado}.")
        return
    
    # Generar archivo .txt
    with open(f"pedidos_{menu_seleccionado}.txt", "w") as file:
        for pedido in pedidos_filtrados:
            for key, value in pedido.items():
                file.write(f"{key.capitalize()}: {value}\n")
            file.write("\n")
    
    # Generar archivo .json
    with open(f"pedidos_{menu_seleccionado}.json", "w") as file:
        json.dump(pedidos_filtrados, file, indent=4)
    
    print(f"Detalles de pedidos para el menú {menu_seleccionado} generados exitosamente.")

# Función principal del programa
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Pedido")
        print("2. Listar Pedidos")
        print("3. Imprimir Detalle de Pedidos por Menú")
        print("4. Salir")
        
        opcion = validar_entrada("Seleccione una opción: ", int)
        
        if opcion == 1:
            registrar_pedido()
        elif opcion == 2:
            listar_pedidos()
        elif opcion == 3:
            imprimir_detalle_pedidos_por_menu()
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
