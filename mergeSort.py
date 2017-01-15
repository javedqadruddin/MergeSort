import sys

testArray1 = [1,2,4,3,5,6]
testArray2 = [6,5,4,3,2,1]
testArray3 = [1,2,4,3,5]
testArray4 = [2,1,3,4,5]
testArray5 = [2,1,3,4,5,6]
testArray6 = [2,1,3,4]


def sort(inputList):
	if len(inputList) <= 1:
		return inputList
	left = sort(inputList[:len(inputList)/2])
	right = sort(inputList[len(inputList)/2:])

	#print(left)
	#print(right)

	return merge(left, right)

	
def merge(left, right):
	outputList = []
	#reverse the lists so that when we pop(), it pops from the correct side (the beginnning of the list in its un-reverse order) 
	left.reverse()
	right.reverse()

	#reverse again so we are starting at the beginning of each list
	for leftItem in left[::-1]:
		for rightItem in right[::-1]:
			if leftItem < rightItem:
				outputList.append(left.pop())
				break
			else:
				outputList.append(right.pop())
	#picking pp residual items left in either list (the highest value will be left behind otherwise)
	if len(left) > 0:
		for item in left[::-1]: outputList.append(item)
	if len(right) > 0:
		for item in right[::-1]: outputList.append(item)

	return outputList



def testSort():
	print("testArray5")
	print(sort(testArray5))
	print("testArray3")
	print(sort(testArray3))
	print("testArray6")
	print(sort(testArray6))

def testMerge():
	print "2,4 and 1,3"
	print(merge([2,4],[1,3]))
	print "1,3,5 and 2,4"
	print(merge([1,3,5],[2,4]))
	print "4,5,6 and 1,2,3"
	print(merge([4,5,6],[1,2,3]))
	print("4,5,7 and 1,2,6")
	print(merge([4,5,7],[1,2,6]))

testSort()



