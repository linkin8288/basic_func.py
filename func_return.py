# return 回傳，可以把function執行的結果儲存下來

def add(x, y):
	return x + y

result = add(3, 4)
print(result)

def average(numbers):
	return sum(numbers) / len(numbers) # sum是清單的加總，算平均
	
print(average([1, 2, 3]))
print(average([23, 6, 100]))

