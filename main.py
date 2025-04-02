from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("FPUIT NINJA")

def run():
    game = True
    start_time = 0
    clock = pygame.time.Clock()




    font = pygame.font.Font(None, 60)


    what_window = "menu"

    rect_start = pygame.Rect(size_window [0] // 2 - 125, 200, 250, 80)

    rect_end = pygame.Rect(size_window [0] // 2 - 125, 350, 250, 80)

    text_start = font.render("START", True, colors ["BLACK"])

    text_end = font.render("EXIT", True, colors ["BLACK"])

    while game:

        events = pygame.event.get()


    #список всіх подій, для зручності, записали в змінну events

    #MENU

        if what_window == "menu":
            window.fill(colors["BLACK"])

        pygame.draw.rect(window, colors ["RED"], rect_start)
        pygame.draw.rect(window, colors ["RED"], rect_end)
        window.blit(text_start, (rect_start.x + 55, rect_start.y +20))
        window.blit(text_end, (rect_end.x + 75, rect_end.y +20))

        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                x, y = event.pos

                if rect_start.collidepoint(x, y):

                    what_window = "game"

                elif rect_end.collidepoint(x, y):

                    game = False


        clock.tick(FPS)                    
        pygame.display.flip()
run()