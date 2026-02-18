
def procesar_registro_clientes():
    Cliente_Reg = int(input("Ingrese la cantidad de clientes a registrar: "))
    
    lista_mujeres_filtro = []
    lista_hombres_filtro = []
    
    for i in range(Cliente_Reg):
        nombre_cl = input("Nombre: ")
        sexo_cl = input("Sexo (M/F): ")
        edad_cl = int(input("Edad: "))
        altura_cl = float(input("Altura (metros): "))
        peso_cl = float(input("Peso (libras): "))
        color_ojos = int(input("Color ojos (1: Azules, 2: Castaños, 3: Otros): "))
        color_cabello = int(input("Color cabello (1: Castaño, 2: Rubio, 3: Otros): "))
        
        if sexo_cl.upper() == 'F':
            if color_cabello == 2 and color_ojos == 1:
                if 1.65 <= altura_cl <= 1.75 and peso_cl < 120:
                    lista_mujeres_filtro.append(nombre_cl)
        
        elif sexo_cl.upper() == 'M':
            if color_ojos == 2 and altura_cl > 1.70:
                if 180 <= peso_cl <= 220:
                    lista_hombres_filtro.append(nombre_cl)

    print("\na) Mujeres rubias, ojos azules (1.65-1.75m, <120lb):")
    for nombre in lista_mujeres_filtro:
        print(nombre)
        
    print("\nb) Hombres ojos castaños (>1.70m, 180-220lb):")
    for nombre in lista_hombres_filtro:
        print(nombre)

if __name__ == "__main__":
    procesar_registro_clientes()