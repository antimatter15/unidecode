Cache = {}

from collections import defaultdict
Reverse = defaultdict(list)

for section in range(0, 500):
	try:
		mod = __import__('x%03x'%(section), [], [], ['data'])
		Cache[section] = mod.data
		for position in range(0, 256):
			num = (section << 8) | position
			# section = codepoint >> 8
			# position = codepoint % 256
			if Cache[section] and len(Cache[section]) > position:
				letter = Cache[section][position]
				if len(letter) == 1 or letter in ['ae']:
					Reverse[letter].append(num)
					# print num, Cache[section][position]


	except ImportError:
		Cache[section] = None


print Reverse