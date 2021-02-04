def foo():
    print('goodbye, world!')


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
# 也是说只有当前的模块被直接执行的时候，才会执行下面的语句，引入的时候因为模块名不是__main__因此不会执行
if __name__ == '__main__':
    print('我是模块一的可执行部分')
