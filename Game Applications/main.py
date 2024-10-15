import pygame
import sys
from game_elements import *
from arduino_communication import TrashVerifier as TV

# Inicializando o Pygame
pygame.init()

# Criando a janela em modo fullscreen
size_window = pygame.display.Info()  # Obtém a resolução atual da tela do usuário
window_width = size_window.current_w
window_heigth = size_window.current_h
window = pygame.display.set_mode((window_width, window_heigth), pygame.FULLSCREEN)
pygame.display.set_caption('Troca de Frames com Pygame')


# Colors
color_text = (255, 255, 255)  # Branco


# Fonts
font_title_eco_logica = pygame.font.Font('Fonts/emmasophia.ttf', 80)
font_subtitle_eco_logica = pygame.font.Font('Fonts/emmasophia.ttf', 25)


# Images
image_home_icon = pygame.image.load("Images/home_icon.png")
image_banana = pygame.image.load("Images/banana.png")
image_scenario_1 = pygame.image.load("Images/scenario_1.png")
image_scenario_2 = pygame.image.load("Images/praia_1.png")

# Função principal do jogo
def main():
    # Estado do frame (1 ou 2)
    frame_atual = 1

    while True:
        #TV.get_data()
        
        
        # Verifica eventos (como fechamento da janela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
            # Verifica se o botão foi clicado
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_quit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

                if frame_atual == 1:
                    if btn_start_game.collidepoint(event.pos):
                        frame_atual = 2


                elif frame_atual == 2:
                    if btn_home_icon.collidepoint(event.pos):
                        frame_atual = 1

        # Desenha o frame atual
        if frame_atual == 1:
            draw_frame_home_screen()
            btn_start_game, btn_quit = buttons_home_screen()
        else:
            draw_frame_scenario_1()
            btn_home_icon, btn_quit = buttons_scenario_1()

        # Atualiza a tela
        pygame.display.update()


# Chamando a função principal
if __name__ == "__main__":
    main()

    # while(trashScenarios < 7):
    #     while(trashNumber >= 0):
    #         get_data()
    #     trashNumber = 5
    #     trashScenarios += 1