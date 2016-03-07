class BaseCache(object):
	def __init__(self, capacity=100):
		self.capacity = capacity
		self.cache = None

	def get(self, key):
		pass

	def set(self, key, value):
		pass
