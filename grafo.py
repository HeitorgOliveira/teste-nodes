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

    a.add_neighbor(b, 10)
    a.add_neighbor(c, 15)

    for i in a.neighbors:
        print(i)
    
    for i in grafo.nodes:
        print(i)


if __name__ == "__main__":
    main()
