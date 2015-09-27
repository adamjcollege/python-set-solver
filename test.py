from set2 import ShapeAttrib, FillAttrib, ColorAttrib, NumberAttrib,  Card, Deck


deck = Deck()
deck.addCard('3 red hatched oval')
deck.addCard('3 red filled oval')
deck.addCard('1 green hatched oval')
deck.addCard('2 red hatched diamond')
deck.addCard('3 green filled diamond')
deck.addCard('1 green filled oval')
deck.addCard('3 purple hollow squiggle')
deck.addCard('3 green hollow oval')
deck.addCard('2 green hatched diamond')
deck.addCard('1 purple filled squiggle')
deck.addCard('1 green hollow diamond')
deck.addCard('2 green hollow squiggle')
deck.findSet()

def printTest(x, y, z):
	print x, " ^ ", y, ": ", x ^ y
	print y, " ^ ", x, ": ", y ^ x
	print x, " ^ ", z, ": ", x ^ z
	print z, " ^ ", x, ": ", z ^ x
	print y, " ^ ", z, ": ", y ^ z
	print z, " ^ ", y, ": ", z ^ y


def test():
	x = ShapeAttrib('diamond')
	y = ShapeAttrib('oval')
	z = ShapeAttrib('squiggle')

	printTest(x, y, z)

	x = FillAttrib('hollow')
	y = FillAttrib('hatched')
	z = FillAttrib('filled')

	printTest(x, y, z)

	x = ColorAttrib('red')
	y = ColorAttrib('green')
	z = ColorAttrib('purple')

	printTest(x, y, z)

	x = NumberAttrib('1')
	y = NumberAttrib('2')
	z = NumberAttrib('3')

	printTest(x, y, z)
