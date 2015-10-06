class Attrib:
	value = 0
	attribVals = []
	def __init__(self, newVal):
		self.value = self.attribVals.index(newVal)

	def __xor__(self, other):
		# (0 + 0)= 000 << 1 = 0 % 3 = 0
		# (1 + 2)= 011 << 1 = 6 % 3 = 0
		#
		# (0 + 2)= 010 << 1 = 4 % 3 = 1
		# (1 + 1)= 010 << 1 = 4 % 3 = 1
		#
		# (0 + 1)= 001 << 1 = 2 % 3 = 2
		# (2 + 2)= 100 << 1 = 8 % 3 = 2
		# In other words, a convenient property where the output is 'the same' as both parameters if both parameters are equal, 
		# or the third 'different' output if both parameters are not equal
		return self.attribVals[((self.value + other.value) << 1) % 3]

	def property(self):
		return self.attribVals[self.value]
	
	def __str__(self):
		return self.property()

	def __eq__(self, other):
		return self.property() == other.property()
	
	def __ne__(self, other):
		return self.property() != other.property()

class ShapeAttrib(Attrib):
	def __init__(self, newVal):
		self.attribVals = ['diamond', 'oval', 'squiggle']
		Attrib.__init__(self, newVal)
	

class ColorAttrib(Attrib):
	def __init__(self, newVal):
		self.attribVals = ['red', 'green', 'purple']
		Attrib.__init__(self, newVal)

class FillAttrib(Attrib):
	def __init__(self, newVal):
		self.attribVals = ['hollow', 'hatched', 'filled']
		Attrib.__init__(self, newVal)

class NumberAttrib(Attrib):
	def __init__(self, newVal):
		self.attribVals = ['1', '2', '3']
		Attrib.__init__(self, newVal)

class Card:
	def __init__(self, args):
		listArgs = args.split(' ')
		self.numberAttrib = NumberAttrib(listArgs[0])
		self.colorAttrib = ColorAttrib(listArgs[1])
		self.fillAttrib = FillAttrib(listArgs[2])
		self.shapeAttrib = ShapeAttrib(listArgs[3])

	def __repr__(self):
		return "Card('%s', '%s, '%s', '%s')" % (str(self.numberAttrib), str(self.colorAttrib), str(self.fillAttrib), str(self.shapeAttrib))

	def findThirdCard(self, comparison):
		number = self.numberAttrib ^ comparison.numberAttrib
		color = self.colorAttrib ^ comparison.colorAttrib
		fill = self.fillAttrib ^ comparison.fillAttrib
		shape = self.shapeAttrib ^ comparison.shapeAttrib
		return Card(str(number) + ' ' + str(color) + ' ' + str(fill) + ' ' + str(shape))
	
	def __eq__(self, other):
		return (self.numberAttrib == other.numberAttrib) &  \
			(self.colorAttrib == other.colorAttrib) & \
			(self.fillAttrib == other.fillAttrib) &  \
			(self.shapeAttrib == other.shapeAttrib)

class Deck:
	cards = []
	def addCard(self, args):
		self.cards.append(Card(args))

	def __str__(self):
		return self.cards

	def findSet(self):
		foundSets = []
		reviewed = []
		for index, card in enumerate(self.cards[:-1]):
			for comparison in self.cards[index+1:]:
				thirdCard = card.findThirdCard(comparison)
				if (thirdCard in self.cards):
					foundSet = sorted([card, comparison, self.cards[self.cards.index(thirdCard)]])
					if foundSet not in foundSets:
						foundSets.append(foundSet)
		for set in foundSets:
			print set
