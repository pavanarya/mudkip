import numpy as np



class Conv2D:
    def __init__(self,units,kernel_size=(3,3),stride=2):
        self.input_array = None
        self.kernel_size = kernel_size
        self.units = units
        self.stride = stride
        self.weights = []
        self.result = []
        self.name = "Conv2D"

    def calculate(self):
        self.weights = np.random.rand(self.units, self.kernel_size[0], self.kernel_size[1])
        
        i, j, row, col = 0, 0, 0, 0
        while i<= self.input_array.shape[1] and i+self.kernel_size[1] <= self.input_array.shape[1]:
            while j<= self.input_array.shape[0] and j+self.kernel_size[0] <= self.input_array.shape[0]:
                self.result.append(list(np.array([np.sum(np.multiply(self.input_array[i:i+3,j:j+3],weight)) for weight in self.weights])))
                j = j + self.stride
                if i == 0:
                    col = col + 1
            i = i + self.stride
            j = 0
            row = row + 1

        self.result = np.array(self.result).reshape(self.units,row,col)
        return self.result

