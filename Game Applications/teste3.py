import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Texto Extenso em Retângulo")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
azul_claro = (173, 216, 230)

# Configuração da fonte
fonte = pygame.font.SysFont('Arial', 30)

# Texto a ser exibido
texto_extenso = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor, nisl vitae tincidunt lacinia,
nisl ipsum ultricies est, quis tristique ligula turpis id justo. Integer dictum sagittis mauris non
faucibus. In volutpat, massa et faucibus egestas, nulla odio tincidunt arcu, euismod feugiat nunc
velit in urna. Fusce tincidunt, mauris et rhoncus dictum, erat arcu porta tortor, sed cursus lorem
odio et libero. Nullam quis scelerisque velit. Integer ut magna in nulla sodales tempus. Nam cursus
metus at sapien commodo, a pretium nulla vehicula.
"""

# Coordenadas e dimensões do retângulo
rect_x = 50
rect_y = 50
rect_largura = 700
rect_altura = 500

# Dividir o texto em linhas
linhas = texto_extenso.split('\n')

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Preenche a tela com a cor de fundo
    screen.fill(branco)
    
    # Desenha o retângulo
    pygame.draw.rect(screen, azul_claro, (rect_x, rect_y, rect_largura, rect_altura), 2)
    
    # Renderizar cada linha de texto dentro do retângulo
    y_offset = rect_y + 10  # Deslocamento inicial dentro do retângulo
    for linha in linhas:
        if y_offset + 40 > rect_y + rect_altura:  # Verifica se a linha cabe dentro do retângulo
            break
        texto = fonte.render(linha, True, preto)
        screen.blit(texto, (rect_x + 10, y_offset))
        y_offset += 40  # Incrementar o deslocamento vertical para a próxima linha

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
sys.exit()
