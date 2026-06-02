# Dicionários criados para futura integração com banco de dados automação (AINDA NÃO IMPLEMENTADO)

# Dict tipo de problema (severidade 1, 2 ou 3)
severidade_dict = {
    "check-up": 1,
    "vacina": 1,
    "alergia": 1,
    "ferimento superficial": 1,
    
    "diarreia": 2,
    "febre": 2,
    "vômito": 2,
    "infecção leve": 2,
    "imobilidade": 2, 
    
    "ferimento grave": 3, 
    "fratura": 3,
    "convulsão": 3,
    "dificuldade respiratória": 3,
    "trauma": 3, 
    "infecção grave": 3
}

# Dict estado do animal (urgência 1, 2 ou 3)
urgencia_dict = {
    "nenhum sintoma": 1,
    "sintoma leve": 1,
    
    "sintoma persistente": 2,
    "sintoma com agravamento": 2, 
    
    "grave desconforto": 3,
    "grave dor": 3,
    "agônico": 3,
    "perda de consciência": 3
}

# Obter severidade
def obter_severidade():
    print("=== TIPO DE PROBLEMA ===")
    print("1 - Check-up")
    print("2 - Vacina")
    print("3 - Alergia")
    print("4 - Ferimento superficial")
    print("5 - Diarreia")
    print("6 - Febre")
    print("7 - Vômito")
    print("8 - Infecção leve")
    print("9 - Imobilidade")
    print("10 - Ferimento grave")
    print("11 - Fratura")
    print("12 - Convulsão")
    print("13 - Dificuldade respiratória")
    print("14 - Trauma")
    print("15 - Infecção grave")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
        else:
            if 1 <= opcao <= 15:
                if opcao in [1, 2, 3, 4]:
                    return 1
                elif opcao in [5, 6, 7, 8, 9]:
                    return 2
                else:
                    return 3
            else:
                print("Número fora do intervalo.")


# Obter urgência
def obter_urgencia():
    print("\n=== ESTADO DO ANIMAL ===")
    print("1 - Nenhum sintoma")
    print("2 - Sintoma leve")
    print("3 - Sintoma persistente")
    print("4 - Sintoma com agravamento")
    print("5 - Grave desconforto")
    print("6 - Grave dor")
    print("7 - Agônico")
    print("8 - Perda de consciência")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
        else:
            if 1 <= opcao <= 8:
                if opcao in [1, 2]:
                    return 1
                elif opcao in [3, 4]:
                    return 2
                else:
                    return 3
            else:
                print("Número fora do intervalo.")


# Calcular prioridade
def calcular_prioridade(severidade, urgencia):
    score = severidade * urgencia

    if score <= 3:
        return score, "Baixa"
    elif score <= 6:
        return score, "Média"
    else:
        return score, "Alta"


# PROGRAMA PRINCIPAL
nivel_severidade = obter_severidade()
nivel_urgencia = obter_urgencia()

score, prioridade = calcular_prioridade(nivel_severidade, nivel_urgencia)

print("\n=== RESULTADO FINAL ===")
print(f"Score: {score}")
print(f"Prioridade de atendimento: {prioridade}")
print("\nClassificação concluída com sucesso!")

