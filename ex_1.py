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

def procesar_estudiantes():
    try:
        EST_n = obtener_entero_valido("Ingrese la cantidad de estudiantes (N): ", min_val=1)
    except Exception as e:
        print(f"Error al leer la cantidad de estudiantes: {e}")
        return
    
    suma_edad_cont = 0
    cant_cont = 0
    cant_hom_ing = 0
    cant_muj_menor_20 = 0
    suma_edad_muj_ing = 0
    cant_muj_ing = 0
    cant_hom_der_noc = 0
    
    for i in range(EST_n):
        try:
            edad_est = obtener_entero_valido(f"Estudiante {i+1} - Edad: ", min_val=1, max_val=80)
            sexo_est = obtener_entero_valido("Sexo (1. Masculino; 2. Femenino): ", min_val=1, max_val=2)
            carrera_est = obtener_entero_valido("Carrera (1. Ingeniería; 2. Contaduría; 3. Derecho; 4. Otra): ", min_val=1, max_val=4)
            jornada_est = obtener_entero_valido("Jornada (1. Diurna; 2. Nocturna): ", min_val=1, max_val=2)
        except Exception as e:
            print(f"Error al procesar datos del estudiante {i+1}: {e}")
            continue
            
            if carrera_est == 2:
                suma_edad_cont += edad_est
                cant_cont += 1
                
            if sexo_est == 1 and carrera_est == 1:
                cant_hom_ing += 1
                
            if sexo_est == 2 and edad_est < 20:
                cant_muj_menor_20 += 1
                
            if sexo_est == 2 and carrera_est == 1:
                suma_edad_muj_ing += edad_est
                cant_muj_ing += 1
                
            if sexo_est == 1 and edad_est > 22 and carrera_est == 3 and jornada_est == 2:
                cant_hom_der_noc += 1
        except ValueError:
            print(f"Error: Datos inválidos para el estudiante {i+1}. Saltando...")
            continue

    if EST_n == 0:
        print("Error: No se procesaron estudiantes válidos")
        return

    try:
        prom_edad_cont = (suma_edad_cont / cant_cont) if cant_cont > 0 else 0
        prom_edad_muj_ing = (suma_edad_muj_ing / cant_muj_ing) if cant_muj_ing > 0 else 0
        
        porc_hom_ing = (cant_hom_ing / EST_n) * 100 if EST_n > 0 else 0
        porc_muj_menor_20 = (cant_muj_menor_20 / EST_n) * 100 if EST_n > 0 else 0
        porc_hom_der_noc = (cant_hom_der_noc / EST_n) * 100 if EST_n > 0 else 0

        print(f"a) Promedio de edad estudiantes de Contaduría: {prom_edad_cont:.2f}")
        print(f"b) Porcentaje de hombres en Ingeniería: {porc_hom_ing:.2f}%")
        print(f"c) Porcentaje de mujeres menores a 20 años: {porc_muj_menor_20:.2f}%")
        print(f"d) Promedio de edad mujeres en Ingeniería: {prom_edad_muj_ing:.2f}")
        print(f"e) Porcentaje hombres > 22 años en Derecho nocturno: {porc_hom_der_noc:.2f}%")
    except Exception as e:
        print(f"Error al calcular resultados: {e}")

if __name__ == "__main__":
    try:
        procesar_estudiantes()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")