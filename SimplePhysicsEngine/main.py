import pygame
from dynamics import Body, PIXELS_PER_METER
from collision import wall_collision, circle_collision

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

bodies = []

running = True
while running:
    dt = 1 / 60.0
    clock.tick(60)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            x_m = mx / PIXELS_PER_METER 
            y_m = my / PIXELS_PER_METER
            bodies.append(Body(x_m, y_m, radius_m=0.2, mass_kg=1.0))

    for i, body in enumerate(bodies):
        body.update(dt)
        wall_collision(body, width, height, PIXELS_PER_METER)

        for j in range(i + 1, len(bodies)):
            circle_collision(body, bodies[j])

        pygame.draw.circle(
            screen,
            (0, 100, 255),
            (int(body.x * PIXELS_PER_METER), int(body.y * PIXELS_PER_METER)),
            int(body.radius * PIXELS_PER_METER)
        )

    pygame.display.flip()

pygame.quit()
