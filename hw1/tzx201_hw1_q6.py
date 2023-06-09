"""
tzx201_hw1_q6
"""

class Vector:
    def __init__(self, d):
        if type(d) == int:
            self.coords = [0]*d
        elif type(d) == list:
            self.coords = d
        else:
            raise TypeError("please enter a valid parameter")
    def __len__(self):
        return len(self.coords)
    def __getitem__(self, j):
        return self.coords[j]
    def __setitem__(self, j, val):
        self.coords[j] = val
    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        return self.coords == other.coords
    def __ne__(self, other):
        return not (self == other)
    def __str__(self):
        return '<'+ str(self.coords)[1:-1]+'>'
    def __repr__(self):
        return str(self)
    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self.coords)):
            result[i] = self[i] * -1
        return result
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            result = Vector(len(self))
            for i in range(len(self.coords)):
                result[i] = self[i] * other
            return result
        elif type(other) == Vector:
            dot_list = []
            if len(self) != len(other):
                raise ValueError('dimensions must agree')
            for i in range(len(self)):
                dot_list.append(self[i] * other[i])
            return sum(dot_list)
        else:
            raise TypeError('vector cannot be multiplied by anything other than another vector or a number')
    def __rmul__(self, num):
        result = Vector(len(self))
        for i in range(len(self.coords)):
            result[i] = self[i] * num
        return result
            


def main():
    v1 = Vector(5)
    v1[1] = 10
    v1[-1] = 10
    print(v1)
    v2 = Vector([2, 4, 6, 8, 10])
    v3 = -v2
    print(v3)
    v4 = v2*3
    print(v4)
    v5 = 3*v2
    print(v5)
    v6 = v2 * v3
    print(v6)
    v7 = v2 * Vector(4)
    print(v7)
    

