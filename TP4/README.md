<div align="center">
    <h1>Analisador Léxico para uma Linguagem de Query</h1>
</div>

### Autor:
*Nome:* Beatriz Salgado Fernandes 

*ID:* A100602

## Descrição
O programa **ana_lex.py** é um analisador léxico para uma linguagem de consulta similar à usada na DBpedia. O objetivo do analisador é dividir uma frase de consulta em tokens para ser utilizada em processamento posterior.

## Regras de Funcionamento
O analisador léxico realiza a divisão da consulta em tokens de acordo com a sintaxe da linguagem de query.
Os tokens reconhecidos são:

- VAR: Variáveis (e.g., ?nome, ?desc)
- RECURSO: Recursos como dbo:MusicalArtist e foaf:name
- STRING: Strings entre aspas (e.g., "Chuck Berry")
- TAG: Idioma para strings (e.g., @en)
- NUM: Números inteiros (e.g., 1000)
- A: a
- PONTO: Pontos finais "."
- AC: Abrir chaveta "{"
- FC: Fechar chaveta "}"
- ID: Palavras reservadas (SELECT, WHERE, LIMIT)

Devemos ainda ter em consideração os espaços brancos (" ") e as mudanças de linhas ("\n").

## Resultado
Ao executar o código com a frase de exemplo, a saída será uma lista de tokens extraídos.

Frase usada para teste:

```python
frase_exemplo="""select ?nome ?desc where {
                ?s a dbo:MusicalArtist.
                ?s foaf:name "Chuck Berry"@en .
                ?w dbo:artist ?s.
                ?w foaf:name ?nome.
                ?w dbo:abstract ?desc 
              } LIMIT 1000
              """
```

OutPut:

```python
LexToken(SELECT,'select',1,0)
LexToken(VAR,'?nome',1,7)
LexToken(VAR,'?desc',1,13)
LexToken(WHERE,'where',1,19)
LexToken(AC,'{',1,25)
LexToken(VAR,'?s',2,47)
LexToken(A,'a',2,50)
LexToken(RECURSO,'dbo:MusicalArtist',2,52)
LexToken(PONTO,'.',2,69)
LexToken(VAR,'?s',3,91)
LexToken(RECURSO,'foaf:name',3,94)
LexToken(STRING,'"Chuck Berry"',3,104)
LexToken(TAG,'@en',3,117)
LexToken(PONTO,'.',3,121)
LexToken(VAR,'?w',4,143)
LexToken(RECURSO,'dbo:artist',4,146)
LexToken(VAR,'?s',4,157)
LexToken(PONTO,'.',4,159)
LexToken(VAR,'?w',5,181)
LexToken(RECURSO,'foaf:name',5,184)
LexToken(VAR,'?nome',5,194)
LexToken(PONTO,'.',5,199)
LexToken(VAR,'?w',6,221)
LexToken(RECURSO,'dbo:abstract',6,224)
LexToken(VAR,'?desc',6,237)
LexToken(FC,'}',7,260)
LexToken(ID,'LIMIT',7,262)
LexToken(NUM,1000,7,268)
```