import numbers

class Triangle:
	def __init__(self, s1, s2, s3):
		self.a = s1
		self.b = s2
		self.c = s3
		
	def classify_triangle(self):
		if isinstance(self.a, numbers.Number) and isinstance(self.b, numbers.Number) and isinstance(self.c, numbers.Number):
			if self.a == self.b == self.c :
				return "equilateral"
			if self.a == self.b or self.a == self.c or self.b == self.c:
				if self.isRight():
					return "isoscelese and right"
				return "isoscelese"
			if self.a != self.b != self.c:
				if self.isRight():
					return "scalene and right"
				return "scalene"
			return "none, probaly an error"
		else: 
			return False

	def isRight(self):
		a, b, c = sorted([self.a, self.b, self.c])

		return a*a + b*b == round(c*c)