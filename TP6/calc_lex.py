import ply.lex as lex

tokens= (
    "NUMBER", #e.g.: 5
    "ADD", #+
    "SUB", #-
    "MULT", #*
    "DIV", #/
    "AP", #(
    "FP" #)
)

t_ADD= r"\+"
t_SUB= r"\-"
t_MULT= r"\*"
t_DIV= r"/"
t_AP= r"\("
t_FP= r"\)"

t_ignore= " "

def t_NUMBER(t):
  r'-?\d+'
  t.value= int(t.value)
  return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Símbolo inválido na linha {t.lineno}: {t.value[0]}")
    t.lexer.skip(1)
    pass

lexer= lex.lex()
