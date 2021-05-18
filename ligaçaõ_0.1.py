# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:23:34 2021

@author: ana e arthur
"""
contato1 ={'nome':'João',
           'telefone':'1111-1111',}

contato2 ={'nome':'Flavia',
           'telefone':'2222-2222',}

contato3 ={'nome':'Eduarda',
           'telefone':'3333-3333',}

contato4 ={'nome':'Vitor',
           'telefone':'4444-4444',}




questão =int(input("selecione uma contato:  "))
if questão == 1:
    print("ligando para "+contato1['nome']+"...")
if questão == 2:
    print("ligando para "+contato2['nome']+"...")      
if questão == 3:
    print("ligando para "+contato3['nome']+"...")
if questão == 4:
    print("ligando para "+contato4['nome']+"...")
    
    
    
    
    