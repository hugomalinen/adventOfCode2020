# Open file with input inside

f = open('./input.txt', 'r')
data = f.readlines()

# Convert the list of strings to a list of integers

for t in enumerate(data):
	data[t[0]] = int(data[t[0]].split("\n")[0])

# A function to go through the list of integers to
# find a triplet that will sum to 2020, then return
# that integer triplet's product.

def find2020mult(data):
	i = 0
	while i < len(data) - 1:
		n1 = data[i]
		i2 = 0
		i += 1
		while i2 < len(data[i+1:]):
			n2 = (data[i+1:])[i2]
			i3 = 0
			i2 += 1
			while i3 < len(data[i2+1:]):
				n3 = (data[i2+1:])[i3]
				if n1 + n2 + n3 == 2020:
					print("%d, %d, %d"%(n1,n2,n3))
					print(n1+n2+n3)
					return(n1 * n2 * n3)
				i3 += 1

print(find2020mult(data))
