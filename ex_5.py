# Yader Ibraldo Quiroga Torres - 20222020034

def obtener_entero_positivo(mensaje):
    """Obtiene un entero positivo válido del usuario."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Error: Ingrese un número positivo")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número entero válido")

def obtener_decimal_positivo(mensaje):
    """Obtiene un número decimal positivo válido del usuario."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Error: Ingrese un número positivo")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número válido")

def calcular_comisiones_concordia():
    try:
        id_vendedor = obtener_entero_positivo("Ingrese el ID del vendedor: ")
        nombre_vendedor = input("Ingrese el nombre del vendedor: ").strip()
        if not nombre_vendedor:
            print("Error: El nombre no puede estar vacío")
            return
        N = obtener_entero_positivo("Ingrese la cantidad de ventas realizadas (N): ")
        
        comision_total = 0
        
        for i in range(N):
            try:
                precio_art = obtener_decimal_positivo(f"Precio del artículo {i + 1}: ")
                
                if precio_art <= 100000:
                    comision_t = precio_art * 0.10
                else:
                    comision_t = precio_art * 0.07
                    
                comision_total += comision_t
            except Exception as e:
                print(f"Error al procesar artículo {i + 1}: {e}")
                continue

        print(f"Vendedor: {nombre_vendedor} (ID: {id_vendedor})")
        print(f"Comisión total por las {N} ventas: {comision_total:.2f}")
    except Exception as e:
        print(f"Error al calcular comisiones: {e}")

if __name__ == "__main__":
    try:
        calcular_comisiones_concordia()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")