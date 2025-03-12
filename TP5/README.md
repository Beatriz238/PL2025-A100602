<div align="center">
    <h1>Máquina de Vending</h1>
</div>

### Autor:
*Nome:* Beatriz Salgado Fernandes 

*ID:* A100602

## Descrição
O programa **vendingMachine.py** simula o funcionamento de uma máquina de vendas automática. Este permite que o utilizador visualize os produtos disponíveis na máquina, insira moedas, selecione itens para compra e, ao sair, receba troco, tudo através de comandos interativos.

## Regras de Funcionamento
O simulador segue as seguintes regras:  

- **LISTAR**: Exibe a lista de produtos disponíveis na máquina, incluindo código, nome, quantidade e preço.  
- **MOEDA X**: Permite ao utilizador inserir moedas válidas na máquina. São aceitas: `5c`, `10c`, `20c`, `50c`, `1e`, `2e`.  
- **SELECIONAR [CÓDIGO]**: Seleciona um produto da máquina pelo código. Se tiver saldo suficiente e o item estiver disponível, ele será comprado e decrementamos a quantidade do produto selecionado. Se não tiver saldo suficiente, a compra não é efetuada.
- **SAIR**: Finaliza a sessão e devolve o troco com a menor quantidade possível de moedas.  

## Estrutura do Stock
O stock é carregado de um ficheiro **Stock.json**, que contém todos os produtos. Estes são armazenado como uma lista de objetos, com os seguintes atributos: **código**, **nome**, **quantidade** e **preço**.

```
stock = [
{"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
...
]
```

## Resultado

### Exemplo de uso:

```
python3 vendingMachine.py

maq: 2025-03-12, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
maq: Escolha dos seguintes comandos:
1. LISTAR (lista todos os produtos da máquina)
2. MOEDA (Ex.: MOEDA 1e 50c - colocar dinheiro na máquina)
3. SELECIONAR (Ex.: SELECIONAR E11 - seleciona o produto que quer comprar)
4. SAIR (devolve-lhe o troco)


>> LISTAR
maq:
cod | nome | quantidade | preço
----------------------------------------
A23 | Água 0.5L | 8 | 0.70e
B24 | Refrigerante 330ml | 5 | 1.20e
C25 | Batatas Fritas | 10 | 1.00e
D26 | Chocolate | 3 | 1.10e
E27 | Pacote de Bolachas | 0 | 0.65e
F28 | Sumo de Laranja | 9 | 1.40e
G29 | Barrita de Cereais | 12 | 0.50e
H30 | Misto | 3 | 1.80e
I31 | Croissant | 8 | 1.80e

>> MOEDA 1e 20c 5c 5c
maq: Saldo = 1e30c

>> SELECIONAR A23
maq: Pode retirar o produto dispensado "Água 0.5L"
maq: Saldo = 0e60c

>> SELECIONAR A23
maq: Saldo insuficiente para satisfazer o seu pedido
maq: Saldo = 0e60c; Pedido = 0e70c

>> SELECIONAR J32
maq: Produto não existe.

>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 10c.
maq: Até à próxima!
```