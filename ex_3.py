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

def calcular_nomina_molina():
    try:
        cod_trab = obtener_entero_positivo("Código del trabajador: ")
        nom_trab = input("Nombre del trabajador: ").strip()
        if not nom_trab:
            print("Error: El nombre no puede estar vacío")
            return
        sexo_trab = obtener_sexo_valido()
        horas_trab = obtener_decimal_positivo("Número de horas trabajadas: ")
        tarifa_h = obtener_decimal_positivo("Tarifa hora normal: ")

        if horas_trab < 240:
            sal_bruto = horas_trab * tarifa_h
        elif 240 <= horas_trab < 300:
            extras = horas_trab - 239
            sal_bruto = (239 * tarifa_h) + (extras * tarifa_h * 2.5)
        else:
            extras = horas_trab - 299
            sal_bruto = (299 * tarifa_h) + (extras * tarifa_h * 1.7)

        if sal_bruto < 900000:
            retencion = 0
        elif 900000 <= sal_bruto < 1200000:
            retencion = sal_bruto * 0.05
        elif 1200000 <= sal_bruto < 2000000:
            retencion = sal_bruto * 0.10
        else:
            retencion = sal_bruto * 0.20

        sal_neto = sal_bruto - retencion

        print(f"Código: {cod_trab}")
        print(f"Nombre: {nom_trab}")
        print(f"Salario Bruto: {sal_bruto:.2f}")
        print(f"Retención: {retencion:.2f}")
        print(f"Sexo: {sexo_trab}")
        print(f"Salario Neto: {sal_neto:.2f}")
    except Exception as e:
        print(f"Error al calcular nómina: {e}")

if __name__ == "__main__":
    try:
        calcular_nomina_molina()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")