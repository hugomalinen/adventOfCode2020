f = open('/home/hugo/Lukio/IBY1/CAS/adventOfCode/d1/input.txt', 'r')
data = f.readlines()

for t in enumerate(data):
	data[t[0]] = int(data[t[0]].split("\n")[0])

def find2020mult(data):
	while len(data) != 0:
		n1 = data[0]
		data.pop(0)
		for n in data:
			if n1 + n == 2020:
				return(n * n1)

print(find2020mult(data))
