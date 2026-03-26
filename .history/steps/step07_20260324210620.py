import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        output.set_creator = self   # 让输出变量保存创造者信息
        self.input = input
        self.output = output        # 保存输出变量
        return output
    
    def forward()
