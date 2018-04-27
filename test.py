import pygame
from variables import *

pygame.init()



def main():
    sw, sh = 600, 400
    screen = pygame.display.set_mode((sw, sh))
    font_p1, font_p2 = font_30, font_30
    p1_input_box = pygame.Rect(screen.get_rect().centerx - 100, 140, 200, 45)
    p2_input_box = pygame.Rect(screen.get_rect().centerx - 100, 200, 200, 45)

    clock = pygame.time.Clock()

    color_inactive_p1 = pygame.Color('lightskyblue3')
    color_active_p1 = pygame.Color('dodgerblue2')
    color_p1 = color_inactive_p1
    color_inactive_p2 = pygame.Color('mediumorchid1')
    color_active_p2 = pygame.Color('mediumorchid3')
    color_p2 = color_inactive_p2

    active_p1 = False
    active_p2 = False
    text_p1, text_p2 = '', ''

    text = 'Enter player names and play!'
    text_button = 'start game'
    button = pygame.Rect(screen.get_rect().centerx - 85, 300, 170, 50)
    draw_line = False

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if p1_input_box.collidepoint(event.pos):
                    # Toggle the active_p1 variable.
                    active_p1 = not active_p1
                    active_p2 = False if active_p1 else True
                else:
                    active_p1 = False

                if p2_input_box.collidepoint(event.pos):
                    # Toggle the active_p1 variable.
                    active_p2 = not active_p2
                    active_p1 = False if active_p2 else True
                else:
                    active_p2 = False

                # Change the current color of the input box.
                color_p1 = color_active_p1 if active_p1 else color_inactive_p1
                font_p1 = font_semibold_30 if active_p1 else font_30

                color_p2 = color_active_p2 if active_p2 else color_inactive_p2
                font_p2 = font_semibold_30 if active_p2 else font_30

                if button.collidepoint(event.pos):
                    if text_p1 == '' or text_p2 == '':
                        draw_line = True
                    else:
                        done = True

            if event.type == pygame.KEYDOWN:
                if active_p1:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        text_p1 = text_p1[:-1]
                    else:
                        text_p1 += event.unicode
                if active_p2:
                    if event.key == pygame.K_RETURN:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        text_p2 = text_p2[:-1]
                    else:
                        text_p2 += event.unicode

                if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                    if text_p1 == '' or text_p2 == '':
                        draw_line = True
                    else:
                        done = True


        screen.fill(WHITE)

        # Main text
        txt = font_semibold_30.render(text, True, BLACK)
        txt_button = font_semibold_24.render(text_button, True, BLACK)
        
        # Render the current text.
        txt_p1 = font_p1.render(text_p1, True, color_p1)
        txt_p2 = font_p2.render(text_p2, True, color_p2)

        # Resize the box if the text is too long.
        p1_width = max(200, txt_p1.get_width() + 30)
        p2_width = max(200, txt_p2.get_width() + 30)

        p1_input_box = pygame.Rect(screen.get_rect().centerx - int(p1_width/2), 140, p1_width, 45)
        p2_input_box = pygame.Rect(screen.get_rect().centerx - int(p2_width/2), 200, p2_width, 45)

        # Blit the text_p1.
        screen.blit(txt_p1, (p1_input_box.centerx - int(txt_p1.get_rect().width/2), p1_input_box.y + 5))
        screen.blit(txt_p2, (p2_input_box.centerx - int(txt_p2.get_rect().width/2), p2_input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color_p1, p1_input_box, 4 if active_p1 else 2)
        pygame.draw.rect(screen, color_p2, p2_input_box, 4 if active_p2 else 2)

        # Blit button
        pygame.draw.rect(screen, GRAY, button)
        pygame.draw.rect(screen, BLACK, button, 2)
        screen.blit(txt_button, (button.centerx - int(txt_button.get_rect().width / 2), 310))
        # Blit the main text
        screen.blit(txt, (int(sw/2) - int(txt.get_rect().width / 2), 50))
        if draw_line:
            pygame.draw.line(screen, BLACK, [(int(sw/2) - int(txt.get_rect().width / 2) - 5), 90],
                             [(int(sw/2) - int(txt.get_rect().width / 2) + 257), 90], 3)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


main()

