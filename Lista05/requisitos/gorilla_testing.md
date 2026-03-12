# Gorilla Testing

Diferentemente da *Monkey Testing Technique* que é caótica e tenta testar coisas aleatórias pelo sistema, combinando diferentes ações em diferentes sequências com diferentes valores, a *Gorilla Testing Technique* é uma técnica que busca levar uma única funcionalidade ao estresse máximo, para garantir que ela não quebrará facilmente.

Uma analogia interessante é imaginar um poderoso gorila em uma floresta que, ao invés de pular de galho em galho por entre as árvores, ele concentra sua atenção em uma única árvore, puxando-a, chacoalhando-a e forçando-a para os lados, garantindo que ela esteja bem fixa no chão e que não cairá facilmente.

## Vantagens

- Blindar módulos críticos
- Garantir performance quando o sistema estiver sobre estresse
- Confiança nos resultados

## Desvantagens

- Tempo e recursos intensivos
- Focam em um único módulo e não tem uma grande cobertura do sistema

## Exemplo

Um *Gorilla Testing* em uma tela de login, por exemplo, tentaria forçar entradas corretas, incorretas e maliciosas para garantir que seu sistema responde como o esperado a estes tipos de entrada.