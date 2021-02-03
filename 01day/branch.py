# 根据用户输入，走不同的计算分支
#
#         3x - 5  (x > 1)
# f(x) =  x + 2   (-1 <= x <= 1)
#         5x + 3  (x < -1)

x = float(input('x='))
y = 0
if x > 1:
    y = 3 * x - 5
elif -1 <= x <= 1:
    y = x + 2
elif x < -1:
    y = 5 * x + 3
print(y)


#
# 百分制成绩转换为等级制成绩
#
# 如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
#

score = 90
result = ''
if score >= 90:
    result = 'a'
elif 80 <= score < 90:
    result = 'b'
elif 70 <= score < 80:
    result = 'c'
elif 60 <= score < 70:
    result = 'd'
else:
    result = '不及格'
print(result)


