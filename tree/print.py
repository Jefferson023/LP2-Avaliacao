from csv import reader
from contextlib import redirect_stdout
from collections import namedtuple
from graphviz import Graph

Entrada = namedtuple("Entrada", "cod_geral area_geral cod_especifica area_especifica cod_detalhada area_detalhada codigo rotulo")
Tree = Graph(filename = "Tree.out", format = 'pdf')
Tree.attr(viewPort = '3456,998,1')
Tree.graph_attr.update(fontname = "Arial", fontsize = '36', style = "bold", label = "\n\nClassificação Brasileira de Cursos Superiores"
    , ssize = "30,60")
Tree.node_attr.update(color='grey', style = 'filled', fontname="Verdana", size="30,30")
dict_especifica = set()
dict_detalhada = set()

with open("dataset.csv", encoding="utf-8") as csvfile:
    csvfile.readline()
    for line in reader(csvfile, delimiter=";"):
        entrada = Entrada(*line)
        if (entrada.cod_especifica not in dict_especifica):
            Tree.node(str(entrada.cod_geral) + ' '+entrada.area_geral, color = 'steelblue3')
            Tree.node(str(entrada.cod_especifica)+' '+ entrada.area_especifica,color = 'gold')
            Tree.edge(str(entrada.cod_geral) + ' '+entrada.area_geral, str(entrada.cod_especifica)+' '
                + entrada.area_especifica, fillcolor='steelblue3')
            dict_especifica.add(entrada.cod_especifica)

        if (entrada.cod_detalhada not in dict_detalhada):   
            Tree.node(str(entrada.cod_detalhada) + ' '+ entrada.area_detalhada, color = 'crimson')   
            Tree.edge(str(entrada.cod_especifica) + ' '+ entrada.area_especifica, str(entrada.cod_detalhada) + ' '
                + entrada.area_detalhada, fillcolor='steelblue3')
            dict_detalhada.add(entrada.cod_detalhada)
        Tree.node(str(entrada.codigo) + ' '+ entrada.rotulo, color = 'springgreen1')
        Tree.edge(str(entrada.cod_detalhada)+ ' '+ entrada.area_detalhada, str(entrada.codigo) + ' '+ entrada.rotulo)
Tree.view()            