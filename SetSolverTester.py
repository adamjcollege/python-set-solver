import unittest
from SetSolver import ShapeAttrib, FillAttrib, ColorAttrib, NumberAttrib,  Card, Deck


class SetSolverTestMethods(unittest.TestCase):

	def test_xor_eq(self):
		x1 = ShapeAttrib('diamond')
		x2 = ShapeAttrib('diamond')
		self.assertEqual(x1, x2)
		x3 = ShapeAttrib(x1 ^ x2)
		self.assertEqual(x1, x3)
		self.assertEqual(str(x1), str(x3))


	def test_xor_ne(self):
		x = ShapeAttrib('diamond')
		y = ShapeAttrib('oval')
		z = ShapeAttrib('squiggle')
		self.assertEqual(str(z), str(y ^ x))
		self.assertEqual(str(y), str(x ^ z))
		self.assertEqual(str(x), str(y ^ z))

	def test_card_repr(self):
		card1 = Card.fromString('1 red hatched oval')
		self.assertEqual(str(card1), "Card(1 red hatched oval)")
		card2 = Card.fromString('2 red hatched oval')
		self.assertEqual(str(card2), "Card(2 red hatched ovals)")



	def test_card_gt(self):
		card1 = Card.fromString('1 red hatched oval')
		card2 = Card.fromString('2 red hatched oval') 
		self.assertGreater(card2, card1) # 2 > 1
		card2 = Card.fromString('1 green hatched oval') 
		self.assertGreater(card1, card2) # red > green (alphabetical)
		card2 = Card.fromString('1 red hollow oval') # hollow > hatched (alphabetical)
		self.assertGreater(card2, card1)

	def test_ftc(self):
		deck = Deck()
		card1 = Card.fromString('3 red hatched oval')
		card2 = Card.fromString('3 red filled oval')
		card3 = Card.fromString('3 red hollow oval')
		deck.addCard(card1)
		deck.addCard(card2)
		self.assertFalse(deck.findThirdCard(card1, card2))
		deck.addCard(card3)
		self.assertEqual(str(deck.findThirdCard(card1, card2)), "Card(3 red hollow ovals)")

	def test_card(self):
		card = Card.fromString("3 red hatched oval")
		self.assertEqual(str(card.numberAttrib), "3")
		self.assertEqual(str(card.colorAttrib), "red")
		self.assertEqual(str(card.fillAttrib), "hatched")
		self.assertEqual(str(card.shapeAttrib), "oval")

	def test_cardShapePluralize(self):
		card = Card.fromString("3 red hatched ovals")
		self.assertEqual(str(card.shapeAttrib), "oval")


	def test_init(self):
		with self.assertRaises(ValueError):
			card = Card.fromString("4 red hatched oval")
		with self.assertRaises(ValueError):
			card = Card.fromString("3 yellow hatched oval")
		with self.assertRaises(ValueError):
			card = Card.fromString("3 purple empty oval")
		with self.assertRaises(ValueError):
			card = Card.fromString("3 purple hollow square")


if __name__ == '__main__':
	unittest.main()
