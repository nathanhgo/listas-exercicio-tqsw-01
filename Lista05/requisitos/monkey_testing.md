# Monkey Testing

O *Monkey Testing Technique*, também conhecida como *Random Testing Technique* é uma técnica de testes baseada em testar valores aleatórios.

> ## Curiosidade
>
> O nome *Monkey* associado ao teste aleatório é atribuído provavelmente por conta do **Teorema do Macaco Infinito**, que estabelece que se um macaco ficasse apertando teclas aleatórias em um teclado de computador durante tempo infinito, eventualmente ele acabaria escrevendo algum texto, como o trabalho completo de Willian Shakespeare.

Como um teste que receberá valores aleatórios, uma etapa importante é a definição do domínio de valores válidos e inválidos que o sistema receberá.

## Tipos de testes aleatórios

1. Sequência de ações aleatória
2. Entrada de dados gerados aleatoriamente
3. Entrada de dados **selecionados** aleatoriamente de um banco de dados

## Vantagens

- São baratos e qualquer um consegue usar
- Podem levar mais tempo para serem executados e analisados

## Desvantagens

- Encontra apenas erros causados por mudança no código
- Alguns valores podem não ser testados por longos períodos de tempo
- Analisar os resultados de todos os testes leva mais tempo

## Exemplo

Por exemplo, um teste de uma função de divisão tem seu domínio de entrada definido como números gerados aleatóriamente dentro de um intervalo e usados em um caso de teste da função.