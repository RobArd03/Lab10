from model.model import Model


mymodel = Model()
mymodel.buildGraph(2016)
edges = mymodel._grafo.edges()
nodes = mymodel._grafo.nodes()
print(len(nodes))
print(len(edges))


