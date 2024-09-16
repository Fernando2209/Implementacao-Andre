class TabelaSimbolos:
    def __init__(self):
        self.simbolos = {}
    
    def adicionar(self, identificador, valor):
        self.simbolos[identificador] = valor
    
    def obter(self, identificador):
        return self.simbolos.get(identificador, None)
