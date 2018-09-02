import unittest
from triangle import Triangle

class TriangleTest(unittest.TestCase):
	def test_init(self):
		""" Sides stored properly in __init__() """
		t = Triangle(3,4,5)
		self.assertEqual(t.a,3)
		self.assertEqual(t.b,4)
		self.assertEqual(t.c,5)
	def test_right_triangle(self):
		""" test right triangle detection """
		t = Triangle(3,4,5)
		self.assertTrue(t.isRight())
		self.assertTrue(Triangle(5,4,3).isRight())
		self.assertFalse(Triangle(3,3,3).isRight())
		self.assertTrue(Triangle(4, 4, 5.6568542495).isRight())
	def test_isoceles(self):
		""" test isoceles with and without right angle"""
		t = Triangle(3,3,5)
		t2 = Triangle(4, 4, 5.6568542495)
		self.assertEquals(t.classify_triangle(),"isoscelese")
		self.assertEquals(t2.classify_triangle(),"isoscelese and right")
		self.assertFalse(Triangle(3,3,3).classify_triangle() == "isoscelese")
	def test_equalateral(self):
		"""test equilateral """
		t = Triangle(3,3,3)
		self.assertEquals(t.classify_triangle(),"equilateral")
	def test_scalene(self):
		"""test scalene"""
		t = Triangle(3,4,5)
		t2 = Triangle(7,54,2)
		self.assertEquals(t.classify_triangle(),"scalene and right")
		self.assertEquals(t2.classify_triangle(),"scalene")
	def test_triangle(self):
		""" test the length of a side of a triangle is less than the sum of the lengths of the other two sides and greater than the difference of the lengths of the other two sides."""
		self.assertFalse(Triangle("test", 3, 4).classify_triangle())
		self.assertEquals(Triangle(3,4,10).classify_triangle, "not a triangle")
if __name__ == '__main__':
	unittest.main(exit=False, verbosity=2)