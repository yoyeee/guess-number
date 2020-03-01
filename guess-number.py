import random
r = random.randint(1, 100)
while True:
	number = input('請輸入數字：')
	number = int(number)
	if number == r:
		print('恭喜正確')
		break
	else:
		if number > r:
			print('比答案大')
		if number < r:
			print('比答案小')
