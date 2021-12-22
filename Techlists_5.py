#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime  import datetime
import numpy
import pandas as pd

data = datetime.now()
dias = data.strftime("%D")
dia = data.strftime("%d")
horas = data.strftime("%H:%M:%S")
hora = int(data.strftime("%H"))

if(0<=hora<=4):
    turno = "Olá,boa madrugada"
if(6<=hora<=12):
    turno = "Oi,bom dia"
if(13<=hora<=18):
    turno = "Olá,boa tarde"
if(19<=hora<=23):
    turno = "Oi,boa noite"


nome = input("\n"+turno+".\nSeja-bem(a) a TechLists! uma loja de informática feita para você!\nPor favor,insira seu nome: ")
print("\nEntão "+nome+",Vamos começar a fazer algumas compras agora?\nUtilize os numeros para fazer suas compras.\n")

codigo = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12","a13","a14","a15"]
produtos = ["camera","smartphone","fone de ouvido","micro sd 32gb","capinha","pelicula","notebook","smartwatch","caixa de som bluetooth","mouse","cabo usb","carregador","capa de notebook","carregador portatil","caixa de som alexa"]
preço = [299.99,1299.99,25.00,30.79,15.90,15.80,3499.79,250.89,150.60,79.99,20.00,15.00,30.00,35.79,359.59]

listacodigo = []#meus codigos selecionados
listaprodutos = [] #meus produtos selecionados
listaquant = [] #quantidade de produtos selecionados
listaunidpreço = []#preço de uma unidade do produto
listapreço = []#preço da unidade x quantidade do produto

#adicionar item a lista
def selecionar():
    print("\n--------------------------------------------")
    print("           adicionando um produto...          ")
    pergunta=input("Digite o codigo do produto: ")
    quantidade = int(input("Digite a quantidade desejada:  "))
    if(pergunta==codigo[0]):
        listacodigo.append(codigo[0])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[0])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[0])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[0])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[1]):
        listacodigo.append(codigo[1])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[1])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[1])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[1])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[2]):
        listacodigo.append(codigo[2])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[2])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidipreço.append(preço[2])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[2])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[3]):
        listacodigo.append(codigo[3])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[3])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaundipreço.append(preço[3])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[3])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[4]):
        listacodigo.append(codigo[4])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[4])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[4])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[4])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[5]):
        listacodigo.append(codigo[5])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[5])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[5])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[5])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[6]):
        listacodigo.append(codigo[6])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[6])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[6])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[6])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[7]):
        listacodigo.append(codigo[7])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[7])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[7])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[7])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[8]):
        listacodigo.append(codigo[8])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[8])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[8])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[8])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[9]):
        listacodigo.append(codigo[9])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[9])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[9])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[9])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[10]):
        listacodigo.append(codigo[10])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[10])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[10])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[10])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[11]):
        listacodigo.append(codigo[11])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[11])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[11])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[11])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[12]):
        listacodigo.append(codigo[12])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[12])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[12])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[12])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[13]):
        listacodigo.append(codigo[13])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[13])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[13])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[13])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    if(pergunta==codigo[14]):
        listacodigo.append(codigo[14])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[14])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[14])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[14])#adiciona o preço total da minha lista
        print("Seu(s) produto(s) foi adicionado(s) com sucesso!")
        print("--------------------------------------------\n")
        return decidir()
    else:
        print("digite apenas o codigo dos produtos disponiveis")
    
    
    
def deletar():
    minhalista = pd.DataFrame(list(zip(listacodigo,listaprodutos,listaquant,listaunidpreço,listapreço)),columns = ["codigo","produtos","quant.","preço.unid","preço.total"])
    print("\n------------------------------------------------------")
    print("     Deletando um produto do carrinho....  \n ")
    print("                   meu carrinho               ")
    print("x---------------------------------------------------x   ")
    print(minhalista)
    print("x---------------------------------------------------x\n")

    numero = int(input( "Digite o numero do produto do seu carrinho: "))
    ler = len(listaprodutos)
    if(numero<=ler):
        listacodigo.pop(numero)
        listaprodutos.pop(numero)
        listaquant.pop(numero)
        listaunidpreço.pop(numero)
        listapreço.pop(numero)
        print("o produto numero "+str(numero)+", foi removido do seu carrinho.")
        print("------------------------------------------------------\n")
        return decidir()
    if(numero>ler):
        print("\n------------------------------------------------------")
        print("Digite novamente o numero do produto da sua lista")
        print(remover())
        print("------------------------------------------------------\n")
        return decidir()
    else:
        print("Digite apenas o numero dos produtos do seu carrinho!")
    
    
def exibir():
    ler = len(listaprodutos)
    minhalista = pd.DataFrame(list(zip(listacodigo,listaprodutos,listaquant,listaunidpreço,listapreço)),columns = ["codigo","produtos","quant.","preço.unid","preço.total"])
    if(ler<=0):
        print("\n-------------------------------------------")
        print("             Meu carrinho                    ")
        print(" Seu carrinho não possui produtos no momento ")
        print("\n-------------------------------------------")
        return decidir()
    else:
        print("\n-------------------------------------------------------")
        print("                       Meu carrinho                    \n")
        print(str(minhalista)+"\n")
        print("-------------------------------------------------------\n")
        return decidir()
    
def osprodutos():
    print("\n----------------------------------------")
    print("        Produtos disponiveis           ")
    loja = pd.DataFrame(list(zip(codigo,produtos,preço)),columns=["codigo","produto","preço"])
    print(str(loja))
    print("----------------------------------------\n")
    return(decidir())

def finalizar():
    total = sum(listapreço)
    cartão = 5000.00
    senha = 12345
    minhalista = pd.DataFrame(list(zip(listacodigo,listaprodutos,listaquant,listaunidpreço,listapreço)), columns = ["codigo","produtos","quant.","preço.unid","preço.total"])       
    print("\n-------------------------------------------------------")
    print("                 Finalizando sua compra...             \n")
    print("                    meu carrinho                         ")
    print("x-------------------------------------------------x")
    print(str(minhalista)+"\n")
    print("x------------------------------------------------ x")
    print("Total da sua compra: R$"+str(total)+"\n")
    print(" ______________________                    ")
    print("|======================|       Saldo     ")
    print("|             ______   |      R$"+str(cartão))
    print("| Listcard    | \U0001F61c |   |            ")
    print("| 0000-0001   ------   |                   ")
    print("|______________________|                  \n")
    
    if(dia==25 and mes==12):
        desconto = total*0.25
        total= total-desconto
        msg = "Feliz natal! Parabéns "+nome+",\n voce acaba de ganhar 25% de desconto na sua compra"
    else:
        msg ="infelizmente ,voce não possui desconto nesta compra :("
    
    print("Desconto: "+msg)
    
    x = 0
    while x<5:
        x+=1
        restante = cartão-total
        usuario = int(input("\ndigite a senha do cartão: \n[\U0001F511]"))
        if(usuario==senha and restante>0):
            print("\n"+nome+",Sua compra foi realizada com sucesso!")
            print("\nx-----------------x Cupom Fiscal x--------------------x")
            print("                       TECHLISTS                        ")
            print(" Data:  "+str(dias)+"                   Horário:  "+str(horas))
            print("                       produtos                        \n")
            print(str(minhalista)+"\n")
            print("Total da compra: R$"+str(total))
            print("cliente:"+nome)
            print("Valor restante do seu cartão: R$"+str(restante))
            print("x-----------------------------------------------------x\n")
            print("Nós da TechLists agradeçemos pela sua preferencia, volte sempre!")
            break
            return decidir()
        if(usuario==senha and restante<0):
            print("\nOps!, voce não tem saldo suficiente para realizar esta compra,\nrealize uma nova compra ou remova um item do seu carrinho")
            b
            return decidir()
        if(usuario!=senha):
            print("senha incorreta,digite sua senha novamente...")
            continue
    
          
          
def decidir(): 
    while True:
        print("[1] Produtos disponiveis\n[2] Adicionar produto\n[3] Remover produtos\n[4] Meu carrinho\n[5] Finalizar minha compra\n[6] Assitencia Tecnica")
        decisao = input("Clinte "+nome+": ")
        if (decisao== "1"):
            print(osprodutos())
        if (decisao== "2"):
                print(selecionar())
        if (decisao== "3"):
                print(deletar())
        if (decisao== "4"):
                print(exibir())
        if (decisao== "5"):
                print(finalizar())
        if (decisao== "6"):
                print("\nEste serviço estará disponivel em breve...\n")
        else:
            print("\nDigite apenas os numeros disponiveis.\n")

                
print(decidir())


# In[ ]:




