def calcular_valor_tickets(qtd, idades):
    if 0 < qtd <= 5:
        valor = 0
        for idade in idades[:qtd]:
            if idade < 0 or idade > 100:
                raise ValueError("Idade inválida")
            if idade <= 12:
                valor += 10
            elif 13 <= idade <= 59:
                valor += 30
            else:
                valor += 15
        return f"Valor total: R$ {valor}"
    elif qtd == 0:
        raise ValueError("Nenhum ticket adicionado!")
    else:
        return "Quantidade máxima excedida!"
