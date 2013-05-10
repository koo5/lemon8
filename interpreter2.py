# -*- coding: utf-8 -*-
import yaml



class Block:
	def __init__(self, entries): 
		self.__dict__.update(entries)
		self.

	def __repr__(self):
		return 'Block:{%s}' % str(', '.join('%s : %s' % (k, repr(v)) for (k, v) in self.__dict__.iteritems()))

	def slot(name):
		s = filter(self.slots, lambda x: return x.name == name)
		if len(s) != 1:
			print 'len(s) = ',len(s)
		else return s[0]


class Interpreter:
	def __init__(self, blocks):
		self.blocks = blocks
		env=dict()

	def slot_by_name(self, slots, name):
		return filter(slots, lambda x: return x.name == name)[0]

	def blocks_by_type(self, type):
		return filter(blocks, lambda x: return (x.type == type))
	
	def function_definitions(self):
		return blocks_by_type("function definition")
		
	def function_definition_by_name(self, name):
		return filter(function_definitions(), lambda x: slot_by_name(x, "name") == name)[0]

	def run(self):
		run_block(self.blocks[0])

	def run_block(self,x):
		print ">", x
		if x.type == "function call":
			run_block(slot_by_name(function_definition_by_name(.slots, "code").value)
			
		elif x.type == "if"
		

def run():
    Interpreter(yaml.load(open("code.yaml", "r").read())).run()
