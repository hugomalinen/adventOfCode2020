# Open file with input inside

f = open('./input.txt', 'r')
data = f.readlines()

# Convert the list of strings to a list of integers

for t in enumerate(data):
	data[t[0]] = int(data[t[0]].split("\n")[0])

# A function to go through the list of integers to
# find a pair that will sum to 2020, then return
# that integer pair's product.

def find2020mult(data):
	while len(data) != 0:
		n1 = data[0]
		data.pop(0)
		for n in data:
			if n1 + n == 2020:
				return(n * n1)

print(find2020mult(data))
