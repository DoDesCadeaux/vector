class Vector:
    def __init__(self, value):
        if not all(len(row) == 1 or len(value) == 1 for row in value):
            raise ValueError("All rows must be size of 1")

        self.value = value
        if all(len(elem) == 1 for elem in value):
            self.shape = (len(value), 1)
        else:
            self.shape = (1, len(value[0]))

    def __str__(self):
        return f"Vector({self.value}) of shape {self.shape}"

    def __add__(self, other):
        if self.shape != other.shape:
            raise TypeError("cannot add different vector shapes")
        if self.shape[0] == 1:
            value = []
            for elem_s, elem_o in zip(self.value[0], other.value[0]):
                value.append(elem_s + elem_o)
            return Vector([value])
        else:
            value = []
            for elem_s, elem_o in zip(self.value, other.value):
                value.append([elem_s[0] + elem_o[0]])
            return Vector(value)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if self.shape != other.shape:
            raise TypeError("connot substract different vector shapes")
        if self.shape[0] == 1:
            value = []
            for elem_s, elem_o in zip(self.value[0], other.value[0]):
                value.append(elem_s - elem_o)
            return Vector([value])
        else:
            value = []
            for elem_s, elem_o in zip(self.value, other.value):
                value.append([elem_s[0] - elem_o[0]])
            return Vector(value)
    
    def __rsub__(self, other):
        return other.__sub__(self)

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError
        elif not isinstance(other, (int, float)):
            raise ValueError("Scalar division must be a int or float")
        if self.shape[0] == 1:
            value = []
            for elem in self.value[0]:
                value.append(elem / other)
            return Vector([value])
        else:
            value = []
            for elem in self.value:
                value.append([elem[0] / other])
            return Vector(value)
    
    def __rtruediv__(self, _):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Scalar product should be int or float")
        if self.shape[0] == 1:
            value = []
            for elem in self.value[0]:
                value.append(elem * other)
            return Vector([value])
        else:
            value = []
            for elem in self.value:
                value.append([elem[0] * other])
            return Vector(value)
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self) -> str:
        return f"Vector({self.value}) of shape {self.shape}"

    def dot(self, other):
        if self.shape != other.shape:
            raise TypeError("Cannot dot product between different vector shapes")
        if self.shape[0] == 1:
            products = []
            for elem_s, elem_o in zip(self.value[0], other.value[0]):
                products.append(elem_s * elem_o)
            return sum(products)        
        else:
            products = []
            for elem_s, elem_o in zip(self.value, other.value):
                products.append(elem_s[0] * elem_o[0])
            return sum(products)
    
    def T(self):
        if self.shape[0] == 1:
            value = []
            for elem in self.value[0]:
                value.append([elem])
            return Vector(value)
        else:
            value = []
            for elem in self.value:
                value.append(elem[0])
            return Vector([value])

