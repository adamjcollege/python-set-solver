import unittest
from set2 import ShapeAttrib, FillAttrib, ColorAttrib, NumberAttrib,  Card, Deck


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
		card1 = Card('1 red hatched oval')
		self.assertEqual(str(card1), "Card(1 red hatched oval)")
		card2 = Card('2 red hatched oval')
		self.assertEqual(str(card2), "Card(2 red hatched ovals)")

	def test_ftc(self):
		card1 = Card('3 red hatched oval')
		card2 = Card('3 red filled oval')
		self.assertEqual(str(card1.findThirdCard(card2)), "Card(3 red hollow ovals)")

	def test_card(self):
		card = Card("3 red hatched oval")
		self.assertEqual(str(card.numberAttrib), "3")
		self.assertEqual(str(card.colorAttrib), "red")
		self.assertEqual(str(card.fillAttrib), "hatched")
		self.assertEqual(str(card.shapeAttrib), "oval")

	def test_init(self):
		with self.assertRaises(ValueError):
			card = Card("4 red hatched oval")
		with self.assertRaises(ValueError):
			card = Card("3 yellow hatched oval")
		with self.assertRaises(ValueError):
			card = Card("3 purple empty oval")
		with self.assertRaises(ValueError):
			card = Card("3 purple hollow square") #should fail


if __name__ == '__main__':
	unittest.main()
