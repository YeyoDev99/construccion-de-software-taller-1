Algoritmo FuncionExponencial
	Definir valor_x, exponencial_res, termino, factorial Como Real
	Definir num_terminos, n, i Como Entero
	Definir continuar Como Logico
	
	Escribir "Ingrese el valor de x: "
	Leer valor_x
	
	Repetir
		Escribir "Ingrese el numero de terminos para la serie (minimo 1): "
		Leer num_terminos
		Si num_terminos < 1 Entonces
			Escribir "Error: Ingrese un numero mayor o igual a 1"
		Fin Si
	Hasta Que num_terminos >= 1
	
	exponencial_res <- 0
	continuar <- Verdadero
	n <- 0
	
	Mientras n < num_terminos Y continuar Hacer
		factorial <- 1
		Si n > 1 Entonces
			Para i <- 1 Hasta n Hacer
				factorial <- factorial * i
			Fin Para
		Fin Si
		
		termino <- (valor_x ^ n) / factorial
		exponencial_res <- exponencial_res + termino
		
		Si abs(termino) < 0.0000000001 Entonces
			continuar <- Falso
		Fin Si
		
		n <- n + 1
	Fin Mientras
	
	Escribir ""
	Escribir "Resultado de e^", valor_x, " con ", n, " terminos: ", exponencial_res
FinAlgoritmo