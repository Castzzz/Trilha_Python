# Simulador de Batalha de Cartas (TCG)

Projeto em Python para simular duelo em turnos de 2 cartas de um tcg, primeiro o programa coleta os dados das cartas, valida os dados e depois inicia a batalha por turnos automaticamente.

Na batalha, as cartas vão se atacar alternadamente até que uma delas chegue a 0 de vida.

## Como rodar o scipt

#### 1 - Primeiro você precisa ter o Python instalado no seu PC, ou usar algum compilador online.
#### 2 - Clone o repositorio pro seu PC, ou copie o código e coloque no colab (ai só rodar direto).
#### 3 - Se clonar o repositorio no PC, apenas execute o arquivo simulador_tcg.py
#### 4 - Insira os dados que o codigo pedir.
#### 5 - Veja a batalha acontecer.

## Respostas Perguntas

#### 1 - A principal diferença é que no for a gente "sabe" o quanto a gente vai querer repetir. No while a gente não vai saber quantas vezes queremos repetir, então usamos uma condição pra ele parar, mas não sabendo quantas vezes ele vai rodar. Pro duelo o while é a melhor escolha porque não tem como saber ao certo quantos turnos a batalha vai durar, só sabemos quando parar (quando a vida chega a 0).

#### 2 - O return serve pra retornar um resultado dentro da função para a parte do código que a chamou. Se uma função que faz um cálculo não possuir o return, a função vai retornar por padrão None.

#### 3 - Loop infinito é quando um laço de while não para de rodar, a condição de parada dele nunca acontece. Pra evitar isso, o melhor é garantir que a condição de parada do while seja atualizada dentro do laço.