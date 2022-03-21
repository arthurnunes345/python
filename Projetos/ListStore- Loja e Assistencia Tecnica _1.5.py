#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd # para gerar o dataframe
import numpy as np # para usarmos os valores das listas, pois listas sao mais faceis de trabalhar
from datetime  import datetime
data = datetime.now()
dias = data.strftime("%D")
dia = int(data.strftime("%d"))
horas = data.strftime("%H:%M:%S")
hora = int(data.strftime("%H"))
if(0<=hora<=12):
    turno = "Bom dia"
if(13<=hora<=18):
    turno = "Bom tarde"
if(19<=hora<=23):
    turno = "Bom noite"



codigo = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12","a13","a14","a15"]
produtos = ["camera","smartphone","fone de ouvido","micro sd 32gb","capinha","pelicula","notebook",
 "smartwatch","caixa de som bluetooth","mouse","cabo usb","carregador","capa de notebook",
"carregador portatil","caixa de som alexa"]
preço = [299.99,1299.99,25.00,30.79,15.90,15.80,3499.79,250.89,
        150.60,79.99,20.00,15.00,30.00,35.79,359.59]

loja = pd.DataFrame(list(zip(codigo,produtos,preço)), columns = ["codigo","produtos","preço"]) #codigo para imprimir a tabela

listacodigo = []#meus codigos selecionados
listaprodutos = [] #meus produtos selecionados
listaquant = [] #quantidade de produtos selecionados
listaunidpreço = []#preço de uma unidade do produto
listapreço = []#preço da unidade x quantidade do produto


# ## adicionar item a lista

# In[ ]:


def selecionar():
    pergunta=input("digite o codigo do produto: ")
    quantidade = int(input("digite a quantidade do produto desejado: "))
    if(pergunta==codigo[0]):
        listacodigo.append(codigo[0])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[0])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[0])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[0])#adiciona o preço total da minha lista
    if(pergunta==codigo[1]):
        listacodigo.append(codigo[1])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[1])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[1])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[1])#adiciona o preço total da minha lista
    if(pergunta==codigo[2]):
        listacodigo.append(codigo[2])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[2])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaundipreço.append(preço[2])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[2])#adiciona o preço total da minha lista
    if(pergunta==codigo[3]):
        listacodigo.append(codigo[3])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[3])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaundipreço.append(preço[3])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[3])#adiciona o preço total da minha lista
    if(pergunta==codigo[4]):
        listacodigo.append(codigo[4])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[4])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[4])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[4])#adiciona o preço total da minha lista
    if(pergunta==codigo[5]):
        listacodigo.append(codigo[5])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[5])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[5])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[5])#adiciona o preço total da minha lista
    if(pergunta==codigo[6]):
        listacodigo.append(codigo[6])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[6])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[6])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[6])#adiciona o preço total da minha lista
    if(pergunta==codigo[7]):
        listacodigo.append(codigo[7])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[7])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[7])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[7])#adiciona o preço total da minha lista
    if(pergunta==codigo[8]):
        listacodigo.append(codigo[8])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[8])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[8])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[8])#adiciona o preço total da minha lista
    if(pergunta==codigo[9]):
        listacodigo.append(codigo[9])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[9])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[9])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[9])#adiciona o preço total da minha lista
    if(pergunta==codigo[10]):
        listacodigo.append(codigo[10])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[10])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[10])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[10])#adiciona o preço total da minha lista
    if(pergunta==codigo[11]):
        listacodigo.append(codigo[11])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[11])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[11])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[11])#adiciona o preço total da minha lista
    if(pergunta==codigo[12]):
        listacodigo.append(codigo[12])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[12])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[12])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[12])#adiciona o preço total da minha lista
    if(pergunta==codigo[13]):
        listacodigo.append(codigo[13])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[13])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[13])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[13])#adiciona o preço total da minha lista
    if(pergunta==codigo[14]):
        listacodigo.append(codigo[14])#adiciona o codigo a minha lista
        listaprodutos.append(produtos[14])#adiciona o produto a minha lista
        listaquant.append(quantidade)#adiciona a quantidade a minha lista
        listaunidpreço.append(preço[14])#adiciona o preço da unidade a minha lista
        listapreço.append(quantidade*preço[14])#adiciona o preço total da minha lista
        
    
    selecione =input("voce deseja adicionar mais produto?")
    print("[s] Sim\n[n] Não")
    if(selecione=="s"or"Sim"or"SIM"or"sim"or"si"):
        print(selecionar())
    if(slecione=="n"or"Não"or"nao"or"Nao"or"N"or"não"):
        return "seu(s) produto(s), foram adicionado(s) com sucesso!"
        print(decidir())


# ## remover item da lista
# 

# In[3]:


def remover():
    print(loja)
    numero = int(input( "Digite o numero do produto do seu carrinho: "))
    numero = numero - 1
    ler = len(listaprodutos)
    if(numero<=ler):
        listacodigo.pop(numero)
        listaprodutos.pop(numero)
        listaquant.pop(numero)
        listaunidpreço.pop(numero)
        listapreço.pop(numero)
        
    print("o produto numero"+str(numero)+", foi removido da sua lista.")
    if(numero>ler):
        print("digite novamente o numero do produto da sua lista")
        print(remover())
        
    return decidir()
        


# ## exibir quantidade de produtos

# In[145]:


def exibir():
    minhalista = pd.DataFrame(list(zip(listacodigo,listaprodutos,listaquant,listaunidpreço,listapreço)),columns = ["codigo","produtos","quant.","preço.unid","preço.total"])
    print(minhalista)#vai exibir minha lista de compras
    return decidir()


# In[5]:


def osprodutos():
    print("carregando os produtos disponiveis")
    print(loja)
    return(decidir())


# ## decidir os comandos

# In[37]:


def decidir(): 
    while True:
        print("[1] Produtos disponiveis na loja\n[2] Adicionar produto\n[3] Remover produtos\n[4] Meu carrinho\n[5] Finalizar minha compra\n[6] Assitencia Tecnica")
        decisao = int(input("comando: "))
        if (decisao== 1):
            print(osprodutos())
        if (decisao== 2):
            print(selecionar())
        if (decisao== 3):
            print(remover())
        if (decisao== 4):
            print(exibir())
        if (decisao== 5):
            print(finalizar())
        if (decisao== 6):
            print("esse serviço ainda não está disponivel, em breve ")
    

        


# ## Nota Fiscal

# In[111]:


def finalizar():
    cartão = 2500
    total = sum(listapreço)
    minhalista = pd.DataFrame(list(zip(listacodigo,listaprodutos,listaquant,listaunidpreço,listapreço)),columns = ["codigo","produtos","quant.","preço.unid","preço.total"])
    print("saldo do seu cartão: R$"+str((cartão)))
    if(dia==25 and mes==12):
        desconto = total*0.25
        total= total-desconto
        print("Feliz natal! Parabéns"+nome+", voce acaba de ganhar 25% de desconto na sua compra")
    if(dia==diaaniversario and mes==mesaniversario):
        desconto = total*0.50
        total= total-desconto
        print("Feliz aniversario"+nome+"!Nos a Liststore vamos te presentear com 50% de desconto na sua compra.")
    
    else:
        print("voce não possui desconto nesta compra")
    print("\ntotal da sua compra:"+str(total))
    

    senha = 1234
    
    print("|=======================|")
    print("|              |----|   |")
    print("|  ListStore   | \U0001F61c |   |")
    print("|  0000-0000   |----|   |")
    print("|-----------------------| ")
    usuario = int(input("\ndigite a senha do cartão: \n[\U0001F511]"))
    restante = cartão-total
    if(usuario==senha and restante>0):
        print("------------- Cupom Fiscal -------------")
        print(dia+"                        "+hora)
        print(minhalista)
        print("total da compra:R$"+str(total))
        print("valor restante do seu cartão"+str(restante))
        print("parabéns, sua compra sua compra foi realizada com sucesso!! volte sempre.")
    if(usuario==senha and restante<0):
        print("Ops!, voce não tem sando suficiente para realizar essa compra,\nrealize uma nova compra ou remova um item do seu carrinho")
        return(decidir())
    if(usuario!=senha):
        print("senha incorreta,digite sua senha novamente...")
        print(finalizar())
    




# In[8]:


def apresentar():
    nome = input("Por favor,insira seu nome: ")
    print("Seja bem-vindo(a)"+nome+"!,nos somos a liststore \n uma loja com diversos produtos tecnologicos com suporte a assitencia tecnica.")
    


# In[38]:


print(decidir())


# In[52]:


print(finalizar())


# In[30]:


data = datetime.now()
dia = int(data.strftime("%d"))
hora = int(data.strftime("%H"))
if(0<=hora<=12):
    turno = "Bom dia"
if(13<=hora<=18):
    turno = "Bom tarde"
if(19<=hora<=23):
    turno = "Bom noite"

nome = input("Por favor insira seu nome: ")
email= input("insira seu melhor e-mail: ")
print(turno+" "+nome+", seja bem-vindo(a) a ListStore,\nuse os comandos disponiveis para iniciar sua compra:")


# # Cupom de desconto
# 

# In[44]:


dia = int(data.strftime("%d"))
mes = int(data.strftime("%m"))
print(dia)
print(mes)
dia = 25
mes = 12
if(dia==25 and mes==12):
    print("feliz natal")


# In[110]:



print("|-----------------------|")
print("|=======================|")
print("|              |----|   |")
print("|  ListStore   | \U0001F61c |   |")
print("|  0000-0000   |----|   |")
print("|-----------------------| ")
usuario = int(input("\ndigite a senha do cartão: \n[\U0001F511]"))


# In[144]:





# In[ ]:


nome = input("Por favor, insira seu nome")
print("digite o seu aniversario (dia e mes)")
diaaniversario= int(input("dia:"))
mesaniversario = int(input("mes:"))


# In[148]:


import smtplib
import email.message
import pandas as pd # para gerar o dataframe
import numpy as np # para usarmos

codigo = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12","a13","a14","a15"]
produtos = ["camera","smartphone","fone de ouvido","micro sd 32gb","capinha","pelicula","notebook",
 "smartwatch","caixa de som bluetooth","mouse","cabo usb","carregador","capa de notebook",
"carregador portatil","caixa de som alexa"]
preço = [299.99,1299.99,25.00,30.79,15.90,15.80,3499.79,250.89,
        150.60,79.99,20.00,15.00,30.00,35.79,359.59]

loja = pd.DataFrame(list(zip(codigo,produtos,preço)), columns = ["codigo","produtos","preço"]) 


def enviar_email():
    codigo = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12","a13","a14","a15"]
produtos = ["camera","smartphone","fone de ouvido","micro sd 32gb","capinha","pelicula","notebook",
 "smartwatch","caixa de som bluetooth","mouse","cabo usb","carregador","capa de notebook",
"carregador portatil","caixa de som alexa"]
preço = [299.99,1299.99,25.00,30.79,15.90,15.80,3499.79,250.89,
        150.60,79.99,20.00,15.00,30.00,35.79,359.59]

    loja = pd.DataFrame(list(zip(codigo,produtos,preço)), columns = ["codigo","produtos","preço"]) 
    corpo_email = """
    <p>Bom dia</p>
    <p>oi arthur tudo bem com voce</p>
    <p>produtos da loja: {loja}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "email automatico em python"
    msg['From'] = 'arthurnunes345@gmail.com'
    msg['To'] = 'arthurncs345@gmail.com'
    password = 'lljj stbq vpbo idjq' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[147]:


enviar_email()


# In[ ]:




