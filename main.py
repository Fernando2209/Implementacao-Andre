from analisador_lexico import AnalisadorLexico
from tabela_simbolos import TabelaSimbolos
from analisador_sintatico import AnalisadorSintaticoLL1

# Exemplo de código de entrada
codigo = """
x = 10
y = 20
if (x < y) {
    x = x + 1
} else {
    y = y - 1
}
"""

# Etapas de análise
analisador_lexico = AnalisadorLexico(codigo)
tokens = analisador_lexico.tokenizar()
tabela_simbolos = TabelaSimbolos()
analisador_sintatico = AnalisadorSintaticoLL1(tokens, tabela_simbolos)

# Executar análise
analisador_sintatico.analisar()

# Mostrar tabela de símbolos final
print(tabela_simbolos.simbolos)
