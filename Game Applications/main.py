import pygame
import sys
from elements_home_screen import *
from elements_scenario_1 import *
from elements_scenario_2 import *
from elements_scenario_3 import *
from arduino_communication import TrashVerifier as TV

# Inicializando o Pygame
pygame.init()

# Criando a janela em modo fullscreen
size_window = pygame.display.Info()  # Obtém a resolução atual da tela do usuário
window_width = size_window.current_w
window_heigth = size_window.current_h
window = pygame.display.set_mode((window_width, window_heigth), pygame.FULLSCREEN)
pygame.display.set_caption('Eco Logica')

# state = 0 -> elemento não depositado
# state = 1 -> elemento depositado, aviso sendo mostrado
# state = 2 -> lixo já guardado 
state_elements = {"casca_banana": 0,
                "casca_laranja": 0,
                "casca_ovo": 0,
                "copo_plastico": 0,
                "espinha_peixe": 0,
                "garrafa_pet": 0,
                "garrafa_vidro": 0,
                "jornal": 0,
                "lata_refrigerante": 0,
                "maca": 0}

# Colors
color_text = (255, 255, 255)  # Branco

# Fonts
font_title_eco_logica = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', 80)
font_subtitle_eco_logica = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', 25)
font_quit_button = pygame.font.Font('Fonts/emmasophia.ttf', 35)

# Images
image_home_icon = pygame.image.load("Images/Icons/home_icon.png")
image_scenario_1 = pygame.image.load("Images/Scenarios/scenario_1.png")
image_scenario_2 = pygame.image.load("Images/Scenarios/scenario_2.png")
image_scenario_3 = pygame.image.load("Images/Scenarios/scenario_3.png")

Image_waste = { "casca_banana": pygame.image.load("Images/Waste/casca_banana.png"),
                "casca_laranja": pygame.image.load("Images/Waste/casca_laranja.png"),
                "casca_ovo": pygame.image.load("Images/Waste/casca_ovo.png"),
                "copo_plastico": pygame.image.load("Images/Waste/copo_plastico.png"),
                "espinha_peixe": pygame.image.load("Images/Waste/espinha_peixe.png"),
                "garrafa_pet": pygame.image.load("Images/Waste/garrafa_pet.png"),
                "garrafa_vidro": pygame.image.load("Images/Waste/garrafa_vidro.png"),
                "jornal": pygame.image.load("Images/Waste/jornal.png"),
                "lata_refrigerante": pygame.image.load("Images/Waste/lata_refrigerante.png"),
                "maca": pygame.image.load("Images/Waste/miolo_maca.png")}

def main():
    frame_atual = 0

    while True:
        # Verifica eventos (como fechamento da janela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_b:
                    state_elements["casca_banana"] = 1

                if event.key == pygame.K_r:
                    state_elements["lata_refrigerante"] = 1

                if event.key == pygame.K_j:
                    state_elements["jornal"] = 1

                if event.key == pygame.K_SPACE:

                    if frame_atual == 1 and (state_elements['casca_banana'] + state_elements['jornal'] + state_elements['lata_refrigerante']) == 6:
                        frame_atual = 2

                    # Verificação para tirar barra de aviso de correto
                    if state_elements['casca_banana'] == 1:
                        state_elements['casca_banana'] = 2
                    
                    if state_elements['jornal'] == 1:
                        state_elements['jornal'] = 2
                    
                    if state_elements['lata_refrigerante'] == 1:
                        state_elements['lata_refrigerante'] = 2
                        

                if event.key == pygame.K_RIGHT:
                    if frame_atual == 0:
                        pass

                    elif frame_atual == 1:
                        frame_atual = 2

                    elif frame_atual == 2:
                        frame_atual = 3
                    
                    elif frame_atual == 3:
                        frame_atual = 1

            # Verifica se o botão foi clicado
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"scenario: {frame_atual} pos:{event.pos}")
                if btn_quit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

                if frame_atual == 0:
                    if btn_start_game.collidepoint(event.pos):
                        frame_atual = 1

                elif frame_atual == 1:
                    if btn_home_icon.collidepoint(event.pos):
                        frame_atual = 0

                elif frame_atual == 2:
                    if btn_home_icon.collidepoint(event.pos):
                        frame_atual = 0

                elif frame_atual == 3:
                    if btn_home_icon.collidepoint(event.pos):
                        frame_atual = 0

        # Desenha o frame atual
        if frame_atual == 0:
            draw_frame_home_screen(window_heigth, window_width, window, font_title_eco_logica, font_subtitle_eco_logica, color_text, Image_waste)
            btn_start_game, btn_quit = buttons_home_screen(window_heigth, window_width, window, font_quit_button)

        elif frame_atual == 1:
            draw_frame_scenario_1(image_scenario_1, window_width, window_heigth, window, Image_waste, state_elements)
            btn_home_icon, btn_quit = buttons_scenario_1(image_home_icon, window_heigth, window_width, window, font_quit_button)

        elif frame_atual == 2:
            draw_frame_scenario_2(image_scenario_2, window_width, window_heigth, window, font_title_eco_logica, Image_waste)
            btn_home_icon, btn_quit = buttons_scenario_2(image_home_icon, window_heigth, window_width, window, font_quit_button)
        
        elif frame_atual == 3:
            draw_frame_scenario_3(image_scenario_3, window_width, window_heigth, window, font_title_eco_logica, Image_waste)
            btn_home_icon, btn_quit = buttons_scenario_3(image_home_icon, window_heigth, window_width, window, font_quit_button)

        # Atualiza a tela
        pygame.display.update()

# Chamando a função principal
if __name__ == "__main__":
    print("window", window_heigth)
    main()


    # while(trashScenarios < 7):
    #     while(trashNumber >= 0):
    #         get_data()
    #     trashNumber = 5
    #     trashScenarios += 1