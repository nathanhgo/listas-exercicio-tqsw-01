def validar_senha_dicionario(senha):
    dicionario_proibido = ["teste", "funcional", "software", "qualidade"]
    
    tamanho_ok = 6 <= len(senha) <= 10
    inicio_ok = senha[0].isalnum() or senha[0] == "?" if senha else False
    fora_dicionario = senha.lower() not in dicionario_proibido

    if tamanho_ok and inicio_ok and fora_dicionario:
        return "Senha Válida"
    else:
        return "Senha Inválida"

# Testes
testes_ex3 = [
    ("?Senha1", "R1 - Válida"),
    ("123", "R2 - Curta"),
    ("!Senha1", "R3 - Início Inválido"),
    ("teste", "R4 - No Dicionário")
]

print("--- Exercício 3 ---")
for valor, desc in testes_ex3:
    print(f"{desc} ({valor}): {validar_senha_dicionario(valor)}")