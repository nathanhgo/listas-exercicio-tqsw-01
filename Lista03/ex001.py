def avaliar_contratacao(idade):
    if 0 <= idade <= 15:
        return "Não empregar"
    elif 16 <= idade <= 17:
        return "Pode ser empregado tempo parcial"
    elif 18 <= idade <= 54:
        return "Pode ser empregado tempo integral"
    elif 55 <= idade <= 99:
        return "Não empregar"
    else:
        return "Idade fora do intervalo permitido (0-99)"

# Execução de Testes baseados na Tabela de Decisão
if __name__ == "__main__":
    testes = [
        (10, "R1 - Criança"),
        (16, "R2 - Jovem"),
        (25, "R3 - Adulto"),
        (60, "R4 - Idoso")
    ]
    
    for valor, desc in testes:
        resultado = avaliar_contratacao(valor)
        print(f"Teste {desc} (Idade {valor}): {resultado}")