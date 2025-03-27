<div align="center">
    <h1>Parser LL(1) Recursivo Descendente para expressões aritméticas</h1>
</div>

### Autor:
*Nome:* Beatriz Salgado Fernandes 

*ID:* A100602

## Descrição
O programa **calc_parser.py** implementa um parser LL(1) recursivo descendente para analisar e calcular expressões aritméticas. O objetivo deste parser é reconhecer e calcular o valor de expressões aritméticas conforme as regras definidas pela gramática.

### Operadores e Tokens Reconhecidos:
- **NUMBER**: Representa números inteiros (ex: 5, 23, -42);
- **ADD**: Operador de soma (`+`);
- **SUB**: Operador de subtração (`-`);
- **MULT**: Operador de multiplicação (`*`);
- **DIV**: Operador de divisão (`/`);
- **AP**: Parêntises de abertura (`(`);
- **FP**: Parêntises de fechamento (`)`).

## Resultado

INPUT:
```
r1= parser.parse("2+3")
r2= parser.parse("67-(2+3*4)")
r3= parser.parse("(9-2)*(13-4)")
r4= parser.parse("5-12/2")
r5= parser.parse("2*(-3+4)")
```

OUTPUT:
```
2+3= 5
67-(2+3*4)= 53
(9-2)*(13-4)= 63
5-12/2= -1.0
2*(-3+4)= 2
```