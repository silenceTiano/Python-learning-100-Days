import random

# 用for循环实现1~100求和
x = 0
for i in range(0, 101):
    x += i
print(x)
# 上面代码中的range(1, 101)可以用来构造一个从1到100的范围，当我们把这样一个范围放到for-in循环中，
# 就可以通过前面的循环变量x依次取出从1到100的整数。


# 用for循环实现1~100之间的偶数求和
rsum = 0
for x in range(2, 101, 2):
    rsum += x
print(rsum)
# range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
# range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
# range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。


# 打印99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()


# 猜大小游戏
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
