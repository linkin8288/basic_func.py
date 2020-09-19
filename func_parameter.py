# parameter(參數)(形容成投幣孔):
# 1.當function需要外部資料的時候，我們就設計投幣孔(參數)，把資料投進function裡面
# 參數有預設值，那就不一定要投給他

def wash(dry=False, water=8): # [定義]function，但沒執行功能
	print('加水', water, '分滿')
	print('加洗衣精')
	print('旋轉')
	if dry:
		print('烘衣')

wash(water=10)


def say_hi():
	print('hi')

def add(x=1, y=2):
	print(x + y)

add()