def determinar_resultado_eleccion():
    v_juan = int(input("Votos obtenidos por Juan: "))
    v_pedro = int(input("Votos obtenidos por Pedro: "))
    v_maria = int(input("Votos obtenidos por Maria: "))

    total_votos = v_juan + v_pedro + v_maria
    meta_ganar = (total_votos // 2) + 1

    if v_juan >= meta_ganar:
        resultado = "Ganador: Juan"
    elif v_pedro >= meta_ganar:
        resultado = "Ganador: Pedro"
    elif v_maria >= meta_ganar:
        resultado = "Ganador: Maria"
    else:
        if v_juan == v_pedro == v_maria:
            resultado = "Elección anulada por empate triple"
        elif (v_juan < v_pedro and v_pedro == v_maria) or \
             (v_pedro < v_juan and v_juan == v_maria) or \
             (v_maria < v_juan and v_juan == v_pedro):
            resultado = "Elección anulada por empate doble en el segundo lugar o empate por el primero sin alcanzar mayoría"
        else:
            if v_juan > v_pedro and v_juan > v_maria:
                primero = "Juan"
                segundo = "Pedro" if v_pedro > v_maria else "Maria"
            elif v_pedro > v_juan and v_pedro > v_maria:
                primero = "Pedro"
                segundo = "Juan" if v_juan > v_maria else "Maria"
            else:
                primero = "Maria"
                segundo = "Juan" if v_juan > v_pedro else "Pedro"
            resultado = f"Segunda vuelta entre: {primero} y {segundo}"

    print(f"Total de votos: {total_votos}")
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    determinar_resultado_eleccion()