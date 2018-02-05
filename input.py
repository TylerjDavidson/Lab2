#!/usr/bin/py


while(true):
  draw_world(window)
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN
      if event.key == K_UP
        Launcher.changeAngle(3)
    if event.type == pygame.KEYUP
      if event.key == K_DOWN
        Launcher.changeAngle(-3)
    if event.type == pygame.KEYLEFT
      if event.key == K_LEFT
        Launcher.changeMagnitude(-3)
    if event.type == pygame.KEYRIGHT
      if event.key == K_RIGHT
        Launcher.changeMagnitude(3)
    if event.type == QUIT
      pygame.quit()
      sys.exit()
   Launcher.draw(window)
   pygame.display.update()
   fpdClock.tick(FPS)
