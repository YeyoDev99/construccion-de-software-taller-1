def calcular_comisiones_concordia():
    id_vendedor = int(input("Ingrese el ID del vendedor: "))
    nombre_vendedor = input("Ingrese el nombre del vendedor: ")
    N = int(input("Ingrese la cantidad de ventas realizadas (N): "))
    
    comision_total = 0
    
    for i in range(N):
        precio_art = float(input(f"Precio del artículo {i + 1}: "))
        
        if precio_art <= 100000:
            comision_t = precio_art * 0.10
        else:
            comision_t = precio_art * 0.07
            
        comision_total += comision_t

    print(f"Vendedor: {nombre_vendedor} (ID: {id_vendedor})")
    print(f"Comisión total por las {N} ventas: {comision_total:.2f}")

if __name__ == "__main__":
    calcular_comisiones_concordia()