import random

x = random.randint(1, 100)

y = input("1至100猜猜看:")

y = int(y)
 
while x > y:
	print("太小了!!!!!死白癡")
	y = input("繼續猜猜看:")
	y = int(y)
while x < y:
	print("太大了!!!!!智障喔!")
	y = input("繼續猜猜看:")
	y = int(y)
while x == y:
	print("終於答對了")
	break
