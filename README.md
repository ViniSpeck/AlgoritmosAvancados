# Matéria de Algoritmos Avançados
Alunos: Vinícius Ferraro Speck, Rodrigo Correia e Pedro Eduardo


<h3>Atividade 1</h3> 

<i>Problema:</i> Faça um programa que leia a lista de nomes masculinos e femininos dos arquivos disponibilizados em https://github.com/MedidaSP/nomes-brasileiros-ibge e carregue em uma lista. A lista deve ser ordenada usando o método de ordenação da linguagem.

Após os dados terem sido lidos e carregados na memória faça o programa solicitar para o usuário um nome e procurar se o nome existe na lista indicando em que posicao ele foi encontrado ou indicando que o nome não existe.

A busca deve ser implementada usando busca binária.


<i>Resolução:</i> Após definir variáveis de valor mínimo, médio e máximo, começando pela metade da lista, se o item iterado for maior/menor que o item médio define-se o ponto médio +1/-1 como o novo mínimo/máximo e processo se repete até encontrar o valor buscado. 

![image](https://user-images.githubusercontent.com/69943624/189453582-1b110a75-a185-476f-b472-4620bf011687.png)


<i>Complexidade:</i> O(log n) -> Cada iteração reduz a área pesquisável na metade.

<hr>

<h3>Atividade 2</h3> 

<i>Problema:</i> Mesmo problema da primeira atividade, com o requisito de ser resolvido com complexidade O(1)


<i>Resolução:</i> Transformar o dataset em dicionário, fazendo as adequações necessárias (ordenar, resetar o índice e inverter a relação chave valor nesse caso que desejamos buscar por nome e não índice) e usar a função .get() para buscar a posição do nome.

![image](https://user-images.githubusercontent.com/69943624/189454322-545db4c2-fafd-4842-a020-42ec06ca8271.png)


<i>Complexidade:</i> O(1) -> A implementação interna do dicionário usa tabelas hash, então tem complexidade O(1) para encontrar o índice.

<hr>

<h3>Atividade 3</h3> 

<i>Problema:</i> Mesmo problema da primeira atividade, com o requisito de ser resolvido em paralelo.


<i>Resolução:</i> É utilizado o mesmo algoritmo de busca da atividade 1, mas dessa vez a execução é dividida em duas threads, um que busca o nome masculino e outro que busca o nome feminino. São iniciadas as threads passando os parâmetros de busca e depois são sincronizadas com o join().


<i>Complexidade:</i> O((logn)/2)

<hr>

<h3>Atividade 4</h3> 

<i>Problema:</i> Dada uma matriz de tamanho N. A tarefa é ordenar os elementos da matriz completando funções heapify() e buildHeap() que são usadas para implementar Heap Sort.


Sugestão de dado para importar e ordenar https://www.kaggle.com/datasets/sveta151/tiktok-popular-songs-2019


<i>Resolução:</i> A função heapSort() ordena a array para maxHeap, itera entre os elementos da array chamando a função heapify, que ordena o elemento iterado dentro da array estruturada como árvore.


<i>Complexidade:</i> O(nlogn) -> Cenário do pior caso: Ir da base de uma raíz até a oposta

<hr>

<h3>Atividade 5</h3> 

<i>Problema:</i> Você recebe uma matriz unidimensional que pode conter tanto inteiros positivos quanto negativos, encontra a soma de subarranjos contíguos de números que tem a maior soma.


<i>Resolução:</i> Foi usada uma abordagem similar ao merge sort, dividindo a array principal em duas partes iguais após calcular o ponto médio. Sabendo que a array com a maior soma está a direita, esquerda ou passando pelo meio da array principal, foi usada a recursividade pra pegar a soma das possibilidades e juntar no resultado.


<i>Complexidade:</i> O(nlogn)


