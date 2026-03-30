def calcular_frete(na_sede, qtd_produtos, valor_compra):
    # Regra 1: Moradores da mesma cidade
    if na_sede:
        return "Frete Grátis"
    
    # Regra 2: Outras cidades (ambas as condições devem ser verdadeiras)
    elif qtd_produtos > 3 and valor_compra > 1000:
        return "Frete Grátis"
    
    else:
        return "Cobrar Frete"

# Execução de Testes baseados na Tabela de Decisão
testes_frete = [
    (True, 1, 100, "R1 - Cliente na sede"),
    (False, 5, 1200, "R2 - Fora da sede, atende requisitos"),
    (False, 2, 1500, "R3 - Fora da sede, poucos produtos"),
    (False, 10, 500, "R4 - Fora da sede, valor baixo")
]

print("--- Exercício 5 ---")
for sede, qtd, valor, desc in testes_frete:
    resultado = calcular_frete(sede, qtd, valor)
    print(f"Teste {desc}: {resultado}")