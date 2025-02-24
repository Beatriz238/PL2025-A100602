import re

def ler_dataset(nome_arquivo):
    with open(nome_arquivo, encoding="utf-8") as f:
        linhas = f.readlines()[1:]  # Ignorar a primeira linha (cabeçalho)

    records = []
    buffer = ""

    for line in linhas:
        buffer += " " + line.strip()
        if buffer.count(";") >= 6:  # Linha completa (7 campos = 6 separadores)
            fields = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', buffer.strip())
            records.append([field.strip().strip('"') for field in fields])
            buffer = ""

    return records

def lista_compositores(dados):
    compositores = sorted(set(linha[4] for linha in dados if linha[4].strip()))
    return compositores

def distribuicao_obras_por_periodo(dados):
    distribuicao = {}
    for linha in dados:
        periodo = linha[3].strip()
        if periodo:
            distribuicao[periodo] = distribuicao.get(periodo, 0) + 1
    return distribuicao

def obras_por_periodo(dados):
    obras = {}
    for linha in dados:
        periodo = linha[3].strip()
        titulo = linha[0].strip()
        if periodo and titulo:
            if periodo not in obras:
                obras[periodo] = []
            obras[periodo].append(titulo)

    for periodo in obras:
        obras[periodo].sort()

    return obras

def main():
    nome_arquivo = 'obras.csv'
    dados = ler_dataset(nome_arquivo)

    print("Lista de compositores:", lista_compositores(dados))
    print('\n')
    print("Distribuição por período:", distribuicao_obras_por_periodo(dados))
    print('\n')
    print("Obras por período:", obras_por_periodo(dados))

if __name__ == "__main__":
    main()
