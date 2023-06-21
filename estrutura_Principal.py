import PerguntasEGabarito as perguntas
import random as random

acoes = ["Pular","Ajuda","Parar","Responder"]
pular = 0
ajuda = 0
dinheiro = 0

numAleatorio = 0
numeroDePerguntasNaListaFaceis = 3
numeroDePerguntasNaListaMedioDificil = 4
numeroDePerguntasRespondidasFaseMedio = 0
numeroDePerguntasRespondidasFaseDificil = 0

def menu():
    print("="*40)
    print(" "*10,"SHOW DO MILHÃO")
    print("="*40)
    print("")
    print("[1] - Jogar")
    print("[0] - Sair")
    print("")
    escolha = str(input("Escolha uma opção: "))
    
    while escolha != "0" and escolha != "1":              
        escolha = str(input("Escolha uma opção existente: "))

    if escolha == "0":
        print("")
        print("Voce fechou o programa")
    else:
        print("")
        print("REGRAS DO JOGO: Responda, acerte e ganhe\nVocê pode pular 3x e pedir uma ajuda")
        print()
        print("INICIANDO O JOGO.....")
        fazerPerguntasFaceis(pular,ajuda,dinheiro,numeroDePerguntasNaListaFaceis,numAleatorio)     



                        #INICIA AS FACEIS


def verificaAlternativaParaRemoverNaAjudaFaceis(alternativa):
    if alternativa == "RIO GRANDE DO SUL" or alternativa == "SÓLIDO" or alternativa == "MINNIE" or alternativa == "SACI-PERERÊ":
        return True
    return False

def verificaSeRespostaCorretaFaceis(resposta,numeroAleatorio):

    indice = int(resposta) -1
    respostaCerta = pegaRespostaCorretaFaceis(numeroAleatorio) 
    if indice == respostaCerta:
        return True
    return False

def pegaRespostaCorretaFaceis(numeroAleatorio):
    cont = 0
    for i in perguntas.gabaritoFaceis[numeroAleatorio]:
        if i == "RIO GRANDE DO SUL" or i == "SÓLIDO" or i == "MINNIE" or i == "SACI-PERERÊ":
            return cont
        cont += 1



def numeroDeAlternativas(alternativaEscolhida):
    if  alternativaEscolhida != "1" and alternativaEscolhida != "2" and alternativaEscolhida != "3" and alternativaEscolhida != "4":
        return True
    return False


def fazerPerguntasFaceis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio):

        for coluna in range(1):
            print("-"*70)
            numerAleatorio = random.randint(0,numeroDePerguntasNoImport)
            print(f"{perguntas.perguntasFacil[numerAleatorio][coluna]}")            
            print("-"*70)  

        for linha in range(4):
            print(f"{[linha+1]} {perguntas.gabaritoFaceis[numerAleatorio][linha]}")    
        print("-"*20)

        for opcao in range(4):
            print(f"{[opcao+1]} {acoes[opcao]}") 

        opcoesAlternativasFaceis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio)


        
def opcoesAlternativasFaceis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio): 

    escolha = str(input("Escolha uma opção: "))  

    while numeroDeAlternativas(escolha):       
        escolha = str(input("Escolha uma opção: "))

    if escolha == "1" :      
        if pulos == 3:
            print("VOCÊ JÁ PULOU 3x.\nNÃO SERÁ POSSIVEL USAR NOVAMENTE....")
            opcoesAlternativasFaceis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio)
        else:
            pulos += 1         
            perguntas.perguntasFacil.pop(numerAleatorio)
            perguntas.gabaritoFaceis.pop(numerAleatorio)
            numeroDePerguntasNoImport -= 1
            fazerPerguntasFaceis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio)   

    elif escolha == "2":    
        if ajudas == 1:
            print("VOCÊ JÁ PEDIU AJUDA.\nNÃO SERÁ POSSIVEL USAR NOVAMENTE....")
            opcoesAlternativasFaceis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio)
        else:
            print("-"*20)  


            for tirar in range(2):
                if verificaAlternativaParaRemoverNaAjudaFaceis(perguntas.gabaritoFaceis[numerAleatorio][tirar]) == False:
                    perguntas.gabaritoFaceis[numerAleatorio].pop(tirar)
                print(f"{[tirar+1]} {perguntas.gabaritoFaceis[numerAleatorio][tirar]}")
            print("-"*20)    
            ajudas += 1

            for opcao in range(4):
                print(f"{[opcao+1]} {acoes[opcao]}")    
            opcoesAlternativasFaceis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio)     


    elif escolha == "4":      
        resposta = str(input("Digite a alternativa certa: "))

        while numeroDeAlternativas(resposta):     
            resposta = str(input("Digite a alternativa certa: "))

        if verificaSeRespostaCorretaFaceis(resposta,numerAleatorio) == True:        
            dinheiro += 1000   
            print("")
            print(f"Certa resposta, você tem R${dinheiro}")  
            print('=-'*23)
            print("     VAMOS PARA PROXIMA FASE....    ")
            print('=-'*23)
            fazerPerguntasMedio(pulos,ajudas,dinheiro,numeroDePerguntasNaListaMedioDificil,numerAleatorio,numeroDePerguntasRespondidasFaseMedio)      
        else:
            print("")
            print(f"Sua resposta está incorreta, você terminou o jogo com R${dinheiro/2}") 
            
            
    elif escolha == "3":  
        print(f"Você parou de jogar, você terminou com R${dinheiro}")     



                    # INICIA AS MEDIAS


def verificaAlternativaParaRemoverNaAjudaMedio(alternativa):
    if alternativa == "SEIS" or alternativa == "ARGENTINA" or alternativa == "NERO" or alternativa == "ITÁLIA" or alternativa == "JAPÃO":
        return True
    return False

def verificaSeRespostaCorretaMedio(resposta,numeroAleatorio):
    indice = int(resposta) -1
    respostaCerta = pegaRespostaCorretaMedio(numeroAleatorio) 
    if indice == respostaCerta:
        return True
    return False

def pegaRespostaCorretaMedio(numeroAleatorio):
    cont = 0
    for i in perguntas.gabaritoMedio[numeroAleatorio]:
        if i == "SEIS" or i == "ARGENTINA" or i == "NERO" or i == "ITÁLIA" or i == "JAPÃO":
            return cont
        cont += 1




def fazerPerguntasMedio(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidas):

        for coluna in range(1):
            print("-"*70)
            numerAleatorio = random.randint(0,numeroDePerguntasNoImport)
            print(f"{perguntas.perguntasMedio[numerAleatorio][coluna]}")            
            print("-"*70)  

        for linha in range(4):
            print(f"{[linha+1]} {perguntas.gabaritoMedio[numerAleatorio][linha]}")    
        print("-"*20)

        for opcao in range(4):
            print(f"{[opcao+1]} {acoes[opcao]}") 

        opcoesAlternativasMedio(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidas)


        
def opcoesAlternativasMedio(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidas): 

    escolha = str(input("Escolha uma opção: "))  

    while numeroDeAlternativas(escolha):       
        escolha = str(input("Escolha uma opção: "))

    if escolha == "1" :      
        if pulos == 3:
            print("VOCÊ JÁ PULOU 3x.\nNÃO SERÁ POSSIVEL USAR NOVAMENTE....")
            opcoesAlternativasMedio(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidas)
        else:
            pulos += 1         
            perguntas.perguntasMedio.pop(numerAleatorio)
            perguntas.gabaritoMedio.pop(numerAleatorio)
            numeroDePerguntasNoImport -= 1
            fazerPerguntasMedio(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidas)   

    elif escolha == "2":    
        if ajudas == 1:
            print("VOCÊ JÁ PEDIU AJUDA.\nNÃO SERÁ POSSIVEL USAR NOVAMENTE....")
            opcoesAlternativasMedio(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidas)
        else:
            print("-"*20)  


            for tirar in range(2):
                if verificaAlternativaParaRemoverNaAjudaMedio(perguntas.gabaritoMedio[numerAleatorio][tirar]) == False:
                    perguntas.gabaritoMedio[numerAleatorio].pop(tirar)
                print(f"{[tirar+1]} {perguntas.gabaritoMedio[numerAleatorio][tirar]}")
            print("-"*20)    
            ajudas += 1

            for opcao in range(4):
                print(f"{[opcao+1]} {acoes[opcao]}")    
            opcoesAlternativasMedio(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidas)     


    elif escolha == "4":      
        resposta = str(input("Digite a alternativa certa: "))

        while numeroDeAlternativas(resposta):     
            resposta = str(input("Digite a alternativa certa: "))

        if verificaSeRespostaCorretaMedio(resposta,numerAleatorio) == True:      
            if numeroDePerguntasRespondidas < 1:
                dinheiro += 9000
            else:
                dinheiro += 90000
            print("")
            print(f"Certa resposta, você tem R${dinheiro}")  
            print('=-'*23)
            print("     VAMOS PARA PROXIMA FASE....    ")
            print('=-'*23)
            if numeroDePerguntasRespondidas < 1:
                numeroDePerguntasRespondidas += 1  
                fazerPerguntasMedio(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidas)
            else:
                dinheiro = 100000
                numeroDePerguntasRespondidasFaseDificil = 0
                fazerPerguntasDificeis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil)   
        else:
            print("")
            print(f"Sua resposta está incorreta, você terminou o jogo com R${dinheiro/2}") 
            
            
    elif escolha == "3":  
        print(f"Você parou de jogar, você terminou com R${dinheiro}")




                    #INICIA AS DIFICEIS


def verificaAlternativaParaRemoverNaAjudaDificeis(alternativa):
    if alternativa == "PINGUIM" or alternativa == "ISRAEL" or alternativa == "JEAN CLAUDE VAN DAMME" or alternativa == "HOLANDA" or alternativa == "ALFA":
        return True
    return False

def verificaSeRespostaCorretaDificeis(resposta,numeroAleatorio):

    indice = int(resposta) -1
    respostaCerta = pegaRespostaCorretaDificeis(numeroAleatorio) 
    if indice == respostaCerta:
        return True
    return False

def pegaRespostaCorretaDificeis(numeroAleatorio):
    cont = 0
    for i in perguntas.gabaritoDificil[numeroAleatorio]:
        if i == "PINGUIM" or i == "ISRAEL" or i == "JEAN CLAUDE VAN DAMME" or i == "HOLANDA" or i == "ALFA":
            return cont
        cont += 1




def fazerPerguntasDificeis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil):

        for coluna in range(1):
            print("-"*70)
            numerAleatorio = random.randint(0,numeroDePerguntasNoImport)
            print(f"{perguntas.perguntasDificil[numerAleatorio][coluna]}")            
            print("-"*70)  

        for linha in range(4):
            print(f"{[linha+1]} {perguntas.gabaritoDificil[numerAleatorio][linha]}")    
        print("-"*20)

        for opcao in range(4):
            print(f"{[opcao+1]} {acoes[opcao]}") 

        opcoesAlternativasDificil(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil)


        
def opcoesAlternativasDificil(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil): 

    escolha = str(input("Escolha uma opção: "))  

    while numeroDeAlternativas(escolha):       
        escolha = str(input("Escolha uma opção: "))

    if escolha == "1" : 
        if numeroDePerguntasRespondidasFaseDificil == 1:
            print("Não é possivel pular na última pergunta")     
            opcoesAlternativasDificil(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil)
        elif pulos == 3:
            print("VOCÊ JÁ PULOU 3x.\nNÃO SERÁ POSSIVEL USAR NOVAMENTE....")
            opcoesAlternativasDificil(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil)
        else:
            pulos += 1         
            perguntas.perguntasDificil.pop(numerAleatorio)
            perguntas.gabaritoDificil.pop(numerAleatorio)
            numeroDePerguntasNoImport -= 1
            fazerPerguntasDificeis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil)   

    elif escolha == "2":  

        if numeroDePerguntasRespondidasFaseDificil == 1:
            print("Não é possivel pedir ajuda na última pergunta")  
            opcoesAlternativasDificil(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil)

        elif ajudas == 1:
            print("VOCÊ JÁ PEDIU AJUDA.\nNÃO SERÁ POSSIVEL USAR NOVAMENTE....")
            opcoesAlternativasDificil(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil)
       
        else:
            print("-"*20)  
            for tirar in range(2):
                if verificaAlternativaParaRemoverNaAjudaDificeis(perguntas.gabaritoDificil[numerAleatorio][tirar]) == False:
                    perguntas.gabaritoDificil[numerAleatorio].pop(tirar)
                print(f"{[tirar+1]} {perguntas.gabaritoDificil[numerAleatorio][tirar]}")
            print("-"*20)    
            ajudas += 1

            for opcao in range(4):
                print(f"{[opcao+1]} {acoes[opcao]}")    
            opcoesAlternativasDificil(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil)     


    elif escolha == "4":      
        resposta = str(input("Digite a alternativa certa: "))

        while numeroDeAlternativas(resposta):     
            resposta = str(input("Digite a alternativa certa: "))

        if verificaSeRespostaCorretaDificeis(resposta,numerAleatorio) == True:  
            if numeroDePerguntasRespondidasFaseDificil < 1:
                dinheiro += 400000  
                print("")
                print(f"Certa resposta, você tem R${dinheiro}")  
                print('=-'*23)
                print("     VAMOS PARA PROXIMA FASE....    ")
                print('=-'*23)
                numeroDePerguntasRespondidasFaseDificil += 1 
                fazerPerguntasDificeis(pulos,ajudas,dinheiro,numeroDePerguntasNoImport,numerAleatorio,numeroDePerguntasRespondidasFaseDificil)      
            else:
                dinheiro += 500000
                print("")
                print("Certa resposta, você concluiu o show do milhão")  
                print(f"Parabéns aqui está seu R${dinheiro}")
                print("")
                print("Obrigado por jogar!")       
        else:
            if numeroDePerguntasRespondidasFaseDificil == 1:
                print("")
                print(f"Sua resposta está incorreta, você terminou o jogo com R${dinheiro/4}")
            else:
                print("")
                print(f"Sua resposta está incorreta, você terminou o jogo com R${dinheiro/2}") 

    elif escolha == "3": 
        if numeroDePerguntasRespondidasFaseDificil == 1:
            print(f"Você parou de jogar, você terminou com R${dinheiro}")
        else:
            print(f"Você parou de jogar, você terminou com R${dinheiro/2}")



menu()