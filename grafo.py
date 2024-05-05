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
    heitor = Pessoa('Heitor', 1)
    grafo.add_node(heitor)
    marco = Pessoa('Marco', 2)
    grafo.add_node(marco)
    renato = Pessoa('Renato', 3)
    grafo.add_node(renato)

    heitor.add_neighbor(marco, 10)
    heitor.add_neighbor(renato, 15)

    for i in heitor.neighbors:
        print(i)
    
    for i in grafo.nodes:
        print(i)


if __name__ == "__main__":
    main()
