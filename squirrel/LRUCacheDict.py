from squirrel.BaseCache import BaseCache

class LRUCacheDict(BaseCache):
	def __init__(self, capacity=100):
		super(self.__class__, self).__init__(capacity)

		self.cache = {}
		self.lru = {}
		self.access_time = 0

	def get(self, key):
		if key in self.cache:
			self.lru[key] = self.access_time
			self.access_time = self.access_time + 1
			return self.cache[key]

		return -1

	def set(self, key, value):
		if len(self.cache) >= self.capacity:
			lru_key = min(self.lru.keys(), key=lambda k: self.lru[k])
			self.cache.pop(lru_key)
			self.lru.pop(lru_key)

		self.cache[key] = value
		self.lru[key] = self.access_time
		self.access_time = self.access_time + 1
