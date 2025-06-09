## 设置不截断
# import better_exceptions
# better_exceptions.MAX_LENGTH = None
# 设置环境变量为BETTER_EXCEPTIONS=1

def func(a, b):
    return a / b

def nested(c):
    func(5, c)

nested(0)