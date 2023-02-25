

class Yogurt:
	
	def __init__(self):
		self.additive = ''
		
	def add(self):
		self.additive = input()

		
	def show_my_eat(self):
		if self.additive == '':
			return 'Безвкусный йогурт'
		return f'«Йогурт с {self.additive}'





yog = Yogurt()
yog.add()
print(yog.show_my_eat())