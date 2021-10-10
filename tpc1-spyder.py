# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 21:08:22 2021

@author: Mariana Ribeiro
"""

#jogo dos fósforos

#alinea a) - o jogador contra o computador

import random 

def fosforos1 ():
    quem=input("quem vai jogar primeiro: \n escreva 'eu' para jogar primeiro ou 'pc' para o computador jogar primeiro:   ")
    if quem=="eu":
        resto=21
        while resto>1:
            n=int(input("introduza o numero 1, 2, 3 ou 4:  " ))
            if n>=5:
                print ("numero invalido ")  
            else:
                resto=resto - n
                if resto==1:
                    print("sobrou um fosforo o jogador ganhou \n")
                    print ("fim\n")
                    return resto

                else:
                     print ("existem ", resto, "fosforos \n")
                     n2=random.randint(1,4)
                     if n2>resto:
                             while n2>= resto:
                                 n2=random.randint(1,4)
                     else: 
                            print ("o computador joga: ", n2, "\n")
                            resto= resto - n2

                            if resto>1:
                                print ("existem ainda ", resto, "fosforos \n")
                            elif resto==1:            
                                print("Sobrou um fosforo. o computador ganha \n ")
                                print ("fim \n")
                          
    elif quem=="pc":
        resto=21
        while resto>1:
            n2=random.randint(1,4)
            if n2>resto:
                    while n2>= resto:
                        n2=random.randint(1,4)
            else: 
                    print ("o computador joga: ", n2, "\n")
                    resto= resto - n2

                    if resto>1:
                        print ("existem ainda ", resto, "fosforos \n")
                    elif resto==1:            
                        print("Sobrou um fosforo. o computador ganha \n")
                        print ("fim")
                        
            n=int(input("introduza o numero 1, 2, 3 ou 4:  \n" ))
            if n>=5:
                    print ("numero invalido \n ")  
            else:
                    resto=resto - n
                    if resto==1:
                        print("sobrou um fosforo o jogador ganhou \n")
                        print ("fim \n")
                        return resto

                    else:
                        print ("existem ", resto, "fosforos \n ")
                     
    else: 
        print ("resposta inválida tente novamente \n")

    return resto

fosforos1()


#alinea b) - o computador joga em 2º lugar e ganha sempre

def fosforos2 ():
    resto=21
    while resto>1:
        n=int(input("introduza o numero 1, 2, 3 ou 4:  \n"))
        if n>=5:
            print ("numero invalido \n")  
        else:
            n2= 5-n
            resto=resto - n
            print ("existem ", resto, "fosforos \n")
            print ("o computador joga: ", n2, "\n")
            resto= resto - n2
            if resto>1:
                print ("existem ainda ", resto, "fosforos \n")
            else:
                print("Sobrou um fosforo. o computador ganha \n")
                print("fim \n")
    return resto

fosforos2()
 
    
#alinea c) - o computador joga em primeiro lugar e tenta apanhar um erro de raciocinio do jogador  

def fosforos3():
    resto=21
    n2=random.randint(1,4)
    print ("o computador joga: ", n2, "\n")
    resto= resto - n2
    print ("existem ainda ", resto, "fosforos \n")
    op=True
    n=int(input("introduza o numero 1, 2, 3 ou 4:  \n" ))
    if n>=5:
        print ("numero invalido \n")
        op=False
        while op==False: 
             n=int(input("introduza o numero 1, 2, 3 ou 4:  \n" ))
             if n>=5:
                 print ("numero invalido \n")
                 op=False
             else:
                 op=True
    else:
          resto= resto - n
          print ("existem ainda ", resto, "fosforos \n")
    

    while (n+n2)==5:
                    n2=random.randint(1,4)
                    print ("o computador joga: ", n2, "\n")
                    resto= resto - n2
                    if resto==1:
                        print("sobrou um fosforo o computador ganhou \n")
                        print ("fim \n")
                        return resto
                    else:
                        print ("existem ainda ", resto, "fosforos \n")              
                        n=int(input("introduza o numero 1, 2, 3 ou 4:  \n" ))
                        
                        
                        if n>=5:
                            print ("numero invalido \n")
                            op=False
                            while op==False: 
                                n=int(input("introduza o numero 1, 2, 3 ou 4:  \n" ))
                                if n>=5:
                                    print ("numero invalido \n")
                                    op=False
                                else:
                                        op=True
                        else:
                              resto= resto - n
                                                       
                              if resto==1:
                                print("sobrou um fosforo o jogador ganhou \n")
                                print ("fim \n")
                                return resto
                              else:
                                print ("existem ainda ", resto, "fosforos \n")
     
    if (n+n2)<5:
                n2=5-(n+n2)

                print ("o computador joga: ", n2, "\n")
                resto= resto - n2
                print ("existem ainda ", resto, "fosforos \n")
    elif (n+n2)>5:

                n2=10-(n+n2)
                print ("o computador joga: ", n2, "\n")
                resto= resto - n2
                print ("existem ainda ", resto, "fosforos \n")

    while resto>1:
                n=int(input("introduza o numero 1, 2, 3 ou 4:  \n" ))
                resto= resto-n
                if n>=5:
                    print ("numero invalido \n")  
                else:
                    n2= 5-n
                    resto=resto - n
                    print ("existem ", resto, "fosforos \n")
                    print ("o computador joga: ", n2, "\n")
                    resto= resto - n2
                    if resto>1:
                        print ("existem ainda ", resto, "fosforos \n")
                    else:
                        print("Sobrou um fosforo. o computador ganha \n")
                        print("fim \n")
    return resto
    
fosforos3() 
              
    