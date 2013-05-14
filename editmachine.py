

#editmachine


typed = "a"


menu(slot, typed):
	menu = filter(blocks_by_type(slot.type), name starts with <typed>)
	menu += filter(blocks_by_type(slot.type), <documentation search>)
	#for now, full dict
	menu += english



active points to the currently active/under cursor block/thing

#active should be some kind of slot or something where you can put things

when adding a word, check that active is either a sentence or 
create it (in the slot)

pile words in sentence

try compilation
