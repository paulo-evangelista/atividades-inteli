# Classe que define nossa fila
class Fila():
    def __init__(self):
        # A fila começa vazia quando é instanciada
        self.fila = []

    # função que adiciona um valor no final da fila
    def add(self, value):
        self.fila.append(value)
    
    #função que retira um valor do inicio da fila e retorna-o
    def next(self):
        return self.fila.pop(0)
        
    #função que retorna True caso a fila esteja vazia
    def isEmpty(self):
        return len(self.fila) == 0

# Classe que define nossa pilha
class Pilha():
    def __init__(self):
        # A pilha começa vazia quando é instanciada
        self.pilha = []

    #função que adiciona um valor no topo da pilha
    def add(self, value):
        self.pilha.append(value)
    
    #função que retira um valor do topo da pilha e retorna-o
    def next(self):
        return self.pilha.pop()
    
    #função que retorna True caso a pilha esteja vazia
    def isEmpty(self):
        return len(self.pilha) == 0
        