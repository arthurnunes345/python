# -*- coding: utf-8 -*-
"""
Created on Mon May 10 07:06:42 2021

@author: arthur nunes carvalho santos
"""
# AVISO: a porcentagem da iluminação nao é algo exato, e sim aproximado ao valor real
# esse programa foi feito para funcionar durante o mes
# alterações devem ser feita comforme os mesesse passam
from datetime import datetime
data= datetime.now()
data_print =int(data.strftime("%d")) # o dia atual do calendario
hora = data.strftime("%H:%M") # a horário atual
dia = data_print
# variaveis que determina o inicio e o terminio de uma fase lunar
# exemplo : nova = 2(começa no dia 2)
# exemplo : nova2 = 9 (termina no dia 9)
nova = 11
nova2 = 18
crescente = 19
crescente2 = 25
cheia = 26
cheia2 = 31
minguante = 3
minguante2 = 10

# função da lua nova
def fase_nova(tempo = 0, dia = data_print):
    tempo
    dia
# Dias em que lua nova começa e termina.
    if dia==11:
        tempo = 0
    if dia==12:
      	tempo = 0
    if dia==13:
      	tempo = 1
    if dia==14:
      	tempo = 2	
    if dia==15:
      	tempo = 3
    if dia==16:
      	tempo = 4
    if dia==17:
        tempo = 5
    if dia==18:
        tempo = 6
    a = tempo*6.6
    z=f'{a:.2f}'
    resposta ="luminosidade:"+str(z)+"%"
    print(resposta)

# função da lua crescente
def fase_crescente(tempo = 0, dia = data_print):
    tempo
    dia
# dias em que a lua crescente começa e termina.
    if dia==19:
        tempo = 7
    if dia==20:
      	tempo = 8
    if dia==21:
      	tempo = 9
    if dia==22:
      	tempo = 10
    if dia==23:
      	tempo = 11
    if dia==24:
      	tempo = 12
    if dia==25:
        tempo = 13
    a = tempo*6.6
    z=f'{a:.2f}'
    resposta ="luminosidade:"+str(z)+"%"
    print(resposta)

# dias em que a lua cheia e minguante , em que começa e termina.
def fase_cheia_minguante():
 dia
 d = 0
 
 if dia==26:
  print(str(100)+"%")
  
 if dia==27:
 	d=1
  
 if dia==28:
 	d=2
 	
 if dia==29:
 	d=3
  
 if dia==30:
 	d=4
  
 if dia==31:
 	d=5
  
 if dia==53:
 	d=6
     #aqui já começa a fase da lua minguante
 if dia==3:
 	d=8
  
 if dia==4:
     d = 9
     
 if dia == 5:
    d =10
    
 if dia==6:
     d = 11 
  
 if dia==7:
 	 d=12
  
 if dia==8:
 	d=13
  
 if dia==9:
 	d=14
     
 if dia==10:
     d=15
 	
 calculo= 6.66*d
 e = 100.00 - calculo
 d=f'{e:.2f}'
 print(" luminosidade:"+str(d)+"%")


# aqui e onde o dia e a hora serão manipulados 
if nova2>=data_print>=nova:
	print(" Hoje é "+str(dia)+" de maio, ás "+hora+" hrs.\n fase atual: Nova\n próxima fase: Crescente\n",fase_nova(tempo = 0, dia = data_print))
    
    
if crescente2>=data_print>=crescente:
	print(" Hoje é "+str(dia)+" de maio, ás "+hora+" hrs.\n fase atual: crescente\n próxima fase: Cheia\n", fase_crescente(tempo = 0, dia = data_print))
    
    
if  cheia2>=data_print>=cheia:
	print(" Hoje é "+str(dia)+" de maio, ás "+hora+" hrs.\n fase atual: Cheia\n próxima fase: Minguante\n",fase_cheia_minguante())
    
    
    
if minguante2>=data_print>=minguante:
	print(" Hoje é "+str(dia)+" de maio, ás "+hora+" hrs.\n fase atual: Minguante\n próxima fase: Nova \n" , fase_cheia_minguante())
    
if data_print>32:
	print("erro de calculo")

          
    