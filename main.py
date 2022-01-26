import requests

def main():
    print("###################")
    print("### Consulta CEP ###")
    print("###################")

    cep_input = input("\nDigite o Cep\n")

    if len(cep_input) != 8:
        print("Quantidade de dígitos inválida")
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    print()
    print("Resultado:")

    resultado = request.json()
    if('erro' not in resultado):    
        for i in resultado:        
            print(f"{i} : {resultado[i]}")
    else:
        print("Cep inválido")

    opcao = int(input("Deseja realizar outra consulta\n 1 - sim\n 2 - não\n"))
    if opcao == 1:
        main()
    

if __name__ == '__main__':
    main()