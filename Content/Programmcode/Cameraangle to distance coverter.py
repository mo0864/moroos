import math

numbers = [
  {'number': '1', 'originY': 148.4},
  {'number': '2', 'originY': 198},
  {'number': '3', 'originY': 60},
  {'number': '4', 'originY': 123}
]



height = 3

print(math.tan(50))


for obj in numbers:
  obj.update({'distance': height * math.tan(((obj.get('originY') * (40 / 212)) + 39) / 180 * math.pi)})
  print(obj.get('originY'), obj.get('distance'))
  print(obj)

def myFunc(i):
	return i['distance']

numbers.sort(key=myFunc)

for i in numbers:
  print(obj)

#	numbers.append('distance': height * math.tan(39+(i.get('originY') / 40)))