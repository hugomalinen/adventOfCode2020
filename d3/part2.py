# Open file with input inside and form it into a list

f = open('./input.txt', 'r')
data = f.readlines()

# Remove \n from each string

for t in enumerate(data):
    data[t[0]] = data[t[0]].split("\n")[0]

# Function to find the n of trees on a certain path defined by a slope

def nOfTrees(incX, incY):

	x = 0
	y = 0
	nTrees = 0
	
	# Loop to go through the map and check each point on
	# a slope incX left incY down for trees

	while y < len(data)-1:
		x += incX
		y += incY
	
		# x%(length of one row) constrains the x value between
		# 0 and the maximum index
		if data[y][x%(len(data[0]))] == '#':
			nTrees += 1

	return(nTrees)

slopes = [
		[1,1],
		[3,1],
		[5,1],
		[7,1],
		[1,2]
		]

# Multiply all found nOfTrees together for answer

ans = 1
for slope in slopes:
	ans = ans * nOfTrees(slope[0], slope[1])

print(ans)	
