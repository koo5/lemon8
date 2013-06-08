#!/usr/bin/python
#-*- coding: utf-8 -*-


import pygame


pygame.init()
pygame.display.set_caption("lemon-9")#window title
#sdl, which pygame is based on, has its own keyboard delay and repeat rate
pygame.key.set_repeat(300,30)
#this creates a window
pygame.display.set_mode((640,480))


#the final version is planned to use comic sans ✈
font = pygame.font.SysFont('monospace', 16)
font.width = font.render(" ",False,(0,0,0)).get_rect().width


#enum
tab = 0

class colors():
	keyword = (200,255,200)

class node():
	def draw(x,y):
		for line in lines:
			for item in line:
				if type(item) == text:
					draw_text(item, (x, y), colors.keyword)
					x=x+len(text)
				else if item == tab:
					x = x + 4
				else if isinstance(item, node):
					x,y= item.draw(x, y)
			y = y + 1
		return (x,y)
			
	def draw_text(text, (x, y), color):
		pygame.display.get_surface().blit(font.render(text,True,color),chars_to_pixels(x,y))
	
	def chars_to_pixels(x, y):
		return (x*font.width, y*font.height)




class if_node():
	node_name = "if"
	node_doc = "conditional evaluation"
	def get_draw_data():
		return [["if", self.expression],
				[tab, self.then

	def __init__():
		
	def run():
		if run(self.expression):
			return run(self.then)
		else:
			if exists(parent) and exists(self.else_):
				return run(self.else_)
			else:
				return None


code = if_node()
code.then = 

class function_declaration_node():
	node_name = "function declaration"

	def __init__():
		
	def draw():
		dprint [["to", self.
		   






def process_event(event):
	if event.type == pygame.QUIT:
		bye()
	if event.type == pygame.KEYDOWN:
		editor.key(event)


def draw():
	screen_surface.fill((0,0,0))
	code.draw()
	#status bar and clock:P
	pygame.display.update()



def loop():
	process_event(pygame.event.wait())
	draw()


def bye():
	#save()
	exit()


#in python, ctrl-c (sigint) causes KeyboardInterrupt exception
#but pygame.event.wait() is stuck somewhere in sdl and doesnt know
#anything about that...
pygame.time.set_timer(pygame.USEREVENT, 40)

while 1:
	try:
		loop()
	except KeyboardInterrupt() as e:
		#hide and slowly die
		pygame.display.iconify()
		raise e
	except Exception() as e:
		pass
