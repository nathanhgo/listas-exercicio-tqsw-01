# Error Guessing

A técnica de "adivinhação de erro" ou *Error Guessing Technique* é uma prática para encontrar potenciais problemas e desenvolver casos de teste para um sistema. Ela depende fortemente do entendimento da aplicação e da experiência do testador em problemas encontrados no passado. Normalmente essa técnica funciona melhor quando combinada a outras técnicas de testes.

### Etapas da *Error Guessing Technique*

1. **Entender a aplicação**: É necessário ter um profundo conhecimento do SUT (*System Under Testing*), sabendo como ele funciona e quais são suas funcionalidades chave. Isso é essencial para saber quais são os pontos críticos que necessitam de mais atenção do testador.
2. **Analisar defeitos anteriores**: Não é exatamente uma etapa de um passo a passo, mas nesse momento é interessante que o testador se lembre ou pesquise problemas encontrados anteriormente em aplicações similares.
3. **Criar uma lista com prováveis problemas**: Com base no conhecimento do testador e nos problemas encontrados em sistemas similares, é possível criar uma lista de prováveis problemas (considerando por exemplo valores de entrada inválidos) que já podem estar incluídos nos casos de teste.
4. **Projetar casos de teste**: Escrever os casos de teste com base na lista de prováveis problemas identificados na etapa anterior.
5. **Executar os testes**: Execute os testes escritos para a aplicação e verifique se ela se comportou como esperado.
6. **Combinar com outras técnicas**: Use outras técnicas de testes para diminuir as chances de manter erros escondidos no sistema. Essa técnica funciona melhor quando combinada com outras técnicas de teste.
7. **Documentar a conclusão**: Documente resultados e erros obtidos durante o caminho que possam ser úteis a futuros testadores ou desenvolvedores.

## Vantagens

- Serve como um bom complemento de técnicas de teste estruturadas.
- Se beneficia da experiência do desenvolvedor.

## Desvantagens

- Depende fortemente da intuição e experiência do testador.
- Não funciona com iniciantes

## Exemplo

### Validação de página de login

Um testador pode deduzir que uma página de login poderia ter um erro quando estiver tratando com entradas de usuário inválidas, como:

- Nome de usuário muito longo
- Campo de senha em branco
- Uso de caractéres especiais

Com a *Error Guessing Technique* o testador pode identificar esses pontos de falha mais comuns e já gerar casos de teste com o objetivo de validar que estes problemas estão sendo verificados nos testes.