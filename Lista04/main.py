def verificar_frete_gratis(cidade_cliente, cidade_loja, qtd_produtos, valor_total):
    """
    Verifica se o cliente tem direito a frete grátis com base nas regras da promoção.
    """
    # C1: Morador da mesma cidade da loja
    # Usamos lower() e strip() para evitar erros de digitação com maiúsculas ou espaços
    c1 = cidade_cliente.strip().lower() == cidade_loja.strip().lower()
    
    # C2: Comprou mais de 3 produtos
    c2 = qtd_produtos > 3
    
    # C3: Valor total da compra atingiu o mínimo de R$ 200,00
    c3 = valor_total >= 200.00
    
    # A LÓGICA DO GRAFO: E1 ocorre se C1 for verdadeiro OU (C2 E C3) forem verdadeiros
    if c1 or (c2 and c3):
        return "Frete Grátis"
    else:
        return "Cobrar Frete"

def main():
    # ==========================================
    # EXECUÇÃO DOS CASOS DE TESTE (CT)
    # ==========================================

    cidade_sede = "Jacareí"

    print("--- Rodando Casos de Teste da Tabela de Decisão ---")

    # CT01: Morador da cidade (Regra 1)
    resultado_ct01 = verificar_frete_gratis("Jacareí", cidade_sede, 1, 50.00)
    print(f"CT01 (Morador local): {resultado_ct01} | Esperado: Frete Grátis")

    # CT02: De fora, bateu qtd e valor (Regra 2)
    resultado_ct02 = verificar_frete_gratis("São José dos Campos", cidade_sede, 4, 250.00)
    print(f"CT02 (De fora, bateu metas): {resultado_ct02} | Esperado: Frete Grátis")

    # CT03: De fora, bateu qtd, falhou no valor (Regra 3)
    resultado_ct03 = verificar_frete_gratis("São Paulo", cidade_sede, 5, 150.00)
    print(f"CT03 (De fora, falhou valor): {resultado_ct03} | Esperado: Cobrar Frete")

    # CT04: De fora, falhou na qtd (Regra 4 - valor não importa mais)
    resultado_ct04 = verificar_frete_gratis("Caçapava", cidade_sede, 2, 400.00)
    print(f"CT04 (De fora, falhou qtd): {resultado_ct04} | Esperado: Cobrar Frete")

main()