# Open file with input inside

f = open('./input.txt', 'r')
data = f.readlines()

# Remove \n from each string

for t in enumerate(data):
    data[t[0]] = data[t[0]].split("\n")[0]

# Loop to find the n of the required char in the passwords

nCompliant = 0
for s in data:
	
	# info = (([min]-[max]), ([char]:), ([password]))
	info = s.split(' ')
	minmax = info[0].split('-')
	
	nLetter = 0
	
	# This inner loop finds the n of the char being inspected
	for c in info[2]:
		if c == info[1][0]:
			nLetter += 1

	# Checking that the n of the inspected char is within the
	# criteria boundaries
	if (int(minmax[0]) <= nLetter) and (nLetter <= int(minmax[1])):
		nCompliant += 1	

print(nCompliant)
