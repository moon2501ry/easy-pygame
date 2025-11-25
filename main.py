import easy_pygame as epygame

epygame.init();
player = epygame.Entity((4,8));
clicks = 0;

while True:
    epygame.get_events();
    if epygame.isquiting(): quit();
    if epygame.keyboard_check(epygame.pygame.K_a): player.position.goto("left",20);
    if epygame.keyboard_check(epygame.pygame.K_d): player.position.goto("right",20);
    if epygame.keyboard_check(epygame.pygame.K_s): player.position.goto("down",20);
    if epygame.keyboard_check(epygame.pygame.K_w): player.position.goto("up",20);
    epygame.init_render();
    epygame.pygame.draw.circle(epygame.screen, "purple", player.position(), 30);
    epygame.final_render();