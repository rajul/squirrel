import collections

from BaseCache import BaseCache

class LRUCacheOrderedDict(BaseCache):
	def __init__(self, capacity):
		super(self.__class__, self).__init__(capacity)

		self.cache = collections.OrderedDict()

	def get(self, key):
		try:
			value = self.cache.pop(key)
			self.cache[key] = value
			return value
		except KeyError:
			return -1

	def set(self, key, value):
		try:
			self.cache.pop(key)
		except KeyError:
			if len(self.cache) >= self.capacity:
				self.cache.popitem(last=False)

		self.cache[key] = value
