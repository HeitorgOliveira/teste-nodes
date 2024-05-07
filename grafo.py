class Pessoa:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.neighbors = []

    def add_neighbor(self, neighbor, cost):
        if neighbor.id == self.id:
            raise ValueError("Não pode adicionar a sí mesmo")
        self.neighbors.append({neighbor.id: neighbor, "custo": cost})

class Grafo:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node.nome] = node
        else:
            raise ValueError("Pessoa já cadastrada")

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
    e = Pessoa('e', 1)
    grafo.add_node(e)
    f = Pessoa('f', 2)
    grafo.add_node(f)
    g = Pessoa('g', 3)
    grafo.add_node(g)
    h = Pessoa('h', 4)
    grafo.add_node(h)

    a.add_neighbor(b, 10)
    a.add_neighbor(c, 15)
    b.add_neighbor(d, 20)
    b.add_neighbor(e, 20)
    b.add_neighbor(g, 20)
    c.add_neighbor(h, 10)
    c.add_neighbor(f, 15)
    d.add_neighbor(a, 15)
    g.add_neighbor(c, 20)
    e.add_neighbor(c, 15)
    
    

    for i in a.neighbors:
        print(i)
    
    for i in grafo.nodes:
        print(i)


if __name__ == "__main__":
    main()


def encontrar(buffer, entrada, saida):
    