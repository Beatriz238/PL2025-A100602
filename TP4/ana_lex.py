import ply.lex as lex

# DBPedia: obras de Chuck Berry
frase_exemplo= """select ?nome ?desc where {
                    ?s a dbo:MusicalArtist.
                    ?s foaf:name "Chuck Berry"@en .
                    ?w dbo:artist ?s.
                    ?w foaf:name ?nome.
                    ?w dbo:abstract ?desc 
                } LIMIT 1000
                """

# Palavras reservadas
reserved = {
    'select': 'SELECT',
    'where': 'WHERE',
    'limit': 'LIMIT'
}

tokens=[
    "VAR", # ?nome, ?desc
    "RECURSO", # dbo:MusicalArtist, foaf:name
    "STRING",  # "Chuck Berry"
    "TAG", # @en
    "NUM",  # 1000
    "A", #a
    "PONTO", #.
    "AC", #{
    "FC", #}
    "ID" #palavras reservadas
]+ list(reserved.values())

t_TAG = r"@[a-z]{2}"
t_PONTO= r"\."
t_AC= r"\{"
t_FC= r"\}"

t_ignore=" " #string -> conjunto de caracteres

def t_VAR(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_RECURSO(t):
    r'[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z_][a-zA-Z0-9_-]*'
    return t

def t_STRING(t):
    r'"[^"]*"'
    return t

def t_A(t):
    r'\ba\b'
    return t

def t_NUM(t):
  r'-?\d+'
  t.value= int(t.value)
  return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Símbolo inválido na linha {t.lineno}: {t.value[0]}")
    t.lexer.skip(1)
    pass

lexer= lex.lex()

lexer.input(frase_exemplo)

#Lê tds os tokens
while tok := lexer.token():
    print(tok)