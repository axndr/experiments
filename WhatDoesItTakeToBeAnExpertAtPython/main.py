class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return f'{self.coeffs[0]}x\u00b2+{self.coeffs[1]}x+{self.coeffs[2]}'

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))
        # return Polynomial(*(
        #     (self.coeffs[0] + other.coeffs[0]),
        #     (self.coeffs[1] + other.coeffs[1]),
        #     (self.coeffs[2] + other.coeffs[2])
        #

    def __len__(self):
        return len(self.coeffs)


if __name__ == '__main__':
    p1, p2 = Polynomial(1, 2, 3), Polynomial(3, 4, 3)
    print(p1)
    print(p2)
    p3 = p1 + p2
    print(p3)
    print(len(p1))