import re

def verificar_senha_forte(senha):
    # Condições baseadas na especificação
    tem_tamanho = len(senha) >= 8
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    # Considera símbolos como qualquer caractere que não seja letra ou número
    tem_simbolo = bool(re.search(r"[@#$%.]", senha))

    if tem_tamanho and tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo:
        return "Senha Forte"
    else:
        return "Senha Fraca"

# Execução de Testes baseados na Tabela de Decisão
testes_senha = [
    ("Ab1@5678", "R1 - Todos os requisitos"),
    ("Ab1@", "R2 - Curta demais"),
    ("ab1@5678", "R3 - Sem maiúscula"),
    ("AB1@5678", "R4 - Sem minúscula"),
    ("Abc@defg", "R5 - Sem número"),
    ("Ab123456", "R6 - Sem símbolo")
]

print("-" * 30)
for valor, desc in testes_senha:
    resultado = verificar_senha_forte(valor)
    print(f"Teste {desc}: {resultado}")