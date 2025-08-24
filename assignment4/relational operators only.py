class Number:
	def __init__(self, value):
		self.value = value  
		
         # Relational operators
	def __eq__(self, other):
		return self.value == other.value
	def __ne__(self, other):
		return self.value != other.value
	def __lt__(self, other):
		return self.value < other.value
	def __le__(self, other):
		return self.value <= other.value
	def __gt__(self, other):
		return self.value > other.value
	def __ge__(self, other):
		return self.value >= other.value
	def __str__(self):
		return str(self.value)

# Test the Number class
a = Number(10)
b = Number(3)
	
print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a <= b:", a <= b)
print("a > b:", a > b)
print("a >= b:", a >= b)