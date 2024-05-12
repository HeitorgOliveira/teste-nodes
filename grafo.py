class Pessoa:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.neighbors = []

    def add_neighbor(self, neighbor, cost):
        if neighbor.id == self.id:
            raise ValueError("Não pode adicionar a sí mesmo")
        self.neighbors.append({"id" : neighbor.id, "neighbor": neighbor, "cost" : cost})

class Grafo:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node.nome] = node
        else:
            raise ValueError("Pessoa já cadastrada")

def bfs(entrada, saida):
    searched = []
    frontier = []

    frontier.append(entrada)
    while len(frontier):
        aux = frontier.pop()
        searched.append(aux)
        if (aux.id == saida.id):
            return searched
        else:
            for i in aux.neighbors:
                frontier.append(i["neighbor"])

def main():
    grafo = Grafo()
    a = Pessoa('a', 1)
    grafo.add_node(a)
    b = Pessoa('b', 2)
    grafo.add_node(b)
    c = Pessoa('c', 3)
    grafo.add_node(c)
    d = Pessoa('d', 4)
    grafo.add_node(d)
    e = Pessoa('e', 5)
    grafo.add_node(e)
    f = Pessoa('f', 6)
    grafo.add_node(f)
    g = Pessoa('g', 7)
    grafo.add_node(g)
    h = Pessoa('h', 8)
    grafo.add_node(h)

    a.add_neighbor(b, 10)
    a.add_neighbor(c, 15)
    b.add_neighbor(d, 10)
    b.add_neighbor(e, 10)
    c.add_neighbor(f, 10)
    f.add_neighbor(g, 10)
    g.add_neighbor(h, 10)   

    resultado = (bfs(a, c))
    for i in resultado:
        print(i.nome)



if __name__ == "__main__":
    main()
