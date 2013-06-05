#-*- coding: utf-8 -*-




class Textbox():

	def __init__():
		pass
		
	def moveright():
		self.cursorx += 1

	def moveleft():
		if self.cursorx > 0: self.cursorx -= 1

	def key(k):
		if event.key==pygame.K_BACKSPACE:
			if cursorx > 0:
				self.text = self.text[0:cursorx-1]+self.text[cursorx:]
				cursorx -=1
		elif event.key==pygame.K_DELETE:
			if self.cursorx >= 0 and self.cursorx < len(self.text):
				self.text=self.text[0:self.cursorx]+self.text[self.cursorx+1:]
		elif event.unicode:
			self.text[0:self.cursorx]+event.unicode+self.text[cursorx:]
			cursorx +=1

	def draw():
		#rectangle around
		pygame.draw.rect(pygame.display.get_surface(),
			(0,200,0), (self.x,self.y,len(self.text)*font.fontw, font.fonth), 1)

		#text
		pygame.display.get_surface().blit(font.render(textbox.text,True,color),(textbox.x, textbox.y))
	
		#cursor
		startpos = (textbox.x+(textbox.cursorx*fontw), textbox.y)
		endpos   = (textbox.x+(textbox.cursorx*fontw), textbox.y+font.get_height())
		pygame.draw.line(screen_surface, (0, 255, 0), startpos, endpos, 3)


