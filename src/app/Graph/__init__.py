class Graph:
  def __init__(self):
    self.adjacentNodeList = []

  def greedyAlgorithm():
    return ''
# /**
#         Algoritmo Guloso para Coloração de Vértices.
# */
# int Grafo::algoritmoGuloso()
# {
#     ordenado.clear();
#     auxOrdena.clear();
#     double tInicio = clock();
#     int i = 0;
#     for(std::vector<No>::iterator it = listaAdj.begin(); it != listaAdj.end(); ++it)
#     {
#         it->setCorNo(-1);           // Coloca as cores de todos os nos como -1
#         ordenado.push_back(i);      // Manda a posicao de todos os nós na listaAdj para o vetor ordenado
#         i++;
#     }


#     auxOrdena = listaAdj;

#     quickSort(0,listaAdj.size()-1);         // Ordena o vetor em ordem descrecente em relacao ao grau.



#     int k = 0;                              // O maximo de cor no momento.

#     listaAdj[ordenado[0]].setCorNo(k);      // Pega o primeiro vertice com maior No e adiciona a primeira cor a ele.


#     for(std::vector<Aresta>::iterator arest = listaAdj[ordenado[0]].listaAresta.begin(); arest != listaAdj[ordenado[0]].listaAresta.end(); ++arest)
#     {
#         listaAdj[arest->getIndiceNo()].addCorAdj(k);        // Adiciona k no vetor de cores adjacentes de todos os nós adjacentes ao primeiro no.
#     }
#     k++;                                                    // Atualiza k.

#     for(int j=1; j < ordenado.size() ; j++)                 // Pega os próximos nós de acordo com a ordem decrescente em reaçao ao grau.
#     {
#         int pos = ordenado[j];                              // Var pos que pega qual o indice da listaAdj fica o nó.

#         for(int i=0; i<=k ; i++)                            // For que roda todas as cores que existem até o momento.
#         {

#             bool flag = false;
#             if(i<k)                                         // Se i = k entao nenhum nó adjacente a ele tem cor k, assim a cor dele sera k e nao é preciso checar suas cores adjacentes.
#             {
#                 for(int corAdjacente = 0; corAdjacente < listaAdj[pos].corAdj.size(); corAdjacente++)       // For que roda todas as cores que sao adjacentes ao nó, pelo vetor corAdjacente que pertence ao nó.
#                 {
#                     if(listaAdj[pos].corAdj[corAdjacente] == i)
#                     {
#                         flag = true;                                          // Var flag recebe true se existe a cor i no vetor de corAdjacente do nó, e assim passa para a próxima cor.
#                         break;
#                     }
#                 }
#             }
#             /* Se a Var flag for falsa, entao temos que aquele indice de cor nao está sendo
#                utilizada por nenhum nó adjacente, portanto pode ser dada a esse nó, e para
#                isso, é necessario verificar se a cor i é uma cor que ja foi utilizada antes
#                ou é uma cor nova (o que implica que o nó é adjacente a todas as cores já
#                utilizadas), sendo assim necessário atualizar a variavel k, com uma cor nova.
#             */
#             if(flag == false && i < k)                                   // Cor i já existe.
#             {
#                 listaAdj[pos].setCorNo(i);
#                 for(std::vector<Aresta>::iterator arest = listaAdj[pos].listaAresta.begin(); arest != listaAdj[pos].listaAresta.end(); ++arest)
#                 {
#                     listaAdj[arest->getIndiceNo()].addCorAdj(i);         // Adiciona k no vetor de cores adjacentes de todos os nós adjacentes ao no.
#                 }
#                 break;
#             }
#             else if(flag == false && i==k)                               // Cor i não existe.
#             {
#                 listaAdj[pos].setCorNo(i);
#                 for(std::vector<Aresta>::iterator arest = listaAdj[pos].listaAresta.begin(); arest != listaAdj[pos].listaAresta.end(); ++arest)
#                 {
#                     listaAdj[arest->getIndiceNo()].addCorAdj(i);         // Adiciona k no vetor de cores adjacentes de todos os nós adjacentes ao no.
#                 }
#                 k++;                                                     // Atualiza k com nova cor
#                 break;
#             }
#         }
#     }

#         double tFinal = clock();
#         double tDecorrido = ((double)(tFinal - tInicio))/CLOCKS_PER_SEC;
#         cout << "Tempo decorrido: " << tDecorrido <<" segundos" << endl;

#     return k;                                                            // Retorna o numero k-coloravel do grafo.
# }