# Class demonstrating operator overloading for all arithmetic and relational operators
class Number:
	def __init__(self, value):
		self.value = value

	# Arithmetic operators
	def __add__(self, other):
		return Number(self.value + other.value)
	def __sub__(self, other):
		return Number(self.value - other.value)
	def __mul__(self, other):
		return Number(self.value * other.value)
	def __truediv__(self, other):
		return Number(self.value / other.value)
	def __floordiv__(self, other):
		return Number(self.value // other.value)
	def __mod__(self, other):
		return Number(self.value % other.value)
	def __pow__(self, other):
		return Number(self.value ** other.value)

	def __str__(self):
		return str(self.value)

# Test the Number class
a = Number(10)
b = Number(3)
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

