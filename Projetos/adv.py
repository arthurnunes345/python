import random

numero = random.randrange(1,5)
print("o numero: "+str(numero))

def questao():
	quantidade = 0
	while True:
		quatidade =+1
		resposta = int(input("Digite um numero : "))
		if(numero == resposta):
			print("Parabéns você acertou!!")
		else:				 					if(resposta>numero):
					 print("sua resposta foi maior que numero secreto!")	    			                	elif(resposta<numero):
					 print("Sua reposta foi menor que o numero secreto")