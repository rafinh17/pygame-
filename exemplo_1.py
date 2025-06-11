import pygame
pygame.init() # inicializa o pygame
largura = 800 # define a largura 
altura = 600  #define a altura da tela 
tela = pygame.display.set_mode((largura, altura)) #cria a tela com as dimensoes especificadas
pygame.display.set_caption("exemplo de jogo")  # define o titulo da janela 
rodando = True # variavel para controlar o loop principal 
while rodando: # loop principal do jogo 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False 

    tela.fill((0,206,209)) # preencha a tela com preto 
    pygame.display.update() # atualiza a tela 
  
pygame.quit()    # encerra a tela 