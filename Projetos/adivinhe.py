import random
x  = 0
while x < 3:
	x+=1
	resposta = random.randint(1, 10)
	print(str(x)+"° tentativa:")
	pergunta  = int(input("adivinhe um numero: "))
	if(pergunta==resposta):
		print("parabens!! voce acertou")
		break
	if(pergunta!=resposta and x==1):
		print("resposta errada, tente novamente")
	if(pergunta!=resposta and x==2):
		print("sua ultima tentiva...")
	if(pergunta!=resposta and x==3):
		print("reposta errada , boa sorte na proxima vez")
		
	
	