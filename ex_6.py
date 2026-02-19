# Yader Ibraldo Quiroga Torres - 20222020034

def obtener_votos_validos(nombre_candidato):
    """Obtiene el número de votos válido para un candidato."""
    while True:
        try:
            votos = int(input(f"Votos obtenidos por {nombre_candidato}: "))
            if votos < 0:
                print("Error: El número de votos no puede ser negativo")
                continue
            return votos
        except ValueError:
            print("Error: Ingrese un número entero válido")

def determinar_resultado_eleccion():
    try:
        v_juan = obtener_votos_validos("Juan")
        v_pedro = obtener_votos_validos("Pedro")
        v_maria = obtener_votos_validos("Maria")

        total_votos = v_juan + v_pedro + v_maria
        
        if total_votos == 0:
            print("Error: No hay votos registrados")
            return
            
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
    except Exception as e:
        print(f"Error al procesar elección: {e}")

if __name__ == "__main__":
    try:
        determinar_resultado_eleccion()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")