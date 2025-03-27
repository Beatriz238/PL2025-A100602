import ply.yacc as yacc

from calc_lex import tokens

def p_operacao_1(p):
    "operacao : calc"
    p[0]=p[1]

def p_operacao_2(p):
    "operacao : operacao ADD calc"
    p[0]= p[1]+p[3]

def p_operacao_3(p):
    "operacao : operacao SUB calc"
    p[0]=p[1]-p[3]

def p_calc_1(p):
    "calc : expressao"
    p[0]=p[1]

def p_calc_2(p):
    "calc : calc MULT expressao"
    p[0]= p[1]*p[3]

def p_calc_3(p):
    "calc : calc DIV expressao"
    p[0]= p[1]/p[3]

def p_expressao_1(p):
    "expressao : NUMBER"
    p[0]=p[1]

def p_expressao(p):
    "expressao : AP operacao FP"
    p[0]=p[2]

def p_error(p):
    print("Erro sintático no input!")

parser=yacc.yacc()

r1= parser.parse("2+3")
r2= parser.parse("67-(2+3*4)")
r3= parser.parse("(9- 2)*(13- 4)")
r4= parser.parse("5- 12/2")
r5= parser.parse("2*(-3+4)")

print("2+3=",r1)
print("67-(2+3*4)=",r2)
print("(9-2)*(13-4)=",r3)
print("5-12/2=",r4)
print("2*(-3+4)=",r5)