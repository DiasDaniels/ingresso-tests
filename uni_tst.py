def calcular_valor_tickets(qtd, idades):
    if qtd < 0 or qtd > 5:
        return "Quantidade máxima excedida!"
    if qtd == 0:
        return "Nenhum ticket adicionado!"
    
    valor = 0
    for idade in idades[:qtd]:
        if idade < 1 or idade > 100:
            raise ValueError("Idade inválida")
        if idade <= 12:
            valor += 10
        elif 13 <= idade <= 59:
            valor += 30
        else:
            valor += 15
    return f"Valor total: R$ {valor}"
