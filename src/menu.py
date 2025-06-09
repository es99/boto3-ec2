import boto3
from ec2 import mostraInstancias

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
            print("opcao 2 escolhida.")
            break
        case "3":
            print("opcao 3 escolhida.")
            break
        case _:
            print("Não compreendemos sua escolha...")

print("Fim do laço")