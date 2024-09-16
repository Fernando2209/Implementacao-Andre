class AnalisadorSintaticoLL1:
    def __init__(self, tokens, tabela_simbolos):
        self.tokens = tokens
        self.token_atual = None
        self.posicao_atual = -1
        self.tabela_simbolos = tabela_simbolos
        self.proximo_token()
    
    def proximo_token(self):
        self.posicao_atual += 1
        if self.posicao_atual < len(self.tokens):
            self.token_atual = self.tokens[self.posicao_atual]
        else:
            self.token_atual = ('EOF', '')
    
    def combinar(self, tipo_esperado):
        if self.token_atual[0] == tipo_esperado:
            self.proximo_token()
        else:
            raise SyntaxError(f"Esperado {tipo_esperado}, encontrado {self.token_atual[0]}")
    
    def analisar(self):
        self.programa()
    
    def programa(self):
        while self.token_atual[0] != 'EOF':
            self.declaracao()
    
    def declaracao(self):
        if self.token_atual[0] == 'ID':
            self.atribuicao()
        elif self.token_atual[0] == 'IF':
            self.condicional()
        else:
            raise SyntaxError(f"Token inesperado {self.token_atual[0]}")
    
    def atribuicao(self):
        identificador = self.token_atual[1]
        self.combinar('ID')
        self.combinar('ATRIBUICAO')
        valor = self.expressao()
        self.tabela_simbolos.adicionar(identificador, valor)
    
    def expressao(self):
        resultado = self.termo()
        while self.token_atual[0] in ('MAIS', 'MENOS'):
            if self.token_atual[0] == 'MAIS':
                self.combinar('MAIS')
                resultado += self.termo()
            elif self.token_atual[0] == 'MENOS':
                self.combinar('MENOS')
                resultado -= self.termo()
        return resultado
    
    def termo(self):
        resultado = self.fator()
        while self.token_atual[0] in ('MULT', 'DIV'):
            if self.token_atual[0] == 'MULT':
                self.combinar('MULT')
                resultado *= self.fator()
            elif self.token_atual[0] == 'DIV':
                self.combinar('DIV')
                resultado //= self.fator()
        return resultado
    
    def fator(self):
        if self.token_atual[0] == 'NUM':
            valor = int(self.token_atual[1])
            self.combinar('NUM')
            return valor
        elif self.token_atual[0] == 'ID':
            identificador = self.token_atual[1]
            self.combinar('ID')
            valor = self.tabela_simbolos.obter(identificador)
            if valor is None:
                raise NameError(f"Variável {identificador} não definida")
            return valor
        elif self.token_atual[0] == 'LPAREN':
            self.combinar('LPAREN')
            resultado = self.expressao()
            self.combinar('RPAREN')
            return resultado
        else:
            raise SyntaxError(f"Token inesperado {self.token_atual[0]}")
    
    def condicional(self):
        self.combinar('IF')
        self.combinar('LPAREN')
        resultado_condicao = self.condicao()
        self.combinar('RPAREN')
        self.combinar('LCHAVE')
        if resultado_condicao:
            self.programa()
        self.combinar('RCHAVE')
        if self.token_atual[0] == 'ELSE':
            self.combinar('ELSE')
            self.combinar('LCHAVE')
            if not resultado_condicao:
                self.programa()
            self.combinar('RCHAVE')
    
    def condicao(self):
        esquerda = self.expressao()
        if self.token_atual[0] == 'IGUAL':
            self.combinar('IGUAL')
            direita = self.expressao()
            return esquerda == direita
        elif self.token_atual[0] == 'DIFERENTE':
            self.combinar('DIFERENTE')
            direita = self.expressao()
            return esquerda != direita
        elif self.token_atual[0] == 'MENOR':
            self.combinar('MENOR')
            direita = self.expressao()
            return esquerda < direita
        elif self.token_atual[0] == 'MAIOR':
            self.combinar('MAIOR')
            direita = self.expressao()
            return esquerda > direita
