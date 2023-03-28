import random

r1 = input("你要猜的起頭:")
r2 = input("你要猜的結尾:")
r1 = int(r1)
r2 = int(r2)

x = random.randint(r1, r2)
count = 0 #count要放在while外面不然就會每次都歸零

while True:
	count += 1 #count += 1就是count=count+1
	y = input("猜猜看:")
	y = int(y)
	if x == y:
		print("恭喜壓恭喜發壓發大財!!")
		print("猜到第",count,"次才猜到，真的是喜憨兒!!")
		break
	elif x > y:
		print("太小了!!!!!死白癡")
	elif x < y:
		print("太大了!!!!!智障喔!")
	print("已經猜",count,"次了喔!到底多憨")
