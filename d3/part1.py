# Open file with input inside and form it into a list

f = open('./input.txt', 'r')
data = f.readlines()

# Remove \n from each string

for t in enumerate(data):
    data[t[0]] = data[t[0]].split("\n")[0]

x = 0
y = 0
nTrees = 0

# Loop to go through the map and check each point on
# a slope 3 left 1 down for trees

while y < len(data)-1:
	x += 3
	y += 1

	# x%(length of one row) constrains the x value between
	# 0 and the maximum index
	if data[y][x%(len(data[0]))] == '#':
		nTrees += 1

print(nTrees)
