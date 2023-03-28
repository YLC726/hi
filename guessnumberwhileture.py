import random

r1 = input("你要猜的起頭:")
r2 = input("你要猜的結尾:")
r1 = int(r1)
r2 = int(r2)

x = random.randint(r1, r2)

while True:
	y = input("猜猜看:")
	y = int(y)
	if x == y:
		print("恭喜壓恭喜發壓發大財!!")
		break
	elif x > y:
		print("太小了!!!!!死白癡")
	elif x < y:
		print("太大了!!!!!智障喔!")
