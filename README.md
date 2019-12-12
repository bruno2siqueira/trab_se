# Trabalho Final Disciplina de Sistemas Evolutivos, UFPEL 
 

Repositório do Trabalho realizado na disciplina de Sistemas Evolutivos. UFPEL

Autores: Bruno Siqueira da Silva e Leandro Camargo

Prof Dr. Prof. Marilton S. Aguiar.


Ao longo do desenvolvimento deste trabalho, realizou-se um estudo sobre o uso de técnicas de otimização, mais especificamente sobre o uso de algoritmos genéticos com o objetivo de otimizar o carregamento de veículos urbanos de carga. A implementação dos algoritmos atingiu o objetivo de selecionar produtos com parâmetros para ocupação ótima do espaço e peso, conforme os limites de carga definidos para o veículo de transporte estudado.

A codificação dos indivíduos com variáveis do tipo binária, mostrou-se adequada para o desenvolvimento deste trabalho, facilitando o desenvolvimento do mesmo. Na seleção por roleta, verificou-se uma tendência para a seleção de indivíduos melhores, que tornava o algoritmo suscetível a obter máximos globais. Os operadores genéticos simples (crossover, mutação, elitismo) utilizados neste trabalho, atenderam perfeitamente aos objetivos.

Os algoritmos implementados mostraram-se adequados para o desenvolvimento deste trabalho experimental. A implementação do algoritmo com a biblioteca DEAP, por sua vez, facilitou consideravelmente a codficação, devido ao  fato de encapsular diversos recursos para o desenvolvimento de AGs, tornando a tarefa de programar menos complexa.

Como trabalhos futuros espera implementar outros operadores genéticos para a busca de melhores indivíduos; a inserção de outros parâmetros importantes na acomodação das cargas, tais como a fragilidade dos itens e restrições de empilhamento das caixas para o transporte, assim como parâmetros relacionados à logística das entregas (visando a minimização dos custos); e a execução de novos ensaios com base de dados maiores. 
