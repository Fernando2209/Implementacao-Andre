import re

class AnalisadorLexico:
    def __init__(self, codigo_entrada):
        self.tokens = []
        self.posicao_atual = 0
        self.codigo_entrada = codigo_entrada
        self.especificacao_tokens = [
            ('NUM', r'\d+'),          
            ('ID', r'[a-zA-Z_]\w*'),  
            ('ATRIBUICAO', r'='),     
            ('MAIS', r'\+'),          
            ('MENOS', r'-'),          
            ('MULT', r'\*'),          
            ('DIV', r'/'),            
            ('LPAREN', r'\('),        
            ('RPAREN', r'\)'),        
            ('LCHAVE', r'\{'),        
            ('RCHAVE', r'\}'),        
            ('IGUAL', r'=='),         
            ('DIFERENTE', r'!='),     
            ('MENOR', r'<'),          
            ('MAIOR', r'>'),          
            ('IF', r'if'),            
            ('ELSE', r'else'),        
            ('ESPACO', r'\s+'),       
        ]
        self.regex_tokens = '|'.join(f'(?P<{nome}>{padrao})' for nome, padrao in self.especificacao_tokens)
    
    def tokenizar(self):
        for correspondencia in re.finditer(self.regex_tokens, self.codigo_entrada):
            tipo = correspondencia.lastgroup
            valor = correspondencia.group()
            if tipo == 'ESPACO':
                continue
            self.tokens.append((tipo, valor))
        return self.tokens
