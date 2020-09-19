# function 函式/功能
# function 是用來[收納]程式碼的
# 他是個功能,用來增加程式碼的重複使用性
# def func():

def wash(dry): # [定義]function，但沒執行功能
	print('加水')
	print('加洗衣精')
	print('旋轉')
	if dry:
		print('烘衣')

wash() # 使用function功能()

def say_hi():
	print('hi')

say_hi()