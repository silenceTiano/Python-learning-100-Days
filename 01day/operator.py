# 算术运算符

print(321 + 123)  # 加法运算
print(321 - 123)  # 减法运算
print(321 * 123)  # 乘法运算
print(321 / 123)  # 除法运算
print(321 % 123)  # 求模运算
print(321 // 123)  # 整除运算
print(321 ** 123)  # 求幂运算

# 赋值运算符
a = 10
b = 3
a += b  # 相当于：a = a + b
a *= a + 2  # 相当于：a = a * (a + 2)


# 将华氏温度转换为摄氏温度
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# 计算年份是否是闰年
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)

