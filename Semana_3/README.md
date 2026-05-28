# Inventário de Laboratório

Projeto em Python para processar e organizar dados do inventário de um laboratório de Engenharia Química.
O código recebe três listas (reagentes, lotes e pureza), identifica e remove duplicações de reagentes, combina com zip as listas, exibe o inventário organizado e por fim exibe apenas os lotes aprovados.


## Como rodar o scipt

#### 1 - Primeiro você precisa ter o Python instalado no seu PC, ou usar algum compilador online.
#### 2 - Clone o repositorio pro seu PC, ou copie o código e coloque no colab (ai só rodar direto).
#### 3 - Se clonar o repositorio no PC, apenas execute o inventario_lab.py
#### 4 - E pronto, só ver as listas do inventário e dos lotes aprovados.

## Respostas Perguntas

### 1 - O dicionario em python permite apenas chaves únicas, e como o laboratório possui frascos do mesmo reagente, se convertessemos pra dicionario, cada reagente do mesmo nome iria sobrescrever o lote anterior, perdendo dados.

### 2 - A função zip() gera um objeto iterável do tipo zip, que trabalha com avaliação preguiçosa, ou seja, ele não gera todas as tuplas de uma vez, mas sim quando são solicitadas. O list() é usado pra forçar o iterador a processar todos os itens e salvar na memória em formato de lista.

### 3 - O list comprehension cria a lista, faz o loop, aplica a condição e a inserção de elementos em uma unica estrutura. E ainda é computacionalmente mais rápido do que fazer varios .append() dentro do for normal.