
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

def obtener_sexo_valido():
    """Obtiene un sexo válido del usuario."""
    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ['M', 'F']:
            return sexo
        print("Error: Ingrese M o F")

def obtener_opcion_valida(mensaje, minimo, maximo):
    """Obtiene una opción válida en un rango."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo or valor > maximo:
                print(f"Error: Ingrese un número entre {minimo} y {maximo}")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número entero válido")

def procesar_registro_clientes():
    try:
        Cliente_Reg = obtener_entero_positivo("Ingrese la cantidad de clientes a registrar: ")
        
        lista_mujeres_filtro = []
        lista_hombres_filtro = []
        
        for i in range(Cliente_Reg):
            try:
                print(f"\nCliente {i+1}:")
                nombre_cl = input("Nombre: ").strip()
                if not nombre_cl:
                    print("Error: El nombre no puede estar vacío")
                    continue
                    
                sexo_cl = obtener_sexo_valido()
                edad_cl = obtener_entero_positivo("Edad: ")
                
                if edad_cl < 1 or edad_cl > 120:
                    print("Advertencia: Edad inusual")
                    
                altura_cl = obtener_decimal_positivo("Altura (metros): ")
                
                if altura_cl < 1.0 or altura_cl > 2.5:
                    print("Advertencia: Altura inusual")
                    
                peso_cl = obtener_decimal_positivo("Peso (libras): ")
                
                if peso_cl < 50 or peso_cl > 500:
                    print("Advertencia: Peso inusual")
                    
                color_ojos = obtener_opcion_valida("Color ojos (1: Azules, 2: Castaños, 3: Otros): ", 1, 3)
                color_cabello = obtener_opcion_valida("Color cabello (1: Castaño, 2: Rubio, 3: Otros): ", 1, 3)
                
                if sexo_cl.upper() == 'F':
                    if color_cabello == 2 and color_ojos == 1:
                        if 1.65 <= altura_cl <= 1.75 and peso_cl < 120:
                            lista_mujeres_filtro.append(nombre_cl)
                
                elif sexo_cl.upper() == 'M':
                    if color_ojos == 2 and altura_cl > 1.70:
                        if 180 <= peso_cl <= 220:
                            lista_hombres_filtro.append(nombre_cl)
            except Exception as e:
                print(f"Error al procesar cliente {i+1}: {e}")
                continue

        print("\na) Mujeres rubias, ojos azules (1.65-1.75m, <120lb):")
        if lista_mujeres_filtro:
            for nombre in lista_mujeres_filtro:
                print(f"  - {nombre}")
        else:
            print("  No hay coincidencias")
            
        print("\nb) Hombres ojos castaños (>1.70m, 180-220lb):")
        if lista_hombres_filtro:
            for nombre in lista_hombres_filtro:
                print(f"  - {nombre}")
        else:
            print("  No hay coincidencias")
    except Exception as e:
        print(f"Error al procesar registro de clientes: {e}")

if __name__ == "__main__":
    try:
        procesar_registro_clientes()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")