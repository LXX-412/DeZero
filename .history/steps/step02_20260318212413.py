class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        reutrn output

    def forward(self, x):
        raise NotImplementedError()
    