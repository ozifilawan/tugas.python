import pygame

pygame.init()

tinggi = 600
lebar = 600

screen = pygame.display.set_mode([tinggi,lebar])



#mengubah title sceern
pygame.display.set_caption('game gak jelas')
# pygame.draw.circle(screen,(0,0,150),(300,300),75)
icone = pygame.image.load('smart-car.png')
pygame.display.set_icon(icone)
def plane(x,y):
    image = pygame.image.load('electric-bus.png')
    screen.blit(image,(x,y))

x = 100
y = 300

x_point = 0
y_point = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            running= False

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point -= 0.1
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point += 0.1
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point -= 0.1
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point += 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point = 0
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point = 0
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point = 0
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point = 0
        
    screen.fill((255,0,0))
    
    x += x_point
    y +=y_point

    plane(x,y)
    pygame.display.update()

pygame.quit()