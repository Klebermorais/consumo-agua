# Solicita os dados ao usuário

tipo = input("Por gentileza, digite o tipo de imóvel (comercial, casa ou apartamento): ").lower()

consumo = float(input("Digite o consumo mensal de água em m³: "))

# Classificação usando match/case

match tipo:

    case "comercial":
        print("Tarifa comercial aplicada consulte o plano corporativo.")

    case "apartamento" if consumo < 10:    
        print("Consumo econômico excelente, controle de água!")

    case "apartamento" | "casa" if consumo <= 25:
        print("Consumo moderado, dentro do padrão residencial.")

    case _:
        print("Consumo excessivo, adote medidas de economia e verifique vazamentos.")

