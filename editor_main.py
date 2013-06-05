#!/usr/bin/python
#-*- coding: utf-8 -*-


import pygame
import interpreter
import pygame_editor


editor = pygame_editor.Editor()


pygame.init()
pygame.display.set_caption("lemonade")
#sdl, which pygame is based on, has its own keyboard delay and repeat rate
pygame.key.set_repeat(300,30)
#this creates a window
pygame.display.set_mode((640,screen_height))
#in python, ctrl-c (sigint) causes KeyboardInterrupt exception
#but pygame.event.wait() is stuck somewhere in sdl and doesnt know
#anything about that...
pygame.time.set_timer(pygame.USEREVENT, 40)


#the final version is planned to use comic sans ✈
font = pygame.font.SysFont('monospace', 16)
font.width = font.render(" ",False,(0,0,0)).get_rect().width


def process_event(event):
	if event.type == pygame.QUIT:
		bye()
	if event.type == pygame.KEYDOWN:
		editor.key(event)


def draw():
	screen_surface.fill((0,0,0))
	editor.draw()
	#status bar and clock:P
	pygame.display.update()



def loop():
	process_event(pygame.event.wait())
	draw()


def bye():
	#save()
	exit()


while 1:
	try:
		loop()
	except KeyboardInterrupt() as e:
		#hide and slowly die
		pygame.display.iconify()
		raise e
	except Exception() as e:
		pass
