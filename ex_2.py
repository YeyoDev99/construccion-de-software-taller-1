# Yader Ibraldo Quiroga Torres - 20222020034

def obtener_entero_valido(mensaje, min_val=None, max_val=None):
    """Obtiene un entero válido del usuario con validación de rango."""
    while True:
        try:
            valor = int(input(mensaje))
            if min_val is not None and valor < min_val:
                print(f"Error: El valor debe ser mayor o igual a {min_val}")
                continue
            if max_val is not None and valor > max_val:
                print(f"Error: El valor debe ser menor o igual a {max_val}")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número entero válido")

def obtener_decimal_valido(mensaje, min_val=None):
    """Obtiene un número decimal válido del usuario."""
    while True:
        try:
            valor = float(input(mensaje))
            if min_val is not None and valor < min_val:
                print(f"Error: El valor debe ser mayor o igual a {min_val}")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número válido")

def procesar_fumigacion():
    try:
        Pedido_F = obtener_entero_valido("Ingrese la cantidad de pedidos: ", min_val=1)
    except Exception as e:
        print(f"Error al leer la cantidad de pedidos: {e}")
        return
    
    for i in range(Pedido_F):
        try:
            nom_granjero = input(f"Pedido {i+1} - Nombre del granjero: ").strip()
            if not nom_granjero:
                print("Error: El nombre no puede estar vacío")
                continue
                
            tipo_fum = obtener_entero_valido("Tipo de fumigación (1, 2, 3, 4): ", min_val=1, max_val=4)
            num_hect = obtener_decimal_valido("Número de hectáreas: ", min_val=0.01)
            
            if tipo_fum == 1:
                valor_total = num_hect * 10
            elif tipo_fum == 2:
                valor_total = num_hect * 15
            elif tipo_fum == 3:
                valor_total = num_hect * 20
            else:  # tipo_fum == 4
                valor_total = num_hect * 30
                
            if num_hect > 1000:
                valor_total = valor_total * 0.95
                
            if valor_total > 3000:
                excedente = valor_total - 3000
                valor_total = 3000 + (excedente * 0.90)
                
            print(f"Granjero: {nom_granjero}")
            print(f"Valor a pagar: {valor_total:.2f}\n")
        except Exception as e:
            print(f"Error al procesar pedido {i+1}: {e}\n")
            continue

if __name__ == "__main__":
    try:
        procesar_fumigacion()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")