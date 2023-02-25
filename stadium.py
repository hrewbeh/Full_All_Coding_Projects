

class Stadium:

	def __init__(self):
		self.stadium_name = []
		self.opening = []
		self.country = []
		self.city = []
		self.capacity = []
		
	def std_name(self,name):
		self.stadium_name.append(name)
		
	def open(self,open):
		self.opening.append(open)
		
	def countr(self,cou):
		self.country.append(cou)
		
	def cit(self,cit):
		self.city.append(cit)
	
	def cap(self,cap):
		self.capacity.append(cap)
		
	def conclusion(self):
		return f'{self.stadium_name} открылся в {self.opening} году в {self.country}, a именно в {self.city}. Вместимость стадиона {self.capacity}'
	
sta = Stadium()
sta.std_name('qew')
sta.open('123')
sta.countr('dfdr')
sta.cit('ass')
sta.cap('12345')



print(sta.conclusion())