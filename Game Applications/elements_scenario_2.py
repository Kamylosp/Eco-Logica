import pygame
from main import *

def buttons_scenario_2(image_home_icon, window_heigth, window_width, window, font_quit_button):

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

    
def draw_frame_scenario_2(image_scenario_2, window_width, window_heigth, window, font_title_eco_logica, Image_waste):
    # Image as background
    background_2 = pygame.transform.scale(image_scenario_2, (window_width, window_heigth))
    window.blit(background_2, (0,0))

    # Title Eco-Logica
    text = font_title_eco_logica.render("Cenario 2", True, (255, 0, 0))
    window.blit(text, (int(window_width *0.5 -(text.get_size()[0])*0.5), int(window_heigth*0.2 -(text.get_size()[1])*0.5)))
    