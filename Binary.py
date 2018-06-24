
#二进制搜索
#idea主要是二分法在数组中找到一个数字
#从数组中间开始，测试指定的数字是否是它正在查找的数字，
#如果数字更大，则将继续将数组分割，检查下半部分
#重复相同的操作
def read_file(filename):
	with open(filename) as f:
		return [int(x) for x in next(f).split()]
	"""
	需要从数组中提取数字到文档
	"""
	pass


def binary_search(low, high, search, numbers):
	found = False
	while low<=high and not found:
		pos = 0
		midpoint = (low + high)//2
		if numbers[midpoint] == search:
			pos = midpoint
			found = True
		else:
			if search < numbers[midpoint]:
				high = midpoint-1
			else:
				low = midpoint+1
	return (pos, found)
	pass

numbers = read_file("sample.array")
b=(binary_search(0,len(numbers)-1,3,numbers))
if(b[1]==False):
	print("Not Found")
else:
	print("Found")


