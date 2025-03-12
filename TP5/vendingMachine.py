import json
import re
from datetime import datetime

STOCK_FILE = "Stock.json"

def carregar_stock():
    try:
        with open(STOCK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_stock(stock):
    with open(STOCK_FILE, "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4)

def listar_produtos(stock):
    print("maq:")
    print("cod | nome | quantidade | preço")
    print("-" * 40)
    for produto in stock:
        print(f"{produto['cod']} | {produto['nome']} | {produto['quant']} | {produto['preco']:.2f}e")

def processar_moedas(saldo_atual, moedas):
    saldo_euros = 0
    saldo_centavos = 0
    moedas_validas = {'5c': 5, '10c': 10, '20c': 20, '50c': 50, '1e': 1, '2e': 2}
    for moeda in moedas:
        moeda_lower = moeda.lower()
        if moeda_lower in moedas_validas:
            valor = moedas_validas[moeda_lower]
            if moeda_lower.endswith('e'):
                saldo_euros += valor
            elif moeda_lower.endswith('c'):
                saldo_centavos += valor
        else:
            print(f"maq: Moeda inválida: {moeda}")
    saldo_atual += saldo_euros * 100 + saldo_centavos
    return saldo_atual

def selecionar_produto(stock, saldo, cod_produto):
    for item in stock:
        if item["cod"] == cod_produto:
            if item["quant"] > 0:
                if saldo >= int(item["preco"] * 100):
                    item["quant"] -= 1
                    saldo -= int(item["preco"] * 100)
                    print(f"maq: Pode retirar o produto dispensado \"{item['nome']}\"")
                    print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c")
                else:
                    print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c; Pedido = {int(item['preco'] * 100) // 100}e{int(item['preco'] * 100) % 100}c")
                return saldo
            else:
                print("maq: Produto fora de stock.")
                return saldo
    print("maq: Produto não existe.")
    return saldo

def calcular_troco(saldo):
    moedas = {200: "2e", 100: "1e", 50: "50c", 20: "20c", 10: "10c", 5: "5c"}
    troco = {}
    for valor, nome in moedas.items():
        if saldo >= valor:
            troco[nome] = saldo // valor
            saldo %= valor
    return troco

def main():
    stock = carregar_stock()
    saldo = 0
    print(f"maq: {datetime.now().date()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    print("maq: Escolha dos seguintes comandos:")
    print("1. LISTAR (lista todos os produtos da máquina)")
    print("2. MOEDA (Ex.: MOEDA 1e 50c - colocar dinheiro na máquina)")
    print("3. SELECIONAR (Ex.: SELECIONAR E11 - seleciona o produto que quer comprar)")
    print("4. SAIR (devolve-lhe o troco)\n")

    while True:
        comando = input("\n>> ").strip().upper()

        if comando == "LISTAR":
            listar_produtos(stock)
        
        elif comando.startswith("MOEDA"):
            moedas = comando.split()[1:]
            if len(moedas) == 1:
                saldo = processar_moedas(saldo, [moedas[0]])  
            else:
                saldo = processar_moedas(saldo, moedas)  
            print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c") 
        
        elif comando.startswith("SELECIONAR"):
            partes = comando.split()
            if len(partes) > 1:
                saldo= selecionar_produto(stock, saldo, partes[1])
            else:
                print("maq: Código de produto inválido")
        elif comando == "SAIR":
            troco = calcular_troco(saldo)
            troco_str = ", ".join([f"{qtd}x {moeda}" for moeda, qtd in troco.items()])
            print(f"maq: Pode retirar o troco: {troco_str}.")
            print("maq: Até à próxima!")
            guardar_stock(stock)
            break
        
        else:
            print("maq: Comando inválido.")

if __name__ == "__main__":
    main()
