
class Shape():
	def __init__(self, a, p):
		self.area = a
		self.perimeter = p

	def get_area(self):
		return self.area

	def __str__(self):
		return "Area %d, perimeter %d" % (self.area, self.perimeter)


class Test:

	def __init__(self, s):
		self.shape = s

	def __str__(self):
		return "Test: " + str(self.shape)

	@classmethod
	def pi_approx(cls, shape):
		enhanced_shape = cls(shape)
		return str(enhanced_shape)


s = Shape(1, 2)
print Test.pi_approx(s)
