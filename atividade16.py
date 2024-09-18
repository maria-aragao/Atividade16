# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
altura, peso = int(input("informe sua altura")), int(input("informe o seu peso"))

IMC = peso / (altura * 2)

if IMC < 18.5:
    print("Você está abaixo do peso")

elif 18.5<= IMC <25:
    print("Você está com peso normal!")

elif 25 <= IMC < 30:
    print("Você está sobrepeso")

elif IMC >= 30:
    print("Você está com obesidade")