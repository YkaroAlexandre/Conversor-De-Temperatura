from time import sleep
import os

print("Ola, vou te ajudar a converter as temperaturas!")
sleep(3)
os.system('cls')

verdade =True
while(verdade):
    resposta1 =''
    while(True):
        resposta1 = input("""Escolha a primeira escala:
            1 - Celsius;
            2 - Fahrenheit;
            3 - Kelvin.
            R -> """)
        if resposta1 =="1":
            resposta1 = "Celsius"
            break
        elif resposta1 =="2":
            resposta1 = "Fahrenheit"
            break
        elif resposta1 == "3":
            resposta1 = "Kelvin"
            break
        else:
            print("Opção errada, escolha uma das opções.")
            print()
            continue

    resposta2 = ''
    while(True):
        resposta2 = input("""Escolha a segunda escala:
            1 - Celsius;
            2 - Fahrenheit;
            3 - Kelvin.
            R -> """)
        if resposta2 =="1":
            resposta2 = "Celsius"
            break
        elif resposta2 =="2":
            resposta2 = "Fahrenheit"
            break
        elif resposta2 == "3":
            resposta2 = "Kelvin"
            break
        else:
            print("Opção errada, escolha uma das opções.")
            print()
            continue
    while(True):
        print("Você escolheu de {} para {}.".format(resposta1,resposta2))
        confirmacao = input("Sim[S] ou Não[N]").upper()
        if confirmacao in ['N',"NÃO", "NAO"]:
            os.system('cls')
            print("Tudo bem, selecione a opção certa!")
            sleep(2)
            verdade = False
            os.system('cls')
            break
        elif confirmacao in ['S','SIM']:
            if resposta1 == 'Celsius':
                if resposta2 == 'Kelvin':
                    valor = float(input("Digite a temperatura: "))
                    print(f"A temperatura de {valor}º {resposta1} para {resposta2} é: {valor + 273.15:.2f} {resposta2}.")
                    break
                elif resposta2 == 'Fahrenheit':
                    valor = float(input("Digite a temperatura: "))
                    print(f"A temperatura de {valor}º {resposta1} para {resposta2} é: {(valor*9/5) + 32:.2f} {resposta2}.")
                    break
                else:
                    print(f"A temperatura de {valor}º {resposta1} para {resposta2} é: {valor:.2f} {resposta2}.")
                    break
            if resposta1 == 'Kelvin':
                if resposta2 == 'Celsius':
                    valor = float(input("Digite a temperatura: "))
                    print(f"A temperatura de {valor} {resposta1} para {resposta2} é: {valor - 273.15:.2f} {resposta2}.")
                    break
                elif resposta2 == 'Fahrenheit':
                    valor = float(input("Digite a temperatura: "))
                    print(f"A temperatura de {valor} {resposta1} para {resposta2} é: {(valor -273.15)*9/5 +32:.2f} {resposta2}.")
                    break
                else:
                    print(f"A temperatura de {valor} {resposta1} para {resposta2} é: {valor:.2f} {resposta2}.")
                    break
            if resposta1 == 'Fahrenheit':
                if resposta2 == 'Celsius':
                    valor = float(input("Digite a temperatura: "))
                    print(f"A temperatura de {valor} {resposta1} para {resposta2} é: {(valor-32) *5/9:.2f} {resposta2}.")
                    break
                elif resposta2 == 'Kelvin':
                    valor = float(input("Digite a temperatura: "))
                    print(f"A temperatura de {valor} {resposta1} para {resposta2} é: {(valor-32) *5/9 + 273.15:.2f} {resposta2}.")
                    break
                else:
                    print(f"A temperatura de {valor} {resposta1} para {resposta2} é: {valor:.2f} {resposta2}.")
                    break
                    



        else:
            print("Opção errada, escolha uma das opções.")
            print()
            continue