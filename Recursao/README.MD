# Estruturas Recursivas

## Introdução

* Existem Linguaguens que não possuem Estruturas de Repetição como For e um While. Um grande exemplo é a linguagem de paradigma Funcional Haskell.
* Já que Haskell não nos oferece esse suporte, nós programadores utilizamos de uma poderosa ferramenta: a RECURSÃO.


## Mas afinal de contas, oque é Recursão? 

* Segundo a wikepedia: Em ciência da computação, a recursividade é a definição de uma sub-rotina (função ou método) que pode invocar a si mesma. 
* Eu ia simplificar, mas a wikipedia ja disse tudo que se precisava. Recursividade é, basicamente, uma função que invoca ela mesmo.

## O poder da Recursão.

* Certo, ai você me pergunta qual a vantagem de usar recursão quando eu posso usar um laço de repetição como um for.
* A Recursão te da o poder de quebrar grandes problemas, em pequenos problemas e assim facilitar a solução do problema.
* Um exemplo classico que mostra o poder da recursão é o algoritmo do MERGESORT. O mergesort é um algoritmo de ordenação que se utiliza da estratégia de dividir para conquistar. E para dividir e conquistar ele faz o uso da recursão.


## Como fazer um método recursivo.

* A coisa mais importante é a definição de um caso base.

### Oque é o caso base?

* Como estamos defininindo uma função em função dela mesmo precisamos de uma forma de parar a chamada da função.
* Por exemplo: Você quer que se eu algoritmo rode 10x. Então, como parametro você vai passar quantas vezes seu algoritmo ja rodou e quando esse valor atingir o valor 10, ele não vai chamar mais a propria função.

* Com o caso bem definido, vamos fazer a chamada recursiva da propria função, dentro da função.