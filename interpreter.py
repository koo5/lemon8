# -*- coding: utf-8 -*-
import yaml



class Interpreter:
	def __init__(self, blocks):
		self.blocks = blocks

	def blocks_by_type(self, type):
		return filter(blocks, lambda x: return (x.type == type))
	
	def function_definitions(self):
		return blocks_by_type("function definition")
		
	def function_definition(self, name):
		return filter(function_definitions(), lambda x: x.slot("name") == name)[0]

	def run(self):
		run_block(self.blocks[0])

	def run_block(self,x):
		print ">", x
		if x.type == "function call":
			run_block(function_definition(x.slot("name")), "code").value)
			
		elif x.type == "if":
			if run_block("condition")["value"]:
				run_block("then")["value"]
			else:
				run_block("else")["value"]
				


def run():
    Interpreter(yaml.load(open("code.yaml", "r").read())).run()
