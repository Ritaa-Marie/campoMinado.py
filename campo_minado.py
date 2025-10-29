import random #biblioteca para gerar as funções aleatórias

#definição de constantes para facilitar na hora de colocar cores no campo
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

#função de validar a entrada do usuário
def entrada_validada():
    #impressões das regras e instruções para o jogo
    print("------ CAMPO MINADO ------\n")
    print("Instruções para o jogo: ")
    print(" - Escolha um tamanho para o lado seu campo minado quadrado (máximo: 10)") 
    print(" - Escolha o número de minas escondidas (mínimo: 1)")
    print(" - Você inicia o jogo na posição da cor verde.")
    print(" - O limite de bandeiras ('M') é o número de minas.")
    print(" - Você perde o jogo se abrir uma casa com mina (?).")
    print(" - Você vence o jogo se marcar todas as casas com minas corretamente.\n")
    #uso do while para a pessoa repetir a entrada caso digite algo errado
    while True:
        #uso do try/except para fazer o tratamento de erro da entrada que se espera em inteiro
        try:
            #perguntas para o usuário responder
            tamanho_campo = int(input(" Digite o tamanho para o lado do campo minado: "))
            numero_minas = int(input(" Digite o número de minas escondidas: "))
            #definindo o limite de minas, sendo ele o número máximo de posições da matriz
            limite_minas = tamanho_campo ** 2
            #verificação se o valor do lado do campo é menor que 1 e maior que 10
            if tamanho_campo < 1 or tamanho_campo > 10:
                print("Tamanho inválido! Ele deve estar entre 1 e 10. Tente novamente.\n")
            #verificação se tem pelo menos uma mina e se não ultrapassa o limite
            elif numero_minas < 1 or numero_minas > limite_minas:
                print(f"Número de minas inválido! Deve ter no mínimo 1 e no máximo {limite_minas}. Tente novamente.\n")
            #verifica se o campo está entre 1 e 10 e se o número de minas está entre 1 e o limite, para retornar essas informações
            elif (tamanho_campo >= 1 and tamanho_campo <= 10) and (1 <= numero_minas <= limite_minas):
                return (tamanho_campo, numero_minas)
        #se for digitado algo diferente de inteiro é tratado nesse trecho
        except ValueError:
            print("Entrada inválida! Deve ser inserido apenas números inteiros. Tente novamente.\n")

'''função para criar o campo minado
como parâmetro tem o tamanho do campo e o que deve ter dentro de suas posições, caso não passado o valor,
por padrão será vazio.'''
def criar_campo_minado(tamanho_campo, preencimento=' '):
    campo_minado = [] #criação de uma lista para iniciar o campo
    #for usado com o tamanho do campo + 2 porque o campo tem barreiras ao seu redor, acrescentando 2 linhas e 2 colunas.
    for i in range(tamanho_campo+2):
        linha = [] #cria as linhas do campo
        for j in range(tamanho_campo+2):
            #para adicionar a barreira no campo, verifica se a posição na linha ou coluna é a primeira (0) ou a última (tamanho_campo+1).
            if i == 0 or i == tamanho_campo+1 or j == 0 or j == tamanho_campo+1:
                linha.append(f"-1") #adiciona a barreira -1 se for alguma dessas posições
            else:
                #caso não seja o caso acima, a posição recebe o preencimento.
                linha.append(f"{preencimento}")
        campo_minado.append(linha) #adiciona a linha na lista do campo já criada, formando assim uma lista de listas, ou matriz em python.
    return campo_minado #retorna o campo criado

'''função para exibir o campo,
como parâmetro recebe o campo a ser exibido, o tamanho dele e a posição que a pessoa está, caso não seja informado, por padrão
será usado ().'''
def exibir_campo(campo_minado, tamanho_campo, posicao=()):
    '''for usado com o intervalo de 1 ao tamanho do campo + 1 porque o campo tem barreiras ao seu redor, e dessa forma  
    desconsidera as casas já ocupadas com -1. Os for's são aninhados para percorrer a posição exata da linha e coluna.'''
    for x in range(1, tamanho_campo +1):
        for y in range(1, tamanho_campo +1):
            if posicao == [x,y]: # se a posição for especificada ela entra aqui e é impressa de verde
                print(f"{GREEN}|{campo_minado[x][y]}|{GREEN}{RESET}", end=' ')
            else:
                #caso não seja igual a condição acima, ela é impressa normal
                print(f"|{campo_minado[x][y]}|", end=' ')
        print( ) #printa uma linha em branco para melhorar a visibilidade

'''função de esconder as minas aleatoriamente, 
como parâmetro é passado o campo minado real, que terá todas as minas, o tamanho do campo e o 
número de minas a serem escondidas.'''
def esconder_minas(campo_minado_real, tamanho_campo, numero_minas):
    minas = set() # para evitar a repetição de minas no mesmo lugar, definimos fazer um conjunto e guardar as posições já sorteadas
    #enquanto não forem sorteadas todas as posições para colocar o número de minas aleatórias isso se repete
    while len(minas) < numero_minas:
        '''a posição x e y recebe um número aleatório entre os valores válidos do campo, ou seja, 
        um número para linha e para coluna de 1 ao tamanho do campo, desconsiderando a posição das barreiras.'''
        x = random.randint(1, tamanho_campo) 
        y = random.randint(1, tamanho_campo)
        #se o valor sorteado não estiver em minas, ou seja, se já não tiver uma mina nele, essa posição receberá uma mina "?"
        if (x,y) not in minas:
            minas.add((x,y)) #adiciona a posição no conjunto
            campo_minado_real[x][y] = "?"
    
'''função para contar o número de minas ao redor das 8 casas vizinhas,
como parâmetro é passado o campo minado real, que contém as minas, e o tamannho do campo.'''
def qtd_minas_lado(campo_minado_real, tamanho_campo):
    '''for usado com o intervalo de 1 ao tamanho do campo + 1 porque o campo tem barreiras ao seu redor, e dessa forma  
    desconsidera as casas já ocupadas com -1. Os for's são aninhados para percorrer a posição exata da linha e coluna.'''
    for x in range(1, tamanho_campo +1):
        for y in range(1, tamanho_campo +1):
            #se a posição estiver livre e não for ocupada por uma mina,
            if campo_minado_real[x][y] == " ":
                qtd_minas_vizinhas = 0 #ela inicia com 0 minas vizinhas
                '''depois, usa outro for para percorrer as 8 casas vizinhas,
                variando a posiçaõ da linha para analisar (x-1, x, x+1), usando o intervalo do  range(x-1, x+2)'''
                for i in range(x-1, x+2):
                    '''e variando também a posiçaõ da coluna para analisar (y-1, y, y+1) usando o intervalo do  range(y-1,y+2),
                    dessa forma, percorrendo todas as possibilidades dessas variações juntas, resultando nas 8 casas ao redor.'''
                    for j in range(y-1,y+2):
                        """se a posição não for ela mesma e se em alguma dessas variações estiver uma mina ira
                        somar mais 1 na qtd_minas_vizinhas."""
                        if (x,y) != (i,j) and campo_minado_real[i][j] == "?":
                            qtd_minas_vizinhas += 1
                '''logo depois, a posiçaõ no campo real recebe como string a quantidade de minas vizinhas.'''
                campo_minado_real[x][y] = str(qtd_minas_vizinhas)

'''função principal do jogo, para que o jogador possa de fato jogar,
como parêmtro é passado o campo real com as minas e a quantidade de minas vizinhas, o tamanho do campo e o número de minas.'''
def movimentacao(campo_real, tamanho_campo, numero_minas):
    #definição de variáveis utilizadas durante a função
    posicao_inicial = 0 #marca a posição inicial
    vencer_por_minas = 0 #conta quantas minas corretas o usuário já marcou
    max_m = numero_minas #número máximo de bandeiras
    perder  = False #para verificar se a pessoa abriu uma mina

    #definindo aleatoriamente a posição inicial do jogador
    '''as possibilidades são armazenadas dentro de uma lista, usando lista comprimida para adicionar todas as posições do campo'''
    possibilidades_posicao_inicial = [[x,y] for x in range(1, tamanho_campo + 1)
                for y in range(1, tamanho_campo + 1)] 
    '''novamente foi usado o range de 1 a tamanho_campo + 1 para desconsiderar a barreira.'''
    #se por acaso não tiverem posiçaõ inicial, o jogo termina.
    if not possibilidades_posicao_inicial:
        print("Não há posições seguras!")
        return
        
    #a posição atual recebe aleatoriamente uma posição escolhida da lista de possibilidades
    posicao_inicial = random.choice(possibilidades_posicao_inicial)
    #a posição atual inicia com a inicial
    posicao_atual = posicao_inicial


    #criação de um campo minado apenas para ser visualizado pelo jogador, tendo todas as casas preenchidas com '*'.
    campo_visivel = criar_campo_minado(tamanho_campo, preencimento='*')

    #while usado para permitir repetições mesmo se a pessoa errar
    while True:
        #try utilizado para tratamento de erro, que se espera inteiro.
        try:
            print("\n== Campo minado ==")

            #verifica se a pessoa perdeu (se perder = True)
            if perder:
                #exibe o campo real com as respostas e encerra o programa
                exibir_campo(campo_real, tamanho_campo)
                print(f"{YELLOW}Você perdeu o jogo.{RESET}")
                break
            
            #se a pessoa marcar corretamente todas as minas ela vence o jogo e ele encerra
            if vencer_por_minas == numero_minas:
                #exibe o campo real com as respostas e encerra o programa
                exibir_campo(campo_real, tamanho_campo)
                print(f"{BLUE}Você ganhou o jogo! Parabéns.{RESET}")
                break
            #exibe o campo visível e indicando a posição atual de verde
            exibir_campo(campo_visivel, tamanho_campo, posicao_atual)
            print(f"Número de bandeiras disponíveis ('M'): {max_m}") #mostra o número máximo de bandeiras
            #print do menu de movimentação
            print("\n   Movimentação ")
            print(" (1) - Cima")
            print(" (2) - Baixo")
            print(" (3) - Direita")
            print(" (4) - Esquerda")
            print(" (5) - Marcar uma posição como mina (bandeira)")
            print(" (6) - Abrir uma posição")
            print(" (7) - Retirar bandeira")
            print(" (8) - Sair")
            print("-" * 20)
            
            #pede a opção para o usuário
            op = int(input("Digite a sua opção: "))

            #uso do match para avaliar os casos
            match op:
                #caso 1 - andar para cima
                case 1:
                    # x representa linha e y coluna
                    # para se mover para cima é necessário apenas ir para a linha de cima, ou seja, a linha atual - 1
                    cima_x = posicao_atual[0] - 1 # a posição atual em x - 1 para ir para cima
                    cima_y = posicao_atual[1]    # a posição atual em y se mantém
                    # se a nova posição não for a barreira,
                    if campo_visivel[cima_x][cima_y] != "-1":
                        posicao_atual[0] = cima_x  # a posição é atualizada
                    else: 
                        print("Caminho inválido! Tente novamente.")

                #caso 2 -  baixo
                # x representa linha e y coluna
                # para se mover para baixo é necessário apenas ir para a linha de baixo, ou seja, a linha atual + 1
                case 2:
                    baixo_x = posicao_atual[0] + 1 #a posição atual em x + 1 para ir para baixo
                    baixo_y = posicao_atual[1]      # a posição atual em y se mantém
                    # se a nova posição não for a barreira,
                    if campo_visivel[baixo_x][baixo_y] != "-1":
                        posicao_atual[0] = baixo_x # a posição é atualizada
                    else: 
                        print("Caminho inválido! Tente novamente.")

                #caso 3 - direita
                case 3:
                # x representa linha e y coluna
                # para se mover para direita é necessário apenas ir para a coluna da direita, ou seja, a coluna atual + 1
                    direita_x = posicao_atual[0]       # a posição atual em x se mantém
                    direita_y = posicao_atual[1] + 1   #a posição atual em y + 1 para ir para direita
                    # se a nova posição não for a barreira,
                    if campo_visivel[direita_x][direita_y] != "-1":
                        posicao_atual[1] = direita_y # a posição é atualizada
                    else: 
                        print("Caminho inválido! Tente novamente.")

                #caso 4 - esquerda
                case 4:
                # x representa linha e y coluna
                # para se mover para esquerda é necessário apenas ir para a coluna da esquerda, ou seja, a coluna atual - 1
                    esquerda_x = posicao_atual[0]       # a posição atual em x se mantém
                    esquerda_y = posicao_atual[1] - 1   #a posição atual em y - 1 para ir para esquerda
                    # se a nova posição não for a barreira,
                    if campo_visivel[esquerda_x][esquerda_y] != "-1":
                        posicao_atual[1] = esquerda_y # a posição é atualizada
                    else: 
                        print("Caminho inválido! Tente novamente.")

                #caso 5 - marcar com 'M' a posição
                case 5:
                    # i e j recebem a posição atual da linha e da coluna
                    i = posicao_atual[0]
                    j = posicao_atual[1]
                    #se o número máximo de minas já adicionadas ainda não tiver sido atingido,
                    if max_m > 0:
                        # se a posição que deseja marcar ainda não foi aberta ou não está marcada com 'M',
                        if campo_visivel[i][j] == '*':
                            campo_visivel[i][j] = f"{RED}M{RESET}" # a posição recebe o 'M'
                            max_m -= 1 # o número de minas já usadas decresce em 1
                            # e se o campo real indicar que essa posição tem uma mina,
                            if campo_real[i][j] == "?": 
                                vencer_por_minas += 1 # a variável de contar as minas já marcadas corretamente soma 1.
                        else:
                            print("Casa inválida para colocar bandeira.")
                    else:
                        print("Número máximo de bandeiras ('M') atingido.")
                    
                #caso 6 - abrir uma posição
                case 6:
                    # i e j recebem a posição atual da linha e da coluna
                    i = posicao_atual[0]
                    j = posicao_atual[1]
                    # se a posição que deseja abrir ainda não foi aberta ou não está marcada com 'M',
                    if campo_visivel[i][j] == '*':
                        valor_real = campo_real[i][j]
                        #recebe o valor dessa posição no campo real
                        campo_visivel[i][j] = valor_real # o campo visível mostra a quantidade de minas vizinhas
                        #verifica se a posição aberta no campo real é uma mina,
                        if campo_real[i][j] == "?":
                            perder = True # se for, perder recebe True e na próxima interação o jogo é encerrado.
                    else:
                        print("Não é permitido abrir essa casa.")
                    
                #caso 7 - retirar uma bandeira
                case 7:
                    # i e j recebem a posição atual da linha e da coluna
                    i = posicao_atual[0]
                    j = posicao_atual[1]
                    #se a posição que deseja desmarcar tem uma marcação, ou seja, um 'M',
                    if campo_visivel[i][j] == f"{RED}M{RESET}":
                        campo_visivel[i][j] = '*' # o campo visivel recebe o '*' padrão
                        max_m += 1 # e aumenta em 1 o número de marcações ainda disponíveis
                        #se esssa posição no campo real é uma mina, 
                        if campo_real[i][j] == '?':
                            vencer_por_minas -= 1 #decrescemos 1 na variável que controla o número de minas já marcadas corretamente
                    else:
                        print("Casa inválida para tirar a bandeira.")

                #caso 8 - sair do programa
                case 8:
                    #encerra o programa
                    print("\nVocê saiu do programa.")
                    break

                #se a opção digitada por fora do escopo, cai nessa opção.
                case _:
                    print("Opção inválida! Escolha uma opção de 1 a 8.\n")
        
        #se a entrada não for números inteiros é tratado nesse trecho
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.\n")


#função main que orquestra as outras e monta de fato o programa     
def main():
    entrada = entrada_validada() # inicia validando as entradas, retornando uma tupla, sendo entrada[0] o tamanho e entrada[1] o número de minas
    campo_real = criar_campo_minado(entrada[0]) #cria um campo real
    esconder_minas(campo_real, entrada[0], entrada[1]) #esconde as minas nesse campo
    qtd_minas_lado(campo_real, entrada[0]) #verifica a quantidade de minas nas 8 casas vizinhas
    movimentacao(campo_real, entrada[0], entrada[1]) #chama a função de movimentação, para jogar o campo minado

#chama a função para executar o programa
main()