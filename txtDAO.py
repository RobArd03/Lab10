from database.DAO import DAO

nodes = DAO.getAllNodes(2016)
for n in nodes:
    print(n)


edges = DAO.getAllEdges(2016)
for e in edges:
    print(e)




print(f"N nodi: {len(nodes)}, N edge: {len(edges)}")

