# Open file with input inside

f = open('./input.txt', 'r')
data = f.readlines()

# Remove \n from each string
for t in enumerate(data):
    data[t[0]] = data[t[0]].split("\n")[0]


# Function to convert from binary to integer
# Obsolete as python has built in capabilities to do this

#def binToInt(bin_):
#	int_ = 0
#	for t in enumerate(bin_):
#		if t[1] == '1':
#			int_ += pow(2, len(bin_)-(t[0]+1))
#
#	return int_


# Function to convert seat code to a binary number

def codeToBin(s):
	# The binary will be saved to this string
	bin_ = ""
	
	# Look through each character in the code
	for c in s:
		# F and L correspond to 0
		if c in ["F","L"]:
			bin_ += "0"
		# B and R correspond to 1
		elif c in ["B","R"]:
			bin_ += "1"

	return(bin_)


# Function to convert a seat code to into a seat ID

def codeToID(code):

	# The row is the base 10 form of the first 7 chars of the seat code in bin
	row    = int(codeToBin(code[0:7]),2)
	# The column is the base 10 form of the last 3 chars of the seat code in bin
	column = int(codeToBin(code[7:]), 2)

	return 8*row+column

# Set 0 as the highest known by default
highest = 0
lowest = codeToID("BBBBBBBRRR")


seatIDs = []
# Look through every code and compare its ID to the highest known ID
for code in data:
	ID = codeToID(code)

	# Save the current ID to be the highest or lowest known if it is highest or lowest so far
	if ID > highest:
		highest = ID
	elif ID < lowest:
		lowest = ID

	# Form a list of all IDs
	seatIDs.append(ID)

# Look through each ID in the known range and determine the missing ID
for n in range(lowest, highest):
	if n not in seatIDs:
		print(n)
