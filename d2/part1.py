# Open file with input inside

f = open('./input.txt', 'r')
data = f.readlines()

# Remove \n from each string

for t in enumerate(data):
    data[t[0]] = data[t[0]].split("\n")[0]

nCompliant = 0
for s in data:
	
	info = s.split(' ')
	minmax = info[0].split('-')
	print(info)
	print(minmax)
	print(info[1][0])
	
	nLetter = 0
	for c in info[2]:
		if c == info[1][0]:
			nLetter += 1
	print(nLetter)	
	if (int(minmax[0]) <= nLetter) and (nLetter <= int(minmax[1])):
		nCompliant += 1	
		print("Compliant!")
print(nCompliant)
