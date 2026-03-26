import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        f = self.creator            # 1. 获取函数
        if f is not None:
            x = f.input             # 2. 获取函数输入
            x.grad = f.backward(self.grad)  # 3. 调用函数的backward方法
            x.backward()            # 4. 调用自己前面那个变量的backward方法(递归)
