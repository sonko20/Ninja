from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("FPUIT NINJA")

def run():
    game = True
    start_time = 0
    clock = pygame.time.Clock()
    random_index_count_fruit = 1
    score = 0

    for i in range(3):
         cross_list.append(CrossLife(size_window[0] - 60 * i - 60, 10, [blue_cross_image, red_cross_image]))

    font = pygame.font.Font(None, 60)
    font_end = pygame.font.Font(None, 80)
    font_score = pygame.font.Font(None, 250)
    what_window = "menu"
    rect_start = pygame.Rect(size_window[0] //2-125, 200, 250, 80)
    rect_end = pygame.Rect(size_window[0] //2 - 125, 350, 250, 80)
    rect_restart = pygame.Rect(size_window[0] //2 - 250 - 20, size_window[1] // 2 + 100, 250, 80)
    rect_end_2 = pygame.Rect(size_window[0] // 2 + 20, size_window[1]//2 + 100, 250, 80)
    rect_menu_icon = pygame.Rect(rect_restart.x - 50, rect_start.y - 50, rect_start.width * 2 + 100 + 40, rect_end_2.bottom - rect_start.y + 100)
    text_start = font.render("START", True, colors["BLACK"])
    text_restart = font.render("RESTART", True, colors["BLACK"])
    text_end = font.render("EXIT", True, colors["BLACK"])
    text_score = font_end.render("SCORE", True, colors ["BLUE_DARK"])
    text_new = font_end.render("NEW BEST", True, colors["BLUE_DARK"])
    while game:

        events = pygame.event.get()


    #список всіх подій, для зручності, записали в змінну events

    #MENU

        if what_window == "menu":
            window.fill(colors["BLACK"])
            window.blit(bg_image, (0,0))

            pygame.draw.rect(window, colors["GREEN"], rect_menu_icon)
            pygame.draw.rect(window, colors["RED"], rect_start)
            pygame.draw.rect(window, colors["RED"], rect_end)
            window.blit(text_start, (rect_start.x + 55, rect_start.y +20))
            window.blit(text_end, (rect_end.x + 75, rect_end.y +20))

            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if rect_start.collidepoint(x,y):
                        what_window = "game"
                    elif rect_end.collidepoint(x,y):
                        game = False

        if what_window == "game menu":


    
            pygame.draw.rect(window, colors ["GREEN"], rect_menu_icon)
            pygame.draw.rect(window, colors["RED"], rect_restart)
            pygame.draw.rect(window, colors["RED"], rect_end_2)
            window.blit(text_restart, (rect_restart.x + 35, rect_restart.y +20))
            window.blit(text_end, (rect_end_2.x + 75, rect_end_2.y +20))
            window.blit(text_score, (size_window[0] // 2 - font_end.size("SCORE")[0] // 2, rect_menu_icon.y +20))
            window.blit(font_score.render(str(score), True, colors["BLUE_DARK"]),
                        (size_window[0] // 2 - font_score.size(str(score)) [0] // 2, rect_menu_icon.y +20 +70))
            if len(score_list) == 1 or max(score_list) <= score:
                    window.blit(text_new, (size_window[0]//2 - font_end.size ("NEW BEST")[0] // 2, rect_restart.y-80))
            for event in events:  
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if rect_restart.collidepoint(x, y):
                        what_window = "game"
                        score = 0
                        CrossLife.hp=3
                        for cross in cross_list:
                            cross.image = cross.cross_list[0]
                        random_index_count_fruit = 1
                    elif rect_end_2.collidepoint(x, y):
                        game = False
#GANE
        elif what_window == "game":

            #BLACKGROUND
            window.blit(bg_image, (0,0))
            window.blit(font_end.render(str(score), True, colors ["BLUE_DARK"]), (10, 10))
            #CROSS/WIN/LOSE
            for i in range(3):
                window.blit(cross_list[i].image, (cross_list[i].x, cross_list[i].y))

            if CrossLife.hp == 0:
                score_list.append(score)
                what_window = "game menu"

            if Knife.cut:
                x, y = pygame.mouse.get_pos()
                Knife.knife_cords_list.append(Knife(x, y, 10, 10, colors["WHITE"]))

            Knife.line(Knife(), window)

            for punch in Knife.knife_cords_list:
                punch.remove()

            #FRUIT CREATE/BLIT/MOVE/COLLIDE/REMOVE
            end_time = pygame.time.get_ticks()
            if end_time - start_time > 1500:
                count_fruit = random.randint(1, int(random_index_count_fruit))
                random_index_count_fruit += 0.2
                for i in range(count_fruit):
                    fruits_list.append(
                        Fruit(random.randint(0, size_window[0] -100), size_window[1], 83, 74, watermelon_image_list,
                        move_x = random.uniform (1.5, 3), power_throw = random.randint(13, 18)))
                start_time = end_time



            for fruit in fruits_list:
                window.blit(fruit.image_now, fruit.rect.topleft)
                fruit.move()

                if fruit.collide(Knife.knife_cords_list):
                        fruits_list.append(
                            Fruit(fruit.rect.x, fruit.rect.y, fruit.image_list[-1].get_rect().width, fruit.image_list[-1].get_rect().width,
                                [fruit.image_list[-1]], fruit.half, - fruit.move_x))

                        score += 1
                fruit.remove()

                
            for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        Knife.cut = True
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                            Knife.cut = False

        for event in events:
                    if event.type == pygame.QUIT:
                        game = False    

        clock.tick(FPS)                    
        pygame.display.flip()
run()