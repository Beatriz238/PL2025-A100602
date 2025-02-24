<div align="center">
    <h1>Somador On/Off</h1>
</div>

### Autor:
*Nome:* Beatriz Salgado Fernandes 

*ID:* A100602

## Descrição
O programa **somador_on_off** processa uma sequência de comandos em formato de texto, ativando ou desativando a soma de valores conforme as instruções "ON" e "OFF" e imprimindo a soma atual no ecrã ao ler o caracter "=".

## Regras de Funcionamento
- O somador é inicializado como desligado (`OFF`);
- Sempre que encontrar "ON", passamos a somar os números subsequentes;
- Sempre que encontrar "OFF", ele paramos de somar;
- Se encontrar "=", imprime o valor atual da soma;
- Suporta números positivos e negativos;
- Aceita comandos "ON" e "OFF" em qualquer combinação de maiúsculas e minúsculas.

## Testes
### Teste1:
```
10 On 20 OFF 5 oN -15 oFf 30 = oN 40 OFF 50 on 60 =
```
### Resultado:
```
5 105
```
### Teste2:
```
On On On 5 10 Off 20 = on 30 OFF 40 On -10 =
```
### Resultado:
```
15 35
```
### Teste3:
```
ON 12 -5 15 OFF 20 ON 86 -10 OFF = ON -3 OFF 25 ON 50 OFF = ON -20 40 -10 ON 22 OFF =
```
### Resultado:
```
98 145 177
```