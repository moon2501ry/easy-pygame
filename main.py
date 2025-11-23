import easy_pygame as epygame

epygame.init();
player = epygame.Entity((4,8));
clicks = 0;

while True:
    epygame.get_events();
    if epygame.isquiting(): quit();
    if epygame.keyboard_check(epygame.pygame.K_a): player.position.goto("left",.1);
    if epygame.keyboard_check(epygame.pygame.K_d): player.position.goto("right",.1);
    if epygame.keyboard_check(epygame.pygame.K_s): player.position.goto("down",.1);
    if epygame.keyboard_check(epygame.pygame.K_w): player.position.goto("up",.1);
    print(player.position);