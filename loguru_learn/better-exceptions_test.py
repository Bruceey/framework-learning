## 设置不截断
# import better_exceptions
# better_exceptions.MAX_LENGTH = None


def func(a, b):
    return a / b

def nested(c):
    func(5, c)

nested(0)