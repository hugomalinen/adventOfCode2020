# Open file with input inside and form it into a list

f = open('./input.txt', 'r')
data = f.read().split("\n\n")

# Remove \n from each string

for t in enumerate(data):
	data[t[0]] = data[t[0]].split("\n")
	tempArr = []

	# Divide remaining long strings into shorter ones

	for s in data[t[0]]:
		for subS in s.split(' '):
			tempArr.append(subS)

	# Divide the fields into the title and the data
	
	for t_ in enumerate(tempArr):
		tempArr[t_[0]] = tempArr[t_[0]].split(":")[0]

	data[t[0]] = tempArr

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] 

def checkFields(arr):

	for f in requiredFields:
		if f not in arr:
			return False
	return True 

nOfValid = 0
for passport in data:
	if checkFields(passport):
		nOfValid += 1

print(nOfValid)
