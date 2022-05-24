
# Author: Jeremiah Morton
# RMS Technology Consulting Test

# Sources: 	https://gist.github.com/Olical/2306105
#			https://www.geeksforgeeks.org/largest-product-subarray-size-k/
#			https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/?ref=lbp

import random

################################################################################################

class Grid():
    def __init__(self, width, height, default=''):
        self.width = width
        self.height = height
        self.data = [[default for y in range(height)] for x in range(width)]
    
    def set(self, x, y, value):
        self.data[y][x] = value
    
    def get(self, x, y):
        return self.data[y][x]

################################################################################################

# Extension of the RotatableGrid class that can render to text and rotate
class DisplayableGrid(Grid):
    def __str__(self):
        return self.render()
    
    def render(self):
        res = []
        
        horiSplit = ' | '
        vertSplit = '\n +' + '---+' * self.height + '\n'
        
        for row in self.data:
            res.append(horiSplit + horiSplit.join(row) + horiSplit)
        
        return vertSplit + vertSplit.join(res) + vertSplit

################################################################################################

def find_greatest_product_of_contiguous_integers(grid: Grid, contiguous_integers: int) -> int:

	NumberOfCombinations = 0
	MaxGridProduct = 0
	CurrentCount = 0

	if(contiguous_integers > grid.width and contiguous_integers > grid.height):
		print("No Combinations, limited by size of grid\n")
		return 0

	# Check all rows
	for i in range(Width):
		currentList = []
		for j in range(Height):
			currentList.append(grid.get(j, i))
		IterationMax, CurrentCount = findMaxProduct(currentList, len(currentList), contiguous_integers)
		MaxGridProduct = max(MaxGridProduct, IterationMax)
		NumberOfCombinations += CurrentCount

	# Check all columns
	for i in range(Height):
		currentList = []
		for j in range(Width):
			currentList.append(grid.get(i, j))

		IterationMax, CurrentCount = findMaxProduct(currentList, len(currentList), contiguous_integers)
		MaxGridProduct = max(MaxGridProduct, IterationMax)
		NumberOfCombinations += CurrentCount

	#Check all diagonals in both directions
	DiagonalList = getDiagonals(grid)

	for current in range(len(DiagonalList)):
		IterationMax, CurrentCount = findMaxProduct(DiagonalList[current], len(DiagonalList[current]), contiguous_integers)
		MaxGridProduct = max(MaxGridProduct, IterationMax)
		NumberOfCombinations += CurrentCount

	# Print Results
	print('Number of Different Combinations: ', NumberOfCombinations)
	print('Greatest Product of ', contiguous_integers, ' adjacent numbers: ', MaxGridProduct, '\n')

	return MaxGridProduct

################################################################################################

# This function returns a list of lists that represent all of the diagonals in a grid

def getDiagonals(grid: DisplayableGrid):

	ROW = grid.height
	COL = grid.width
	listOfDiagonals = []

	# Down and to the right

	for line in range(1, (ROW + COL)):
		# Get column index of the first element in this line of output. The index is 0 for first ROW lines and line - ROW for remaining lines
		start_col = max(0, line - ROW)

		# Get count of elements in this line. The count of elements is equal to minimum of line number, COL-start_col and ROW
		count = min(line, (COL - start_col), ROW)

		currentList = []

		# Get elements of this line
		for j in range(0, count):
			x = min(ROW, line) - j - 1
			y = start_col + j
			currentList.append(grid.get(x,y))

		listOfDiagonals.append(currentList)



	# Up and to the right

	for line in range(1, (ROW + COL)):
		# Get column index of the first element in this line of output. The index is 0 for first ROW lines and line - ROW for remaining lines
		start_col = max(0, line - ROW)

		# Get count of elements in this line. The count of elements is equal to minimum of line number, COL-start_col and ROW
		count = min(line, (COL - start_col), ROW)

		currentList = []

		# Get elements of this line
		for j in range(0, count):
			x = min(ROW, line) - j - 1
			y = (grid.width - (start_col + j) - 1)
			currentList.append(grid.get(x,y))

		listOfDiagonals.append(currentList)
	return listOfDiagonals

################################################################################################

# This function returns maximum product of a subarray of size k in given array, arr[0..n-1].
def findMaxProduct(arr, n, k):

	count = 0

	if(k>n):
		return 0, 0

	MaxProduct = 1
	for i in range(0, k):
		MaxProduct = MaxProduct * int(arr[i])
	prev_product = MaxProduct
	count += 1

	# Consider every product beginning with arr[i] where i varies from 1 to n-k+1
	for i in range(1, n - k + 1):
		count += 1
		if(int(arr[i-1]) != 0):
			curr_product = (prev_product // int(arr[i-1])) * int(arr[i+k-1])
		MaxProduct = max(MaxProduct, curr_product)
		prev_product = curr_product

	# Return the maximum product found
	return MaxProduct, count

################################################################################################

# Testing setup

# Define Width and Height and the Number of Continuous Ints
Width = 10
Height = 15
ContinuousInts = 7

# Define Grid Object, set up
grid = DisplayableGrid(width=Width, height=Height)

for i in range(Width):
	for j in range(Height):
		randomNumber = int(random.random()*100)
		grid.set(j, i, str(randomNumber))

print(grid.render())

# Answer Questions 1 and 2
find_greatest_product_of_contiguous_integers(grid, ContinuousInts)

################################################################################################
