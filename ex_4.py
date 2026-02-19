# Yader Ibraldo Quiroga Torres - 20222020034

def obtener_entero_positivo(mensaje):
    """Obtiene un entero positivo válido del usuario."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: Ingrese un número no negativo")
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

def calcular_retencion_subsidio():
    try:
        cod_emp = obtener_entero_positivo("Código del empleado: ")
        nom_emp = input("Nombres del empleado: ").strip()
        if not nom_emp:
            print("Error: El nombre no puede estar vacío")
            return
        num_hijos = obtener_entero_positivo("Número de hijos: ")
        pag_hora = obtener_decimal_positivo("Salario por hora: ")
        hrs_mes = obtener_decimal_positivo("Número de horas trabajadas al mes: ")

        devengado = pag_hora * hrs_mes

        if devengado < 428000:
            if num_hijos > 12:
                ret = 0
            elif 6 < num_hijos <= 12:
                ret = devengado * ((12 - num_hijos) / 2 / 100)
            else:
                ret = devengado * 0.04
        else:
            if num_hijos < 5:
                ret = devengado * 0.05
            elif 5 <= num_hijos < 10:
                ret = devengado * ((10 / num_hijos) / 100)
            else:
                ret = 0

        subs = num_hijos * 17200
        total_p = devengado - ret + subs

        print(f"Código: {cod_emp}")
        print(f"Nombres: {nom_emp}")
        print(f"Devengado: {devengado:.2f}")
        print(f"Retención: {ret:.2f}")
        print(f"Subsidio: {subs:.2f}")
        print(f"Total a pagar: {total_p:.2f}")
    except Exception as e:
        print(f"Error al calcular retención y subsidio: {e}")

if __name__ == "__main__":
    try:
        calcular_retencion_subsidio()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")