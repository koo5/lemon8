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



#menu
	letters = getletters()
	#wordy * fonth is the y position of the current word
	counter = 0
	for i in menu:
		if counter == menu_sel:
			color = (255,0,0)
		else:
			color = (200,0,0)
		to_blit=font.render(i[0],True,color)
		y = (wordy*lines_for_each_line+counter+1) * fonth
		x = left_margin + letters * fontw
		screen_surface.blit(to_blit,(x, y))
		counter += 1





	pygame.display.update()








#key input


def control(event):
	global menu_sel,cursorx,code, wordx,wordy


	# up & down
	if event.key == pygame.K_DOWN:
		movedown()
	elif event.key == pygame.K_UP:
		moveup()

	# pg up & down
	elif event.key == pygame.K_PAGEDOWN:
		menu_sel +=1
	elif event.key == pygame.K_PAGEUP:
		menu_sel -=1

	# left & right
	elif event.key == pygame.K_LEFT:
		moveleft()
	elif event.key == pygame.K_RIGHT:
		moveright()




	elif event.key == pygame.K_HOME:
		cursorx = 0
		wordx = 0
	elif event.key == pygame.K_END:
		wordx = -1+len(code[wordy])
		cursorx = len(get_text())



	elif event.key == pygame.K_F8:
	        del code[wordy]



	elif event.scancode == 151 or event.key == pygame.K_F12:
	        #exit
#		save()
		bye()
	elif event.key == pygame.K_F10:
 		bye()

#	print "scancode ", event.scancode
	
	elif event.unicode == ' ':
		confirm_choice()
		wordright()

	elif event.key == pygame.K_RETURN:
		if pygame.key.get_mods() & pygame.KMOD_RCTRL:
			parse()
		else:
			confirm_choice()
			wordy+=1
			wordx=0
			cursorx=0
			code.insert(wordy, [])
			snap_to_line()
			stretch_line()

	else: return False		

	update_menu()
	return True


def edit(event):
	global cursorx
	if event.key==pygame.K_BACKSPACE:
		print "backspace"
		if cursorx > 0:
			if cursorx <= len(get_text()):
				newtext = get_text()[0:cursorx-1]+get_text()[cursorx:]
				#print get_text(), "->", newtext
				set_text(newtext)
				cursorx -=1
		else:
			if wordx > 0:
				#print ">0"
				#print code[wordy][wordx-1]
				if code[wordy][wordx][0]=="":
					#print "del"
					del code[wordy][wordx]
					moveleft()
			else:
				if wordy > 0:
					if code[wordy-1][len(code[wordy-1]-1)]:

	elif event.key==pygame.K_DELETE:
		if cursorx >= 0 and cursorx < len(get_text()):
			set_text(get_text()[0:cursorx]+get_text()[cursorx+1:])
	elif event.unicode:
		set_text(get_text()[0:cursorx]+event.unicode+get_text()[cursorx:])
		cursorx +=1
	else:
		return

	update_dictionary()
	update_menu()
	update_menu_sel()



def mouse_me_baby(event):
	global menu_sel
	print event
	if event.button == 4: #up
		menu_sel -= 1
	if event.button == 5: #down
		menu_sel += 1





def process_event(event):
	if event.type == pygame.QUIT:
		bye()
	if event.type == pygame.KEYDOWN:
		control(event) or edit(event)
	if event.type == pygame.MOUSEBUTTONDOWN:
		mouse_me_baby(event)








#margin between displayed text and left edge of the window
left_margin = 10
screen_height = 480







def init_window():
	pygame.init()
	pygame.display.set_caption("secret-banana")
	#sdl, which pygame is based on, has its own keyboard delay and repeat rate
	pygame.key.set_repeat(300,30)
	#this creates a window
	return pygame.display.set_mode((640,screen_height))

screen_surface = init_window()





def init_font():
	#the final version is planned to use comic sans ✈
	font = pygame.font.SysFont('monospace', 16)
	f= font.render(" ",False,(0,0,0)).get_rect()
	fonth = f.height
	fontw = f.width
	return font, fontw, fonth

(font, fontw, fonth) = init_font()








try:
	code = simplejson.loads(open("code.json", "r").read())
except:
	code = [[[3,"number"],["+", "plus"],[3, "number"]]]




#cursor position in the current word
cursorx = 0
#the current word on line
wordx = 0
#line
wordy = 0





#the red menu
menu = []
#selected item. -1 for none
menu_sel = 0





def loop():
	process_event(pygame.event.wait())
	draw()








update_menu()






pygame.time.set_timer(pygame.USEREVENT, 40)#SIGINT timer





def bye():
	open("code.json", "w").write(simplejson.dumps(code))
	exit()





while 1:
	try:
		loop()
	except KeyboardInterrupt() as e:
		pygame.display.iconify()
		raise e
	except Exception() as e:
		pass













"""
#todo:
if key.unicode == '\':
	cursor left
	add newline
	cursor up

"""			
