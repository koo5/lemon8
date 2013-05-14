



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
