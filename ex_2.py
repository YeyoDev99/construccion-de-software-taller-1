def procesar_fumigacion():
    Pedido_F = int(input("Ingrese la cantidad de pedidos: "))
    
    for i in range(Pedido_F):
        nom_granjero = input("Nombre del granjero: ")
        tipo_fum = int(input("Tipo de fumigación (1, 2, 3, 4): "))
        num_hect = float(input("Número de hectáreas: "))
        
        if tipo_fum == 1:
            valor_total = num_hect * 10
        elif tipo_fum == 2:
            valor_total = num_hect * 15
        elif tipo_fum == 3:
            valor_total = num_hect * 20
        elif tipo_fum == 4:
            valor_total = num_hect * 30
        else:
            valor_total = 0
            
        if num_hect > 1000:
            valor_total = valor_total * 0.95
            
        if valor_total > 3000:
            excedente = valor_total - 3000
            valor_total = 3000 + (excedente * 0.90)
            
        print(f"Granjero: {nom_granjero}")
        print(f"Valor a pagar: {valor_total:.2f}")

if __name__ == "__main__":
    procesar_fumigacion()