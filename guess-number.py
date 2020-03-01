import random

r = random.randint(1, 100)
count = 0

while True:
	number = input('請輸入數字：')
	number = int(number)
	count = count + 1

	if number == r:
		print('恭喜正確')
		print('這是你猜的第', count, '次')
		break
	elif number > r:
			print('比答案大')
	elif number < r:
			print('比答案小')
	print('這是你猜的第', count, '次')
