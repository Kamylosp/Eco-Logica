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


def buttons_scenario_2(image_home_icon, window_heigth, window_width, window, font_quit_button):

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

def draw_frame_scenario_2(image_scenario_2, window_width, window_heigth, window, Image_waste, state_elements):
    # Image as background
    background_1 = pygame.transform.scale(image_scenario_2, (window_width, window_heigth))
    window.blit(background_1, (0,0))

    font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', int(window_heigth/22.5))
    rect_text = pygame.Rect(0, 0, window_width, window_heigth*0.1)
    pygame.draw.rect(window, (245, 245, 220), rect_text)
    text_rect_text = font.render("Elementos já depositados: ", True, (0, 100, 0))
    x = int(rect_text.x) + int(rect_text.width/2) - int(text_rect_text.get_width()/2)
    y = int(rect_text.y) + int(rect_text.height/2) - int(text_rect_text.get_height()/2)
    window.blit(text_rect_text, (x, y))

    elements_already_deposited_correct = 0

    # Casca de laranja
    if state_elements["casca_laranja"] == 0:
        resized_image = pygame.transform.scale(Image_waste['casca_laranja'], (int(window_heigth/5.3), int(window_heigth/5.3)))  # Redimensiona a imagem se necessário
        x = window_width*0.816 - int(resized_image.get_width()/2)
        y = window_heigth*0.796 - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, y))

    else:
        resized_image = pygame.transform.scale(Image_waste['casca_laranja'], (rect_text.height, rect_text.height))  # Redimensiona a imagem se necessário
        x = int(rect_text.width/2) + int(text_rect_text.get_width()/2) + elements_already_deposited_correct*(rect_text.height+15) + 15
        y = int(text_rect_text.get_height()/2) - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, max(y, 0)))
        elements_already_deposited_correct += 1

    # Garrafa de vidro
    if state_elements["garrafa_vidro"] == 0:
        resized_image = pygame.transform.scale(Image_waste['garrafa_vidro'], (int(window_heigth/7), int(window_heigth/5.62)))  # Redimensiona a imagem se necessário
        x = window_width*0.345 - int(resized_image.get_width()/2)
        y = window_heigth*0.76 - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, y))
    else:
        resized_image = pygame.transform.scale(Image_waste['garrafa_vidro'], (rect_text.height, rect_text.height))  # Redimensiona a imagem se necessário
        x = int(rect_text.width/2) + int(text_rect_text.get_width()/2) + elements_already_deposited_correct*(rect_text.height+15) + 15
        y = int(text_rect_text.get_height()/2) - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, max(y, 0)))
        elements_already_deposited_correct += 1

    # Copo de plástico
    if state_elements["copo_plastico"] == 0:
        resized_image = pygame.transform.scale(Image_waste['copo_plastico'], (int(window_heigth/5.62), int(window_heigth/5.62)))  # Redimensiona a imagem se necessário
        x = window_width*0.15 - int(resized_image.get_width()/2)
        y = window_heigth*0.92 - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, y))
    else:
        resized_image = pygame.transform.scale(Image_waste['copo_plastico'], (rect_text.height, rect_text.height))  # Redimensiona a imagem se necessário
        x = int(rect_text.width/2) + int(text_rect_text.get_width()/2) + elements_already_deposited_correct*(rect_text.height+15) + 15
        y = int(text_rect_text.get_height()/2) - int(resized_image.get_height()/2)
        window.blit(resized_image, (x, max(y, 0)))
        elements_already_deposited_correct += 1

    # Caixa de exibição de texto quando acertou
    if (state_elements["casca_laranja"] + state_elements["copo_plastico"] + state_elements["garrafa_vidro"])%2 == 1:
        larg = window_heigth*1
        alt1 = window_heigth*0.1
        alt2 = window_heigth*0.3
        alt3 = window_heigth*0.1

        font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', int(window_heigth/22))
        rect_text = pygame.Rect(window_width*0.5 -larg/2, window_heigth*0.5 -(alt1+alt2)/2, larg, alt1)
        pygame.draw.rect(window, (203,238,203), rect_text)

        string = "Parabens! Você acertou!"

        text_rect_text = font.render(string, True, (0, 100, 0))
        x = int(rect_text.x) + int(rect_text.width/2) - int(text_rect_text.get_width()/2)
        y = int(rect_text.y) + int(rect_text.height/2) - int(text_rect_text.get_height()/2)
        window.blit(text_rect_text, (x, y))


        if state_elements["casca_laranja"] == 1:
            string = "texto casca laranja"
        
        elif state_elements["garrafa_vidro"] == 1:
            string = "texto garrafa"
        else:
            string = "texto copo plastico"

        font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', int(window_heigth/28))
        rect_background = pygame.Rect(window_width*0.5- larg/2, window_heigth*0.5 -(alt1+alt2)/2 + alt1-1, larg, alt2)
        pygame.draw.rect(window, (203,238,203), rect_background)

        linhas = wrap_text(string, font, rect_background.width - 100)

        line_height = font.get_linesize()
        total_text_height = line_height * len(linhas)
        y_offset = rect_background.y + (rect_background.height - total_text_height) // 2

        for linha in linhas:
            if y_offset + 40 > rect_background.y + rect_background.width:  # Verifica se a linha cabe dentro do retângulo
                break
            # Calcular a posição horizontal para centralizar a linha
            texto = font.render(linha, True, (0, 100, 0))
            texto_width = texto.get_width()
            x_offset = rect_background.x + (rect_background.width - texto_width) // 2
            window.blit(texto, (x_offset, y_offset))
            y_offset += 40  # Incrementar o deslocamento vertical para a próxima linha

        rect_text = pygame.Rect(window_width*0.5 -larg/2, window_heigth*0.5 +(alt1+alt2)/2-1, larg, alt3)
        pygame.draw.rect(window, (203,238,203), rect_text)
        string = "Pressione espaço para continuar"

        font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', int(window_heigth/28))
        text_rect_text = font.render(string, True, (150, 0, 0))
        x = int(rect_text.x) + int(rect_text.width/2) - int(text_rect_text.get_width()/2)
        y = int(rect_text.y) + int(rect_text.height/2) - int(text_rect_text.get_height()/2)
        window.blit(text_rect_text, (x, y))
    
    elif (state_elements["casca_laranja"] + state_elements["copo_plastico"] + state_elements["garrafa_vidro"]) == 6:
        larg = window_heigth*1.2
        alt1 = window_heigth*0.1
        alt2 = window_heigth*0.3
        alt3 = window_heigth*0.1

        font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', int(window_heigth/22))
        rect_text = pygame.Rect(window_width*0.5 -larg/2, window_heigth*0.5 -(alt1+alt2)/2, larg, alt1)
        pygame.draw.rect(window, (203,238,203), rect_text)

        string = "Parabens! Você depositou todos corretamente!"

        text_rect_text = font.render(string, True, (0, 100, 0))
        x = int(rect_text.x) + int(rect_text.width/2) - int(text_rect_text.get_width()/2)
        y = int(rect_text.y) + int(rect_text.height/2) - int(text_rect_text.get_height()/2)
        window.blit(text_rect_text, (x, y))

        string = "TEXTO AO COMPLETAR CENÁRIO"

        font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', int(window_heigth/28))
        rect_background = pygame.Rect(window_width*0.5- larg/2, window_heigth*0.5 -(alt1+alt2)/2 + alt1-1, larg, alt2)
        pygame.draw.rect(window, (203,238,203), rect_background)

        linhas = wrap_text(string, font, rect_background.width - 100)

        line_height = font.get_linesize()
        total_text_height = line_height * len(linhas)
        y_offset = rect_background.y + (rect_background.height - total_text_height) // 2

        for linha in linhas:
            if y_offset + 40 > rect_background.y + rect_background.width:  # Verifica se a linha cabe dentro do retângulo
                break
            # Calcular a posição horizontal para centralizar a linha
            texto = font.render(linha, True, (0, 100, 0))
            texto_width = texto.get_width()
            x_offset = rect_background.x + (rect_background.width - texto_width) // 2
            window.blit(texto, (x_offset, y_offset))
            y_offset += 40  # Incrementar o deslocamento vertical para a próxima linha

        rect_text = pygame.Rect(window_width*0.5 -larg/2, window_heigth*0.5 +(alt1+alt2)/2-1, larg, alt3)
        pygame.draw.rect(window, (203,238,203), rect_text)
        string = "Pressione espaço para continuar"

        font = pygame.font.Font('Fonts/PoetsenOne-Regular.ttf', int(window_heigth/28))
        text_rect_text = font.render(string, True, (150, 0, 0))
        x = int(rect_text.x) + int(rect_text.width/2) - int(text_rect_text.get_width()/2)
        y = int(rect_text.y) + int(rect_text.height/2) - int(text_rect_text.get_height()/2)
        window.blit(text_rect_text, (x, y))