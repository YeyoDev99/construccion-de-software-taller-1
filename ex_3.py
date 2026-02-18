def calcular_nomina_molina():
    cod_trab = int(input("Código del trabajador: "))
    nom_trab = input("Nombre del trabajador: ")
    sexo_trab = input("Sexo (M/F): ")
    horas_trab = float(input("Número de horas trabajadas: "))
    tarifa_h = float(input("Tarifa hora normal: "))

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

if __name__ == "__main__":
    calcular_nomina_molina()