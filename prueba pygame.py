import pygame, sys #importando libreria
pygame.init() #inicializando pygame

color = (184,184,104)#fondo
size=(600,750) #dimensiones

#Crear ventana
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#subiendo el personaje, "alpha" es para poner la transparencia de la imagen
player = pygame.image.load("pixil-frame-0.png").convert_alpha()

#coordenadas del personaje
coord_x = 230
coord_y = 510
#velocidad
x_speed = 0
y_speed = 0

#salir del juego
while True:
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			sys.exit()
#configuracion de las telcas
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -4
			if event.key == pygame.K_RIGHT:
				x_speed = 4


		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_speed = 0
				pass
			if event.key == pygame.K_RIGHT:
				x_speed = 0
				pass

	coord_x += x_speed
	coord_y += y_speed
#fondo
	screen.fill(color)
#persona y colocacion en la imagen
	screen.blit(player, (coord_x, coord_y))
	pygame.display.flip()
	clock.tick(60)
