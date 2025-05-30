import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('audio/soudtrack/funny-bgm-240795.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('audio/sound/smw_coin.wav')
barulho_colisao.set_volume(0.5)

largura = 640
altura = 480
x = largura/2 # essa maneira faz com que o obj dique no meio da tela: largura_tela/2 - largura_obj/2
y = altura/2

x_azul = randint(40, 600)
y_azul = randint(50, 430)


pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

# define largura e altura da janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo')#mudar nome da janela
relogio = pygame.time.Clock()


#faz um loop principal. (tem expliacao na pasta 'explicacoes')
while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

            '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20   
                ''' 
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20    
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50)) 
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()

    tela.blit(texto_formatado, (430,15))
    

    pygame.display.update()