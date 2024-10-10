import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da janela
largura = 640
altura = 480
tamanho_janela = (largura, altura)

# Criando a janela em modo fullscreen
tamanho_janela = pygame.display.Info()  # Obtém a resolução atual da tela do usuário
largura = tamanho_janela.current_w
altura = tamanho_janela.current_h
janela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
pygame.display.set_caption('Troca de Frames com Pygame')

# Definindo cores
cor_fundo = (50, 50, 50)  # Cinza escuro
cor_texto = (255, 255, 255)  # Branco
cor_botao = (0, 128, 255)  # Azul claro
cor_botao_claro = (100, 200, 255)  # Azul mais claro

# Definindo a fonte e o tamanho do texto
fonte = pygame.font.Font(None, 40)

# Carregar a imagem para o frame 1
imagem = pygame.image.load("Software/Images/B.png").convert_alpha()
# imagem = pygame.image.load("Software/Images/B.png")  # Certifique-se de que o caminho da imagem está correto
imagem_redimensionada = pygame.transform.scale(imagem, (200, 200))  # Redimensiona a imagem se necessário

# Funções para desenhar os frames
def draw_frame_home_screen():
    janela.fill((0, 100, 0))  # Fundo verde escuro
    texto = fonte.render("Frame 1", True, cor_texto)
    janela.blit(texto, (largura // 2 - 50, altura // 2 - 20))
    
    # Desenhar a imagem no frame 1
    janela.blit(imagem_redimensionada, (largura // 2 - 100, altura // 2 - 150))  # Centraliza a imagem

def desenhar_frame_2():
    janela.fill((100, 0, 0))  # Fundo vermelho escuro
    texto = fonte.render("Frame 2", True, cor_texto)
    janela.blit(texto, (largura // 2 - 50, altura // 2 - 20))

# Função para desenhar botões
def desenhar_botoes():
    botao_frame_1 = pygame.Rect(50, 400, 200, 50)
    botao_frame_2 = pygame.Rect(390, 400, 200, 50)

    # Desenhando botões
    pygame.draw.rect(janela, cor_botao, botao_frame_1)
    pygame.draw.rect(janela, cor_botao, botao_frame_2)

    # Adicionando texto aos botões
    texto_botao_1 = fonte.render("Frame 1", True, cor_texto)
    texto_botao_2 = fonte.render("Frame 2", True, cor_texto)

    janela.blit(texto_botao_1, (botao_frame_1.x + 50, botao_frame_1.y + 10))
    janela.blit(texto_botao_2, (botao_frame_2.x + 50, botao_frame_2.y + 10))

    return botao_frame_1, botao_frame_2

# Função principal do jogo
def main():
    # Estado do frame (1 ou 2)
    frame_atual = 1

    while True:
        # Verifica eventos (como fechamento da janela)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Verifica se um botão foi clicado
                if botao_frame_1.collidepoint(mouse_pos):
                    frame_atual = 1
                if botao_frame_2.collidepoint(mouse_pos):
                    frame_atual = 2

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Desenha o frame atual
        if frame_atual == 1:
            draw_frame_home_screen()
        else:
            desenhar_frame_2()

        # Desenha os botões e retorna seus retângulos
        botao_frame_1, botao_frame_2 = desenhar_botoes()

        # Atualiza a tela
        pygame.display.update()

# Chamando a função principal
if __name__ == "__main__":
    main()
