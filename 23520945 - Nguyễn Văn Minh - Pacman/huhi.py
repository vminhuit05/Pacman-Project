import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Draw a blue arc
  pygame.draw.arc(screen, (0, 0, 255), (100, 100, 200, 100), 0, 3.14)  # Half circle

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
