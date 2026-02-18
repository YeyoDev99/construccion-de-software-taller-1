def procesar_estudiantes():
    EST_n = int(input("Ingrese la cantidad de estudiantes (N): "))
    
    suma_edad_cont = 0
    cant_cont = 0
    cant_hom_ing = 0
    cant_muj_menor_20 = 0
    suma_edad_muj_ing = 0
    cant_muj_ing = 0
    cant_hom_der_noc = 0
    
    for i in range(EST_n):
        edad_est = int(input("Edad: "))
        sexo_est = int(input("Sexo (1. Masculino; 2. Femenino): "))
        carrera_est = int(input("Carrera (1. Ingeniería; 2. Contaduría; 3. Derecho; 4. Otra): "))
        jornada_est = int(input("Jornada (1. Diurna; 2. Nocturna): "))
        
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

if __name__ == "__main__":
    procesar_estudiantes()