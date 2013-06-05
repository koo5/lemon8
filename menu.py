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
		
	
