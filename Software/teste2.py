import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Criando a janela em modo fullscreen
tamanho_janela = pygame.display.Info()  # Obtém a resolução atual da tela do usuário
largura = tamanho_janela.current_w
altura = tamanho_janela.current_h
janela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
pygame.display.set_caption('Modo Tela Cheia com Pygame')

# Função para desenhar o frame
def desenhar_frame():
    janela.fill((0, 100, 100))  # Fundo de cor azul-esverdeada
    texto = pygame.font.Font(None, 50).render("Tela cheia: {}x{}".format(largura, altura), True, (255, 255, 255))
    janela.blit(texto, (largura // 2 - 200, altura // 2 - 20))

# Função principal do jogo
def main():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Verifica se a tecla ESC foi pressionada para sair do modo fullscreen
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Desenha o frame atual
        desenhar_frame()

        # Atualiza a tela
        pygame.display.update()

# Chamando a função principal
if __name__ == "__main__":
    main()
