import os
import random
from collections import defaultdict
from pprint import pprint

class SimulatorBase(object):
	def __init__(self, fodder_directory = None):
		self.cache = defaultdict(list)

		if fodder_directory:
			[self.load_fodder(fodder_directory + f) for f in os.listdir(fodder_directory) if f.endswith('.txt')]
			
	def load_fodder(self, path):
		words   = self._filter(open(path).read().split())
		for i in range(len(words) - 2):
			k1, k2, v = words[i], words[i+1], words[i+2]
			self.cache[(k1, k2)].append(v)

	def _filter(self, words):
		return [w for w in words if not w.isupper()]

	def _format(self, text):
		sentences = ' '.join(text).split('.')
		return '. '.join([s.strip().capitalize() for s in sentences])

	def _generate_seed(self):
		return random.choice(list(self.cache.keys()))

	def generate_text(self, minimum = 30):
		w1, w2 = self._generate_seed()
		text = []
		while(True):
			text.append(w1)
			if len(text) > minimum and w1.strip().endswith('.'):
				break
			w1, w2 = w2, random.choice(self.cache.get((w1, w2)))
		return self._format(text)
