import random

rang1 = int(input("请设置本局游戏的最小值:"))
rang2 = int(input("请设置本局游戏的最大值:"))
num = random.randint(rang1, rang2)
guess = "guess"
print("数字猜谜游戏！")
i = 0
while guess != num:
    i += 1
    guess = int(input("请输入你猜的数字："))

    if guess == num:
        print("恭喜，你猜对了！")
    elif guess < num:
        print("你猜的数小了...")
    else:
        print("你猜的数大了...")

print("你总共猜了%d" % i + "次", end='')
print(",快和你朋友较量一下...")