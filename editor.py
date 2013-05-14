#!/usr/bin/python
#-*- coding: utf-8 -*-


import pygame
import interpreter2
import editmachine
import block

editor = editmachine.EditMachine()


pygame.init()
pygame.display.set_caption("lemonade")
#sdl, which pygame is based on, has its own keyboard delay and repeat rate
pygame.key.set_repeat(300,30)
#this creates a window
pygame.display.set_mode((640,screen_height))


#the final version is planned to use comic sans ✈
font = pygame.font.SysFont('monospace', 16)
font.width = font.render(" ",False,(0,0,0)).get_rect().width


def process_event(event):
	if event.type == pygame.QUIT:
		bye()
	if event.type == pygame.KEYDOWN:
		editor.key(event)

def loop():
	process_event(pygame.event.wait())
	draw()

def bye():
	#save()
	exit()

pygame.time.set_timer(pygame.USEREVENT, 40)#SIGINT timer:
#in python, ctrl-c (sigint) causes KeyboardInterrupt exception
#but pygame.event.wait() is stuck somewhere in sdl and doesnt know
#anything about that...

while 1:
	try:
		loop()
	except KeyboardInterrupt() as e:
		#hide and slowly die
		pygame.display.iconify()
		raise e
	except Exception() as e:
		pass
