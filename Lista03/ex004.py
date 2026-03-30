def interface_bancaria(cod_area, prefixo, sufixo, senha, operacao):
    # Validações
    valida_area = cod_area == "" or (len(cod_area) == 3 and cod_area.startswith('0') and cod_area.isdigit())
    valida_prefixo = len(prefixo) == 3 and not prefixo.startswith('0') and prefixo.isdigit()
    valida_sufixo = len(sufixo) == 4 and sufixo.isdigit()
    valida_senha = len(senha) == 6 and senha.isalnum()
    valida_op = operacao.lower() in ['c', 'd', 'e']

    if valida_area and valida_prefixo and valida_sufixo and valida_senha and valida_op:
        return f"Operação '{operacao}' realizada com sucesso!"
    else:
        return "Erro: Dados inválidos"

# Testes
testes_ex4 = [
    ("", "344", "2598", "abc123", "c"),  # R1 - Sucesso (Cód Vazio)
    ("011", "344", "2598", "abc123", "e"), # R1 - Sucesso (Cód 011)
    ("11", "344", "2598", "abc123", "d"),  # R2 - Cód Área Errado
    ("011", "044", "2598", "abc123", "c")  # R3 - Prefixo inicia com 0
]

print("\n--- Exercício 4 ---")
for a, p, s, sen, op in testes_ex4:
    print(f"Teste: {interface_bancaria(a, p, s, sen, op)}")