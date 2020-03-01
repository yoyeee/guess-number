import random
print('這是一個猜數字的遊戲')
start = input('請輸入最小值：')
end = input('請輸入最大值：')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	number = input('遊戲開始，請輸入數字：')
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
