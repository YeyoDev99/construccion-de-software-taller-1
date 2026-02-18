def procesar_accidentes_medellin():
    ATM_n = int(input("Ingrese la cantidad de conductores involucrados en accidentes: "))
    
    total_conductores = ATM_n
    cont_menores_25 = 0
    cont_femenino = 0
    cont_masc_12_30 = 0
    cont_fuera_medellin = 0
    
    anio_actual = 2024

    for i in range(ATM_n):
        identificación = int(input("Identificación del conductor: "))
        fecha_acc = input("Fecha del accidente (DD/MM/AAAA): ")
        ubicación = input("Ubicación del accidente: ")
        
        anio_nac_cond = int(input("Año de nacimiento del conductor: "))
        sexo_cond = int(input("Sexo (1: Femenino, 2: Masculino): "))
        
        placa = input("Placa del carro: ")
        registro = int(input("Registro del carro (1: Medellín, 2: Otras ciudades): "))
        
        edad_cond = anio_actual - anio_nac_cond
        
        if edad_cond < 25:
            cont_menores_25 += 1
            
        if sexo_cond == 1:
            cont_femenino += 1
            
        if sexo_cond == 2 and 12 <= edad_cond <= 30:
            cont_masc_12_30 += 1
            
        if registro == 2:
            cont_fuera_medellin += 1

    porc_menores_25 = (cont_menores_25 / total_conductores) * 100 if total_conductores > 0 else 0
    porc_femenino = (cont_femenino / total_conductores) * 100 if total_conductores > 0 else 0
    porc_masc_12_30 = (cont_masc_12_30 / total_conductores) * 100 if total_conductores > 0 else 0
    porc_fuera_medellin = (cont_fuera_medellin / total_conductores) * 100 if total_conductores > 0 else 0

    print(f"Porcentaje de conductores menores de 25 años: {porc_menores_25:.2f}%")
    print(f"Porcentaje de conductores del sexo femenino: {porc_femenino:.2f}%")
    print(f"Porcentaje de conductores masculinos entre 12 y 30 años: {porc_masc_12_30:.2f}%")
    print(f"Porcentaje de conductores con carros registrados fuera de Medellín: {porc_fuera_medellin:.2f}%")

if __name__ == "__main__":
    procesar_accidentes_medellin()