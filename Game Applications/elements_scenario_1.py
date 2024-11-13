import pygame

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    while words:
        line_words = []
        while words and font.size(' '.join(line_words + [words[0]]))[0] <= max_width:
            line_words.append(words.pop(0))
        lines.append(' '.join(line_words))
    return lines




def buttons_scenario_1(image_home_icon, window_heigth, window_width, window, font_quit_button):

    # Button home icon
    image_resized = pygame.transform.scale(image_home_icon, (window_heigth*0.1, window_heigth*0.1))
    button_home_icon = image_resized.get_rect()
    button_home_icon.topleft = (0, 0)
    window.blit(image_resized, button_home_icon.topleft)

    # Button quit
    button_quit = pygame.Rect(window_width*0.95, 0, window_width*0.05, window_width*0.05)
    pygame.draw.rect(window, (245, 245, 220), button_quit)
    text_button_quit = font_quit_button.render("x", True, (255,0 , 0))  
    x = int(button_quit.x) + int(button_quit.width/2) - int(text_button_quit.get_width()/2)
    y = int(button_quit.y) + int(button_quit.height/2) - int(text_button_quit.get_height()/2)
    window.blit(text_button_quit, (x, y))

    return button_home_icon, button_quit

def draw_frame_scenario_1(image_scenario_1, window_width, window_heigth, window, Image_waste, state_elements):
    # Image as background
    background_1 = pygame.transform.scale(image_scenario_1, (window_width, window_heigth))
    window.blit(background_1, (0,0))

    font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', 40)
    rect_text = pygame.Rect(0, 0, window_width, window_heigth*0.1)
    pygame.draw.rect(window, (245, 245, 220), rect_text)
    text_rect_text = font.render("Elementos já depositados: ", True, (0, 100, 0))
    x = int(rect_text.x) + int(rect_text.width/2) - int(text_rect_text.get_width()/2)
    y = int(rect_text.y) + int(rect_text.height/2) - int(text_rect_text.get_height()/2)
    window.blit(text_rect_text, (x, y))

    elements_already_deposited_correct = 0

    # Casca de banana
    if state_elements["casca_banana"] == 0:
        resized_image = pygame.transform.scale(Image_waste['casca_banana'], (140, 140))  # Redimensiona a imagem se necessário
        x = window_width*0.55 - int(resized_image.get_width()/2)
        y = window_heigth*0.68 - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, y))
    else:
        resized_image = pygame.transform.scale(Image_waste['casca_banana'], (rect_text.height, rect_text.height))  # Redimensiona a imagem se necessário
        x = int(rect_text.width/2) + int(text_rect_text.get_width()/2) + elements_already_deposited_correct*(rect_text.height+15) + 15
        y = int(text_rect_text.get_height()/2) - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, max(y, 0)))
        elements_already_deposited_correct += 1

    # Jornal
    if state_elements["jornal"] == 0:
        resized_image = pygame.transform.scale(Image_waste['jornal'], (170, 170))  # Redimensiona a imagem se necessário
        x = window_width*0.82 - int(resized_image.get_width()/2)
        y = window_heigth*0.79 - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, y))

    else:
        resized_image = pygame.transform.scale(Image_waste['jornal'], (rect_text.height, rect_text.height))  # Redimensiona a imagem se necessário
        x = int(rect_text.width/2) + int(text_rect_text.get_width()/2) + elements_already_deposited_correct*(rect_text.height+15) + 15
        y = int(text_rect_text.get_height()/2) - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, max(y, 0)))
        elements_already_deposited_correct += 1

    # Lata de refrigerante
    if state_elements["lata_refrigerante"] == 0:
        resized_image = pygame.transform.scale(Image_waste['lata_refrigerante'], (160, 160))  # Redimensiona a imagem se necessário
        x = window_width*0.19 - int(resized_image.get_width()/2)
        y = window_heigth*0.70 - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, y))
    else:
        resized_image = pygame.transform.scale(Image_waste['lata_refrigerante'], (rect_text.height, rect_text.height))  # Redimensiona a imagem se necessário
        x = int(rect_text.width/2) + int(text_rect_text.get_width()/2) + elements_already_deposited_correct*(rect_text.height+15) + 15
        y = int(text_rect_text.get_height()/2) - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, max(y, 0)))
        elements_already_deposited_correct += 1

    # Caixa de exibição de texto quando acertou
    if (state_elements["casca_banana"] + state_elements["jornal"] + state_elements["lata_refrigerante"])%2 == 1:
        larg = window_heigth*1
        alt1 = window_heigth*0.15
        alt2 = window_heigth*0.3
        font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', 40)
        rect_text = pygame.Rect(window_width*0.5 -larg/2, window_heigth*0.5 -(alt1+alt2)/2, larg, alt1)
        pygame.draw.rect(window, (203,238,203), rect_text)

        string = "Parabens! Você acertou!"

        text_rect_text = font.render(string, True, (0, 100, 0))
        x = int(rect_text.x) + int(rect_text.width/2) - int(text_rect_text.get_width()/2)
        y = int(rect_text.y) + int(rect_text.height/2) - int(text_rect_text.get_height()/2)
        window.blit(text_rect_text, (x, y))

        if state_elements["casca_banana"] == 1:
            string = "A casca de banana é um valioso fertilizante natural porque é rica em potássio, fósforo e magnésio, essenciais para o crescimento saudável de diversas plantas, como o tomate, pepinos e rosas"
        
        elif state_elements["jornal"] == 1:
            string = "texto jornal"
        
        else:
            string = "texto lata de refrigerante"

        font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', 30)
        rect_background = pygame.Rect(window_width*0.5- larg/2, window_heigth*0.5 -(alt1+alt2)/2 + alt1-1, larg, alt2)
        pygame.draw.rect(window, (203,238,203), rect_background)

        linhas = wrap_text(string, font, rect_background.width - 20)

        y_offset = rect_background.y + 10  # Deslocamento inicial dentro do retângulo
        for linha in linhas:
            if y_offset + 40 > rect_background.y + rect_background.width:  # Verifica se a linha cabe dentro do retângulo
                break
            # Calcular a posição horizontal para centralizar a linha
            texto = font.render(linha, True, (0, 100, 0))
            texto_width = texto.get_width()
            x_offset = rect_background.x + (rect_background.width - texto_width) // 2
            window.blit(texto, (x_offset, y_offset))
            y_offset += 40  # Incrementar o deslocamento vertical para a próxima linha