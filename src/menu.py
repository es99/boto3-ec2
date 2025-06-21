import boto3
from ec2 import pararInstancia
from ec2 import mostraInstancias, iniciarInstancia

ec2 = boto3.client('ec2')

while True:
    choosen = input(r"""
    1. Mostrar Instâncias
    2. Parar Instância
    3. Startar Instância
    'q' - sair
""")
    match choosen:
        case "q":
            print("saindo...")
            break
        case "1":
            mostraInstancias()
        case "2":
            instancia = input("Informe o id da instância: ")
            if pararInstancia(instancia):
                print("Instancia parada com sucesso.")
        case "3":
            instancia = input("Informe o id da instância: ")
            if iniciarInstancia(instancia):
                print("Instancia iniciada com sucesso.")
        case _:
            print("Não compreendemos sua escolha...")

print("Fim do laço")