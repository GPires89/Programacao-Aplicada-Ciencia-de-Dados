import subprocess as spr
import time

while True:
    spr.run("cls", shell=True)#Limpa a tela
    print("="*25)
    print("**** Menu Principal ****")
    print("="*25)
    print("1- Área do triângulo")
    print("2- Todos os Calculos")
    print("3- Par ou impar")
    print("4- Comparar números")
    print("5- Fases da vida")
    print("6- Contador de números")
    print("7- Repetição")
    print("8- Tabuada")
    print("9- Lista")
    print("10- String")
    print("11- Lista de Palavras")
    print("12- Exercícios")
    print("0- Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        spr.run(["python", "1-area_triangulo.py"])
    elif opcao == "2":
        spr.run(["python", "2-todos_calculos.py"])
    elif opcao == "3":
        spr.run(["python", "3-par_impar.py"])
    elif opcao == "4":
        spr.run(["python", "4-compara_numeros.py"])
    elif opcao == "5":
        spr.run(["python", "5-fase_vida.py"])
    elif opcao == "6":
        spr.run(["python", "6-Contador.py"])
    elif opcao == "7":
        spr.run(["python", "7-repeticao_for.py"])
    elif opcao == "8":
        spr.run(["python", "8-tabuada_de_um_numero.py"])
    elif opcao == "9":
        spr.run(["python", "9-lista.py"])
    elif opcao == "10":
        spr.run(["python", "10-string.py"])
    elif opcao == "11":
        spr.run(["python", "11-lista_palavras.py"])
    elif opcao == "12":
        spr.run(["python", "12-Exercicio_com_lista.py"])
    elif opcao == "0":
        break
    else:
        print("\n[***Opção inválida]")
    time.sleep(3)
        

