# Open file with input inside

f = open('./input.txt', 'r')
data = f.readlines()

# Remove \n from each string
for t in enumerate(data):
    data[t[0]] = data[t[0]].split("\n")[0]


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


seatIDs = []

# Look through every code and compare its ID to the highest known ID
for code in data:
	i = 0

	for ID in seatIDs:
		if codeToID(code) < ID or len(seatIDs) == i:
			seatIDs.insert(i, codeToID(code))
			break
		i += 1

	print(seatIDs)

print(seatIDs)

i = 1
for ID in seatIDs:

#	try:
	#print(seatIDs[i] - ID)
	print(ID)
	if (seatIDs[i] - ID) > 1:
		print("!!!" + str(ID + 1) + "!!!")
		break

#	except:
#		break

	i += 1




