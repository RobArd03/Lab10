import networkx as nx
from database.DAO import DAO


class Model:

    def __init__(self):
        self._annoI = 1816
        self._annoF = 2016
        self._nodes = []
        self._grafo=nx.Graph()
        self._idMap = {}
        self._strMap = {}


    def buildGraph(self, year: int):
        """"
        Crea il grafo
        """
        self.addNodes(year)
        self.setEdges(year)
        self.getConfinanti(year)


    def addNodes(self, year: int):
        """
        aggiunge tutti i nodi del grafico minori uguali del anno specificato
        """
        self._nodes.extend(DAO.getAllNodes(year))
        self._grafo.add_nodes_from(self._nodes)
        for n in self._nodes:
            self._idMap[n.getIdState()] = n
            self._strMap[n.getStrState()]= n



    def getNodes(self):
        return self._nodes

    def numeroCompConnesse(self):
        print(len(self._grafo.nodes), len(self._grafo.edges))
        return nx.number_connected_components(self._grafo)

    def setEdges(self, year: int):
        """
        aggiunge tutti gli archi del grafo
        """
        collegamenti = DAO.getAllEdges(year)
        for c in collegamenti:
            self._grafo.add_edge(c.stato1, c.stato2)

    def getConfinanti(self, year):
        for c in DAO.getConfinanti(year):
            (idState , count) = c
            self._idMap[idState].setCollegamenti(count)


    def getIdMap(self):
        return self._idMap


    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)


    def hasAnno(self, idAnno: int):
        return idAnno >= self._annoI and idAnno <= self._annoF

    def getNodesConn(self, source):

        conn = nx.node_connected_component(self._grafo, self._strMap[source])
        return conn


