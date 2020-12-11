# Open file with input inside

f = open('./input.txt', 'r')
data = f.readlines()

# Remove \n from each string

for t in enumerate(data):
    data[t[0]] = data[t[0]].split("\n")[0]

# Function to make sure that the index n is in found in string s
# Will return the letter in that index if found, otherwise
# will return a space

def indextest(s, n):
	try:
		return(s[n-1])
	except:
		return(' ')

# Loop to find the password info and the characters in the indexed
# positions in the password and the number of compliant passwords

nCompliant = 0
for s in data:
	
	info  = s.split(' ')
	index = info[0].split('-')

	cMin  = indextest(info[2], int(index[0]))
	cMax  = indextest(info[2], int(index[1]))	

# If the first indexed char is the required char XOR the last
# indexed char is the required char

	if (cMin == info[1][0]) ^ (cMax == info[1][0]):
		nCompliant += 1	

print(nCompliant)
