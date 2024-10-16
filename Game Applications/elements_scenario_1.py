import pygame

def buttons_scenario_1(image_home_icon, window_heigth, window_width, window, font_quit_button):

    # Button home icon
    image_resized = pygame.transform.scale(image_home_icon, (window_heigth*0.1, window_heigth*0.1))
    button_home_icon = image_resized.get_rect()
    button_home_icon.topleft = (0, 0)
    window.blit(image_resized, button_home_icon.topleft)

    # Button quit
    button_quit = pygame.Rect(window_width*0.95, 0, window_width*0.05, window_width*0.05)
    pygame.draw.rect(window, (0, 80, 0), button_quit)
    text_button_quit = font_quit_button.render("x", True, (255,0 , 0))
    x = int(button_quit.x) + int(button_quit.width/2) - int(text_button_quit.get_width()/2)
    y = int(button_quit.y) + int(button_quit.height/2) - int(text_button_quit.get_height()/2)
    window.blit(text_button_quit, (x, y))

    return button_home_icon, button_quit

def draw_frame_scenario_1(image_scenario_1, window_width, window_heigth, window, font_title_eco_logica, Image_waste):
    # Image as background
    background_1 = pygame.transform.scale(image_scenario_1, (window_width, window_heigth))
    window.blit(background_1, (0,0))



    resized_image = pygame.transform.scale(Image_waste['casca_banana'], (140, 140))  # Redimensiona a imagem se necessário

    x = 1370 - int(resized_image.get_width()/2)
    y = 700 - int(resized_image.get_height()/2)
    window.blit(resized_image, (x, y))

    resized_image = pygame.transform.scale(Image_waste['lata_refrigerante'], (160, 160))  # Redimensiona a imagem se necessário
    x = 350 - int(resized_image.get_width()/2)
    y = 730 - int(resized_image.get_height()/2)
    window.blit(resized_image, (x, y))

    resized_image = pygame.transform.scale(Image_waste['jornal'], (170, 170))  # Redimensiona a imagem se necessário
    x = 1650 - int(resized_image.get_width()/2)
    y = 860 - int(resized_image.get_height()/2)
    window.blit(resized_image, (x, y))


    # Title Eco-Logica
    text = font_title_eco_logica.render("Cenario 1", True, (255, 0, 0))
    window.blit(text, (int(window_width *0.5 -(text.get_size()[0])*0.5), int(window_heigth*0.2 -(text.get_size()[1])*0.5)))