import requests

def obter_taxas():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']

def converter_moedas(valor, moeda_origem, moeda_destino, taxas):
    if moeda_origem in taxas and moeda_destino in taxas:
        taxa_origem = taxas[moeda_origem]
        taxa_destino = taxas[moeda_destino]
        valor_em_usd = valor / taxa_origem
        valor_convertido = valor_em_usd * taxa_destino
        return valor_convertido
    else:
        return None
    
while True:
    taxa_de_cambio = obter_taxas()
    valor = float(input("Qual o valor a ser convertido: "))
    moeda_origem = input("Qual a moeda de origem: ").upper()
    moeda_destino = input("Qual a moeda de destino: ").upper()
    


    valor_convertido = converter_moedas(valor, moeda_origem, moeda_destino, taxa_de_cambio)

    if valor_convertido is not None:
        print(f"{valor:.2f} {moeda_origem} é equivalente  a {valor_convertido:.2f} {moeda_destino}")
        
        opcao = input("Deseja encerrar? [S/N]: ").upper()
        if opcao ==  "S":
            print("Encerrando o programa")
            break
        elif opcao == "N":
            continue
    else:
        print('Moedas não encontradas ou inválidas')        
            
    

