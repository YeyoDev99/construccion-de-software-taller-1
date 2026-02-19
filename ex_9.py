# Yader Ibraldo Quiroga Torres - 20222020034

import math

def obtener_decimal(mensaje):
    """Obtiene un número decimal válido del usuario."""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Ingrese un número válido")

def obtener_entero_positivo(mensaje, minimo=1):
    """Obtiene un entero positivo válido del usuario."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"Error: Ingrese un número mayor o igual a {minimo}")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número entero válido")

def calcular_factorial(n):
    """Calcula el factorial de n de forma segura."""
    try:
        if n < 0:
            raise ValueError("Factorial no está definido para números negativos")
        if n == 0 or n == 1:
            return 1
        
        if n > 170:
            print(f"Advertencia: n={n} es muy grande, el resultado puede ser impreciso")
        
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
    except Exception as e:
        print(f"Error al calcular factorial: {e}")
        return None

def calcular_termino_exponencial(x, n):
    """Calcula el término n de la serie exponencial: x^n / n!"""
    try:
        numerador = x ** n
        denominador = calcular_factorial(n)
        
        if denominador is None:
            raise ValueError("Error al calcular factorial")
        
        if denominador == 0:
            raise ValueError("División por cero en el término exponencial")
        
        termino = numerador / denominador
        return termino
    except OverflowError:
        print(f"Error: Desbordamiento en el cálculo del término {n}")
        return None
    except Exception as e:
        print(f"Error al calcular término {n}: {e}")
        return None

def calcular_funcion_exponencial():
    try:
        valor_x = obtener_decimal("Ingrese el valor de x: ")
        num_terminos = obtener_entero_positivo("Ingrese el número de términos para la serie: ", minimo=1)
        
        if num_terminos > 1000:
            print("Advertencia: número de términos muy grande, esto puede tomar tiempo")
        
        exponencial_res = 0
        
        for n in range(num_terminos):
            try:
                termino = calcular_termino_exponencial(valor_x, n)
                
                if termino is None:
                    print(f"No se pudo procesar el término {n}, deteniendo cálculo")
                    break
                
                exponencial_res += termino
                
                if (n + 1) % 50 == 0 or n == num_terminos - 1:
                    print(f"Procesando término {n + 1}/{num_terminos}...")
                
                if abs(termino) < 1e-10:
                    print(f"Serie convergió en término {n + 1}")
                    break
                    
            except Exception as e:
                print(f"Error en término {n}: {e}")
                continue
        
        try:
            valor_real = math.exp(valor_x)
            error = abs(exponencial_res - valor_real)
            print(f"\nResultado de e^{valor_x} con {num_terminos} términos: {exponencial_res:.10f}")
            print(f"Valor real de e^{valor_x}: {valor_real:.10f}")
            print(f"Error absoluto: {error:.10e}")
        except:
            print(f"\nResultado de e^{valor_x} con {num_terminos} términos: {exponencial_res:.10f}")
            
    except Exception as e:
        print(f"Error al calcular la función exponencial: {e}")

if __name__ == "__main__":
    try:
        calcular_funcion_exponencial()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")