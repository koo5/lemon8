

class Menu():
	def __init__:
		self.typed = "" # text typed into the edit box
		self.textbox = Textbox()

	def set_typed(typed):
		self.typed = typed
		self.menu = []
		populate()

	def populate(slot, typed):
		self.menu = filter(blocks_by_type(slot.type), name starts with <typed>)
		self.menu += filter(blocks_by_type(slot.type), <documentation search>)
		#for now, full dict
		self.menu += english
		


class EditMachine():
	def __init__:
		self.typed = "" #

		

	def key(event):


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


active points to the currently active/under cursor block/thing

#active should be some kind of slot or something where you can put things

when adding a word, check that active is either a sentence or 
create it (in the slot)

pile words in sentence

try compilation into a sentence block


