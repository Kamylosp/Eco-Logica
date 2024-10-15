import pygame
import os
from main import *

def buttons_home_screen():

    # Button start game
    button_start_game = pygame.Rect(window_width *0.5 -150, window_heigth*0.5-25, 300, 50)
    pygame.draw.rect(window, (0, 100, 0), button_start_game)
    font_start_button = pygame.font.Font('Fonts/emmasophia.ttf', 20)
    text_button_start_game = font_start_button.render("Start Game", True, (255, 255, 255))
    x = int(button_start_game.x) + int(button_start_game.width/2) - int(text_button_start_game.get_width()/2)
    y = int(button_start_game.y) + int(button_start_game.height/2) - int(text_button_start_game.get_height()/2)
    window.blit(text_button_start_game, (x, y))


    button_quit = pygame.Rect(window_width*0.95, 0, window_width*0.05, window_width*0.05)
    pygame.draw.rect(window, (0, 80, 0), button_quit)
    font_start_button = pygame.font.Font('Fonts/emmasophia.ttf', 25)
    text_button_quit = font_start_button.render("x", True, (255,0 , 0))
    x = int(button_quit.x) + int(button_quit.width/2) - int(text_button_quit.get_width()/2)
    y = int(button_quit.y) + int(button_quit.height/2) - int(text_button_quit.get_height()/2)
    window.blit(text_button_quit, (x, y))

    return button_start_game, button_quit

def buttons_scenario_1():

    # Button home icon
    image_resized = pygame.transform.scale(image_home_icon, (window_heigth*0.1, window_heigth*0.1))
    button_home_icon = image_resized.get_rect()
    button_home_icon.topleft = (0, 0)
    window.blit(image_resized, button_home_icon.topleft)

    # Button quit
    button_quit = pygame.Rect(window_width*0.95, 0, window_width*0.05, window_width*0.05)
    pygame.draw.rect(window, (0, 80, 0), button_quit)
    font_start_button = pygame.font.Font('Fonts/emmasophia.ttf', 25)
    text_button_quit = font_start_button.render("x", True, (255,0 , 0))
    x = int(button_quit.x) + int(button_quit.width/2) - int(text_button_quit.get_width()/2)
    y = int(button_quit.y) + int(button_quit.height/2) - int(text_button_quit.get_height()/2)
    window.blit(text_button_quit, (x, y))

    return button_home_icon, button_quit

def buttons_scenario_2():

    # Button home icon
    image_resized = pygame.transform.scale(image_home_icon, (window_heigth*0.1, window_heigth*0.1))
    button_home_icon = image_resized.get_rect()
    button_home_icon.topleft = (0, 0)
    window.blit(image_resized, button_home_icon.topleft)

    # Button quit
    button_quit = pygame.Rect(window_width*0.95, 0, window_width*0.05, window_width*0.05)
    pygame.draw.rect(window, (0, 80, 0), button_quit)
    font_start_button = pygame.font.Font('Fonts/emmasophia.ttf', 25)
    text_button_quit = font_start_button.render("x", True, (255,0 , 0))
    x = int(button_quit.x) + int(button_quit.width/2) - int(text_button_quit.get_width()/2)
    y = int(button_quit.y) + int(button_quit.height/2) - int(text_button_quit.get_height()/2)
    window.blit(text_button_quit, (x, y))

    return button_home_icon, button_quit

    

def draw_frame_home_screen():
    # Background color
    color_background_frame = (0, 200, 0)
    window.fill(color_background_frame)

    # Title Eco-Lógica
    text = font_title_eco_logica.render("Eco-Logica", True, color_text)
    window.blit(text, (int(window_width *0.5 -(text.get_size()[0])*0.5), int(window_heigth*0.2 -(text.get_size()[1])*0.5)))
    
    # Sub-title
    text = font_subtitle_eco_logica.render("Uma forma divertida de ajudar o meio ambiente", True, color_text)
    window.blit(text, (int(window_width *0.5 -(text.get_size()[0])*0.5), int(window_heigth*0.35 -(text.get_size()[1])*0.5)))

def draw_frame_scenario_1():
    # Image as background
    background_1 = pygame.transform.scale(image_scenario_1, (window_width, window_heigth))
    window.blit(background_1, (0,0))

    # Title Eco-Logica
    text = font_title_eco_logica.render("Cenario 1", True, (255, 0, 0))
    window.blit(text, (int(window_width *0.5 -(text.get_size()[0])*0.5), int(window_heigth*0.2 -(text.get_size()[1])*0.5)))
    

def draw_frame_scenario_2():
    # Image as background
    background_2 = pygame.transform.scale(image_scenario_2, (window_width, window_heigth))
    window.blit(background_2, (0,0))

    # Title Eco-Logica
    text = font_title_eco_logica.render("Cenario 2", True, (255, 0, 0))
    window.blit(text, (int(window_width *0.5 -(text.get_size()[0])*0.5), int(window_heigth*0.2 -(text.get_size()[1])*0.5)))
    