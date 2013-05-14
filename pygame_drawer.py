
#global:font

def draw_textbox(textbox, color):
	#rectangle around
	pygame.draw.rect(pygame.display.get_surface(),
		(0,200,0), (self.x,self.y,len(self.text)*font.fontw, font.fonth), 1)

	#text
	pygame.display.get_surface().blit(font.render(textbox.text,True,color),(textbox.x, textbox.y))
	
	#cursor
	startpos = (textbox.x+(textbox.cursorx*fontw), textbox.y)
	endpos   = (textbox.x+(textbox.cursorx*fontw), textbox.y+font.get_height())
	pygame.draw.line(screen_surface, (0, 255, 0), startpos, endpos, 3)

	
def draw_
