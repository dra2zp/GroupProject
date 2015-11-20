import pygame
from random import randint

dog_path = pygame.image.load("dog.jpg")
cat_path = pygame.image.load("cat.jpg")

class DogImage(object):
    def __init__(self, image):
        self.image = dog_path
        self.rect = dog_path.get_rect()
        self.a = 0
        self.b = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 0.5
        if key[pygame.K_DOWN]:
            self.b += dist

        elif key[pygame.K_UP]:
            self.b -= dist

        if key[pygame.K_RIGHT]:
            self.a += dist

        elif key[pygame.K_LEFT]:
            self.a -= dist

    def draw_dog(self, surface):
        surface.blit(self.image, (self.a, self.b))

class CatImage(object):
    def __init__(self, image):
        self.image = cat_path
        self.rect = cat_path.get_rect()
        self.c = 250
        self.d = 250

    def handle_random(self):
        dist = 10
        if ((randint(1,2) == 1) and (self.d < 500)):
            self.d += dist

        elif (self.d > 0):
            self.d -= dist

        else:
            self.d += 0

        if ((randint(1,2) == 1) and (self.c < 500)):
            self.c += dist

        elif (self.c > 0):
            self.c -= dist

        else:
            self.c += 0

    def draw_cat(self, surface):
        surface.blit(self.image, (self.c, self.d))

    #def checkCollision(sprite1, sprite2):
    #    collision = pygame.sprite.spritecollide(sprite1, sprite2, False)
    #    if collision == True:
    #        pygame.quit()

pygame.init()#rdy
screen = pygame.display.set_mode((500, 500))

#dog_rect = dog_path.get_rect()
#cat_rect = cat_path.get_rect()

dogImage = DogImage(dog_path)
catImage = CatImage(cat_path)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        #CatImage.draw_cat(cat_path, (self.c, self.d))
        #DogImage.draw_dog(dog_path, (self.a, self.b))
        #if (event.type == None):
            #running = True
        #elif (DogImage(self.rect).colliderect(CatImage(self.rect))):
            #running = False
        if (event.type == pygame.QUIT):
            pygame.quit()
            running = False
        if ((abs(dogImage.a) >= abs(catImage.c - 25)) and (abs(dogImage.b) >= abs(catImage.d - 25))):
            pygame.quit()
            running = False
        #CatImage.checkCollision(dogImage.image_a, catImage.image_c)
        #elif (CatImage.checkCollision(dogImage.rect, catImage.rect)):
        #    pygame.quit()
        #    running = False


        #elif (dogImage.collide(catImage)):
        #    running = False
        #elif (abs(self.a - self.c) < 12.5):
        #    running = False
        #elif (abs(self.b - self.d) < 12.5):
        #    running = False

    dogImage.handle_keys()
    catImage.handle_random()

    screen.fill((255, 255, 255))
    dogImage.draw_dog(screen)
    catImage.draw_cat(screen)
    pygame.display.update()

    clock.tick(40)
