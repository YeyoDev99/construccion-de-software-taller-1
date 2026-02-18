def calcular_retencion_subsidio():
    cod_emp = int(input("Código del empleado: "))
    nom_emp = input("Nombres del empleado: ")
    num_hijos = int(input("Número de hijos: "))
    pag_hora = float(input("Salario por hora: "))
    hrs_mes = float(input("Número de horas trabajadas al mes: "))

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

if __name__ == "__main__":
    calcular_retencion_subsidio()