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

def obtener_ano_valido(mensaje, ano_minimo=1900, ano_maximo=2024):
    """Obtiene un año válido del usuario."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < ano_minimo or valor > ano_maximo:
                print(f"Error: Ingrese un año entre {ano_minimo} y {ano_maximo}")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número entero válido")

def obtener_fecha_valida(mensaje):
    """Obtiene una fecha válida en formato DD/MM/AAAA."""
    while True:
        try:
            fecha = input(mensaje).strip()
            partes = fecha.split('/')
            if len(partes) != 3:
                print("Error: Ingrese la fecha en formato DD/MM/AAAA")
                continue
            dia, mes, ano = map(int, partes)
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2024):
                print("Error: Fecha inválida")
                continue
            return fecha
        except ValueError:
            print("Error: Ingrese una fecha válida en formato DD/MM/AAAA")

def obtener_opcion_valida(mensaje, opciones_validas):
    """Obtiene una opción válida del usuario."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor not in opciones_validas:
                print(f"Error: Ingrese una de las opciones válidas: {opciones_validas}")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número entero válido")

def procesar_accidentes_medellin():
    try:
        ATM_n = obtener_entero_positivo("Ingrese la cantidad de conductores involucrados en accidentes: ")
        
        total_conductores = ATM_n
        cont_menores_25 = 0
        cont_femenino = 0
        cont_masc_12_30 = 0
        cont_fuera_medellin = 0
        
        anio_actual = 2024

        for i in range(ATM_n):
            try:
                print(f"\nConductor {i + 1}:")
                identificación = obtener_entero_positivo("Identificación del conductor: ")
                fecha_acc = obtener_fecha_valida("Fecha del accidente (DD/MM/AAAA): ")
                ubicación = input("Ubicación del accidente: ").strip()
                if not ubicación:
                    print("Error: La ubicación no puede estar vacía")
                    continue
                
                anio_nac_cond = obtener_ano_valido("Año de nacimiento del conductor: ", ano_minimo=1900)
                sexo_cond = obtener_opcion_valida("Sexo (1: Femenino, 2: Masculino): ", [1, 2])
                
                placa = input("Placa del carro: ").strip().upper()
                if not placa:
                    print("Error: La placa no puede estar vacía")
                    continue
                registro = obtener_opcion_valida("Registro del carro (1: Medellín, 2: Otras ciudades): ", [1, 2])
                
                edad_cond = anio_actual - anio_nac_cond
                
                # Validar que la edad sea razonable
                if edad_cond < 16 or edad_cond > 100:
                    print(f"Advertencia: Edad calculada inusual ({edad_cond} años)")
                
                if edad_cond < 25:
                    cont_menores_25 += 1
                    
                if sexo_cond == 1:
                    cont_femenino += 1
                    
                if sexo_cond == 2 and 12 <= edad_cond <= 30:
                    cont_masc_12_30 += 1
                    
                if registro == 2:
                    cont_fuera_medellin += 1
            except Exception as e:
                print(f"Error al procesar conductor {i + 1}: {e}")
                continue

        if total_conductores == 0:
            print("\nError: No se procesaron conductores válidos")
            return

        porc_menores_25 = (cont_menores_25 / total_conductores) * 100 if total_conductores > 0 else 0
        porc_femenino = (cont_femenino / total_conductores) * 100 if total_conductores > 0 else 0
        porc_masc_12_30 = (cont_masc_12_30 / total_conductores) * 100 if total_conductores > 0 else 0
        porc_fuera_medellin = (cont_fuera_medellin / total_conductores) * 100 if total_conductores > 0 else 0

        print("\n=== RESULTADOS ===")
        print(f"Porcentaje de conductores menores de 25 años: {porc_menores_25:.2f}%")
        print(f"Porcentaje de conductores del sexo femenino: {porc_femenino:.2f}%")
        print(f"Porcentaje de conductores masculinos entre 12 y 30 años: {porc_masc_12_30:.2f}%")
        print(f"Porcentaje de conductores con carros registrados fuera de Medellín: {porc_fuera_medellin:.2f}%")
    except Exception as e:
        print(f"Error al procesar accidentes: {e}")

if __name__ == "__main__":
    try:
        procesar_accidentes_medellin()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")