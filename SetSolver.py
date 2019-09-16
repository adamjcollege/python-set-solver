import sys, argparse
from itertools import combinations

customFillValues = False

class Attrib:
	def __init__(self, newVal):
		try:
			self.value = self.attribVals.index(newVal)
		except ValueError:
			print("{0} is not a valid attribute".format(newVal))
			raise

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

	def getProperty(self):
		return self.attribVals[self.value]
	
	def __str__(self):
		return str(self.getProperty())

	def __eq__(self, other):
		return self.getProperty() == other.getProperty()
	
	def __ne__(self, other):
		return self.getProperty() != other.getProperty()

	def __gt__(self, other):
		return self.getProperty() > other.getProperty()

class ShapeAttrib(Attrib):
	def __init__(self, newVal):
		self.attribVals = ['diamond', 'oval', 'squiggle']
		#for shapes, can pluralize
		Attrib.__init__(self, newVal.rstrip('s'))
	

class ColorAttrib(Attrib):
	def __init__(self, newVal):
		self.attribVals = ['red', 'green', 'purple']
		Attrib.__init__(self, newVal)

class FillAttrib(Attrib):
	def __init__(self, newVal):
		if(customFillValues):
			self.attribVals = customFillValues
		else: 
			self.attribVals = ['hollow', 'hatched', 'filled']
		Attrib.__init__(self, newVal)

class NumberAttrib(Attrib):
	def __init__(self, newVal):
		self.attribVals = ['1', '2', '3']
		Attrib.__init__(self, newVal)

class Card:
	def __init__(self, listArgs):
		self.numberAttrib = NumberAttrib(listArgs[0])
		self.colorAttrib = ColorAttrib(listArgs[1])
		self.fillAttrib = FillAttrib(listArgs[2])
		self.shapeAttrib = ShapeAttrib(listArgs[3])

	@classmethod
	def fromString(cls, inputString):
		return cls(inputString.split(' '))

	def __repr__(self):
		return "Card({0} {1} {2} {3})".format(self.numberAttrib, self.colorAttrib, self.fillAttrib, (self.shapeAttrib if int(str(self.numberAttrib)) == 1 else str(self.shapeAttrib) + "s"))

	
	def __eq__(self, other):
		return (self.numberAttrib == other.numberAttrib) &  \
			(self.colorAttrib == other.colorAttrib) & \
			(self.fillAttrib == other.fillAttrib) &  \
			(self.shapeAttrib == other.shapeAttrib)

	def __gt__(self, other):
		if(self.numberAttrib > other.numberAttrib):
			return True 
		if(self.colorAttrib > other.colorAttrib):
			return True
		if(self.fillAttrib > other.fillAttrib):
			return True
		if(self.shapeAttrib > other.shapeAttrib):
			return True
		return False


class Deck:
	cards = []
	def addCard(self, cardArg):
		self.cards.append(cardArg)
		

	def __str__(self):
		return str(self.cards)

	def findSet(self):
		foundSets = []
		twoCardCombinationSets = combinations(self.cards, 2)
		for twoCardCombination in twoCardCombinationSets:
			thirdCard = self.findThirdCard(twoCardCombination[0], twoCardCombination[1])
			if (thirdCard):
				foundSet = sorted([str(twoCardCombination[0]), str(twoCardCombination[1]), str(thirdCard)])
				if foundSet not in foundSets:
					foundSets.append(foundSet)

		for set in foundSets:
			print(set)

	def findThirdCard(self, firstCard, secondCard):
		number = firstCard.numberAttrib ^ secondCard.numberAttrib
		color = firstCard.colorAttrib ^ secondCard.colorAttrib
		fill = firstCard.fillAttrib ^ secondCard.fillAttrib
		shape = firstCard.shapeAttrib ^ secondCard.shapeAttrib
		testCard = Card([number, color, fill, shape])
		for card in self.cards:
			if card == testCard:
				return card
		return False

def load_cards_from_file(f, fill):
	if(fill):
		global customFillValues
		customFillValues = f.readline().split()
	f1 = f.readlines()
	deck = Deck()
	for line in f1:
		card = Card.fromString(line.strip())
		deck.addCard(card)
	return deck

def main():
	parser = argparse.ArgumentParser(description='A Solver for the Game Set.')
	parser.add_argument('--fill', action='store_true', help='Optional: Line 1 of input file uses custom descriptors for fill, such as empty, shaded, and solid')
	parser.add_argument('file', type=argparse.FileType('r'))
	args = parser.parse_args()
	deck = load_cards_from_file(args.file, args.fill)
	deck.findSet()

if __name__ == '__main__':
	main()


