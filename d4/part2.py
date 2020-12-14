import re

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

	# Form a dictionary that has fields correspond to their values

	passDict = {}
	for t_ in enumerate(tempArr):
		split = tempArr[t_[0]].split(":")

		# Check if the length is 2 before inserting into dict
		# to avoid out of range index
		if len(split) == 2:
			passDict[split[0]] = split[1]

	# Insert dictionary into data

	data[t[0]] = passDict

# Dict with definitions for valid values for each field
# [min, max]
# regex
# arr of valids

requiredFields = {
				"byr":[1920,2002],
				"iyr":[2010,2020],
				"eyr":[2020,2030],
				"hgt":{
					"cm":[150,193],
					"in":[59,76]
					},
				"hcl":"^#[a-f0-9]{6}$",
				"pid":"^[0-9]{9}$",
				"ecl":[
					"amb",
					"blu",
					"grn",
					"brn",
					"gry",
					"hzl",
					"oth"
					]
				} 

# Function to check if a value is within boundaries defined in a array, tuple or list
# [min,max]

def checkBoundaries(val, minMaxArr):
	
	if minMaxArr[0] <= int(val) <= minMaxArr[1]:
		return True
	return False

# Function to check that the fields have valid values

def checkFields(dic):

	for f in requiredFields.keys():

		# Checking that the passport has all the required fields
		if f not in dic.keys():
			print("MISSING FIELDS: "+str(dic.keys()))
			return False

		# Printing each field's name and data
		print(f + " : " + str(dic[f]))

		# Checking the fields involving years
		# They are all limited by a range
		if f in ["byr","iyr","eyr"]:
			if not checkBoundaries(dic[f], requiredFields[f]):
				print("BAD YEARS     : " + f + " " + dic[f])
				return False

		# Checking for valid hcl and pid
		# The validity definitions for hcl and pid are regexes
		if f in ["hcl","pid"]:
			if re.search(requiredFields[f], dic[f]) == None:
				print("BAD HCL/PID   : " + dic[f] + " len: " + str(len(dic[f])) + " type: " + f)
				return False

		# Checking for valid eye colour
		# The validity definition is a list of all valid colours
		if f == "ecl":
			if dic[f] not in requiredFields[f]:
				print("BAD ECL       : " + dic[f])
				return False

		# Checking for valid height
		if f == "hgt":
			# Defining the span where the numeric value occurs in the string
			span = re.search("^[0-9]+", dic[f]).span()
			# Checking that at least one of the units is used
			if re.search("^[0-9]*cm$", dic[f]) == None and re.search("^[0-9]*in$", dic[f]) == None:
				print("BAD HEIGHT    : " + dic[f])
				return False

			# If the height is in cm, check with valid cm range
			if re.search("^[0-9]*cm$", dic[f]) != None:
				if not checkBoundaries(dic[f][span[0]:(span[1])], requiredFields[f]["cm"]):
					print("BAD HEIGHT    : " + dic[f])
					return False

			# If the height is in in, check with valid in range
			if re.search("^[0-9]*in$", dic[f]) != None:
				if not checkBoundaries(dic[f][span[0]:span[1]], requiredFields[f]["in"]):
					print("BAD HEIGHT    : " + dic[f])
					return False

	# Return true if there are no violations
	return True 

# Check each passport's validity
nOfValid = 0
for passport in data:
	print("\n")
	if checkFields(passport):
		print("Valid!")
		nOfValid += 1
	else: print("Not valid!")

print("\n" + str(nOfValid))
