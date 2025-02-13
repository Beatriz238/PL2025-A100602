def somador_on_off(texto):
    somador= False
    res= 0  
    list= [] 

    palavras = texto.split() #divide texto nos espaços (cada separação conta como 1 palavra)

    for palavra in palavras:
        palavra_min = palavra.lower()  #passamos para minúsculas para o caso de termos combinações aleatórias de maiusculas e minusculas

        if palavra_min == "off":  
            somador = False  #desliga a soma
        elif palavra_min == "on":  
            somador = True  #liga a soma
        elif palavra == "=":  
            list.append(str(res))
        elif somador and palavra.lstrip("+-").isdigit():  
            res += int(palavra)

    return " ".join(list)

def main():
    teste1= "10 On 20 OFF 5 oN -15 oFf 30 = oN 40 OFF 50 on 60 ="
    teste2= "On On On 5 10 Off 20 = on 30 OFF 40 On -10 ="
    teste3= "ON 12 -5 15 OFF 20 ON 86 -10 OFF = ON -3 OFF 25 ON 50 OFF = ON -20 40 -10 ON 22 OFF ="

    print(somador_on_off(teste1))
    print(somador_on_off(teste2))
    print(somador_on_off(teste3))

main()
